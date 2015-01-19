# WeedBotRefresh's comic.py - based on nekosune's comic.py

from cloudbot import hook
import os
from random import shuffle
import random
from PIL import Image, ImageDraw, ImageFont
import base64
import requests
import json
from datetime import datetime
from io import BytesIO

from cloudbot.event import EventType

mcache = dict()

@hook.on_start()
def load_key(bot):
    global dev_key
    global background_file
    dev_key = bot.config.get("api_keys", {}).get("imgur_client_id")
    background_file = bot.config.get("resources", {}).get("background")

@hook.event([EventType.message, EventType.action], ignorebots=False, singlethread=True)
def track(event, db, conn):
    key = (event.chan, conn.name)
    if key not in mcache:
        mcache[key] = []

    value = (datetime.now(), event.nick, str(event.content))
    mcache[key].append(value)
    buffer_size = 30
    mcache[key] = mcache[key][-1*buffer_size:]


@hook.command("comic")
def comic(conn, chan):
    text = chan
    msgs = mcache[(text, conn.name)]
    sp = 0
    chars = set()

    for i in range(len(msgs)-1, 0, -1):
        sp += 1
        diff = msgs[i][0] - msgs[i-1][0]
        chars.add(msgs[i][1])
        if sp > 10 or diff.total_seconds() > 120 or len(chars) > 3:
            break

    msgs = msgs[-1*sp:]

    panels = []
    panel = []

    for (d, char, msg) in msgs:
        if len(panel) == 2 or len(panel) == 1 and panel[0][0] == char:
            panels.append(panel)
            panel = []
        if msg.count('\x01') >= 2:
            ctcp = msg.split('\x01', 2)[1].split(' ', 1)
            if len(ctcp) == 1:
                ctcp += ['']
            if ctcp[0]=='ACTION':
                msg='*'+ctcp[1]+'*'
        panel.append((char, msg))

    panels.append(panel)

    print(repr(chars))
    print(repr(panels))
    fname = ''.join([random.choice("fartpoo42069") for i in range(16)]) + ".jpg"
    imgtpath = "imgtemp"
    make_comic(chars, panels).save(os.path.join(imgtpath, fname), quality=85)
    API_KEY = "df9c92f33223cd4"
    image_path = os.path.join(imgtpath,fname)
    headers = {'Authorization': 'Client-ID ' + API_KEY}
    fh = open(image_path, 'rb')
    base64img = base64.b64encode(fh.read())
    url="https://api.imgur.com/3/upload.json"
    r = requests.post(url, data={'key': API_KEY, 'image':base64img,'title':'apitest'},headers=headers,verify=False)
    print(r.text)
    val=json.loads(r.text)
    return val['data']['link']


def wrap(st, font, draw, width):
    #print "\n\n\n"
    st = st.split()
    mw = 0
    mh = 0
    ret = []

    while len(st) > 0:
        s = 1
        #print st
        #import pdb; pdb.set_trace()
        while True and s < len(st):
            w, h = draw.textsize(" ".join(st[:s]), font=font)
            if w > width:
                s -= 1
                break
            else:
                s += 1

        if s == 0 and len(st) > 0: # we've hit a case where the current line is wider than the screen
            s = 1

        w, h = draw.textsize(" ".join(st[:s]), font=font)
        mw = max(mw, w)
        mh += h
        ret.append(" ".join(st[:s]))
        #print st[:s]
        #print
        st = st[s:]

    return (ret, (mw, mh))

def rendertext(st, font, draw, pos):
    ch = pos[1]
    for s in st:
        w, h = draw.textsize(s, font=font)
        draw.text((pos[0], ch), s, font=font, fill=(0xff,0xff,0xff,0xff))
        ch += h

def fitimg(img, width, height):
    scale1 = float(width) / img.size[0]
    scale2 = float(height) / img.size[1]

    l1 = (img.size[0] * scale1, img.size[1] * scale1)
    l2 = (img.size[0] * scale2, img.size[1] * scale2)

    if l1[0] > width or l1[1] > height:
        l = l2
    else:
        l = l1

    return img.resize((int(l[0]), int(l[1])), Image.ANTIALIAS)

def make_comic(chars, panels):
    #filenames = os.listdir(os.path.join(os.getcwd(), 'chars'))

    panelheight = 300
    panelwidth = 450

    filenames = os.listdir('chars/')
    shuffle(filenames)
    filenames = map(lambda x: os.path.join('chars', x), filenames[:len(chars)])
    chars = list(chars)
    chars = zip(chars, filenames)
    charmap = dict()
    for ch, f in chars:
        charmap[ch] = Image.open(f)

    #print charmap


    imgwidth = panelwidth
    imgheight = panelheight * len(panels)

    bg = Image.open("backgrounds/Backdrop.jpg")

    im = Image.new("RGBA", (imgwidth, imgheight), (0xff, 0xff, 0xff, 0xff))
    font = ImageFont.truetype("plugins/FiraSansLight.ttf", 18)

    for i in range(len(panels)):
        pim = Image.new("RGBA", (panelwidth, panelheight), (0xff, 0xff, 0xff, 0xff))
        pim.paste(bg, (0, 0))
        draw = ImageDraw.Draw(pim)

        st1w = 0; st1h = 0; st2w = 0; st2h = 0
        (st1, (st1w, st1h)) = wrap(panels[i][0][1], font, draw, 2*panelwidth/3.0)
        rendertext(st1, font, draw, (10, 10))
        if len(panels[i]) == 2:
            (st2, (st2w, st2h)) = wrap(panels[i][1][1], font, draw, 2*panelwidth/3.0)
            rendertext(st2, font, draw, (panelwidth-10-st2w, st1h + 10))

        texth = st1h + 10
        if st2h > 0:
            texth += st2h + 10 + 5

        maxch = panelheight - texth
        im1 = fitimg(charmap[panels[i][0][0]], 2*panelwidth/5.0-10, maxch)
        pim.paste(im1, (10, panelheight-im1.size[1]), im1)

        if len(panels[i]) == 2:
            im2 = fitimg(charmap[panels[i][1][0]], 2*panelwidth/5.0-10, maxch)
            im2 = im2.transpose(Image.FLIP_LEFT_RIGHT)
            pim.paste(im2, (panelwidth-im2.size[0]-10, panelheight-im2.size[1]), im2)

        draw.line([(0, 0), (0, panelheight-1), (panelwidth-1, panelheight-1), (panelwidth-1, 0), (0, 0)], (0, 0, 0, 0xff))
        del draw
        im.paste(pim, (0, panelheight * i))

    return im
