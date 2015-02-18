# WeedBot Refresh's weedbotsayings.py - Py3 version

import random
from cloudbot import hook
import re

cs = unicode("I can take a 9-inch dildo up my butt, because I’m an adult and I solve my own problems", encoding="utf-8")
ms = unicode("stop oppressing white people plz", encoding="utf-8")
cp = unicode("(⊙︿⊙)  crap ass ", encoding="utf-8")
ft = unicode("This seems like an appropriate time to tell you what my penis thinks", encoding="utf-8")
ap = unicode("plz censor your slurs  \(@_@)/", encoding="utf=8")
da = unicode("heh dae le skytheists?", encoding="utf-8")
ta = unicode("I do not support this request.", encoding="utf-8")
gi = unicode("I am laid low by the matriarchy!", encoding="utf-8")
li = unicode("I know now I'll never have any flair again and I've come to terms with that.", encoding="utf-8")
dong1 = unicode("ヽ༼ຈل͜ຈ༽ﾉ raise your dongers ヽ༼ຈل͜ຈ༽ﾉ", encoding="utf-8")
dong2 = unicode("ヽ༼ຈل͜ຈ༽ﾉ WHAT DOESNT KILL ME ONLY MAKES ME DONGER ᕙ༼ຈل͜ຈ༽ᕗ", encoding="utf-8")
dong3 = unicode("ヽ༼ຈل͜ຈ༽ﾉ ITS A HARD DONG LIFE ヽ༼ຈل͜ຈ༽ﾉ", encoding="utf-8")
dong4 = unicode("ᕙ༼ຈل͜ຈ༽ᕗ. ʜᴀʀᴅᴇʀ,﻿ ʙᴇᴛᴛᴇʀ, ғᴀsᴛᴇʀ, ᴅᴏɴɢᴇʀ .ᕙ༼ຈل͜ຈ༽ᕗ", encoding="utf-8")
dong5 = unicode("work it ᕙ༼ຈل͜ຈ༽ᕗ harder make it (ง •̀_•́)ง better do it ᕦ༼ຈل͜ຈ༽ᕤ faster raise ur ヽ༼ຈل͜ຈ༽ﾉ donger", encoding="utf-8")
dong6 = unicode("ᕦ༼ຈل͜ຈ༽ᕤ ＤＯ ＹＯＵ ＥＶＥＮ ＤＯＮＧ? ᕦ༼ຈل͜ຈ༽ᕤ", encoding="utf-8")
dong7 = unicode("ง ͠ ͠° ͟ل͜ ͡°)ง sᴏᴜɴᴅs ᴅᴏɴɢᴇʀᴏᴜs... ɪᴍ ɪɴ (ง ͠ ͠° ͟ل͜ ͡°)ง", encoding="utf-8")
gg = unicode("actually, its about ethics in games journalism", encoding="utf-8")
randomness_const = 2

@hook.regex(re.compile(r'cum', re.I))
def cum(message):
    if random.randrange(1,10+1) >= randomness_const:
        message(cs)


@hook.regex(re.compile(r'mitten', re.I))
def mitten(message):
    if random.randrange(1,10+1) >= randomness_const:
        message(ms)


@hook.regex(re.compile(r'crap', re.I))
def crap(message):
    if random.randrange(1,10+1) >= randomness_const:
        message(cp)


@hook.regex(re.compile(r'ass', re.I))
def ass(message):
    if random.randrange(1,10+1) >= randomness_const:
        message(cp)


@hook.regex(re.compile(r'\\bftw\\b', re.I))
def ftw(message):
    if random.randrange(1,10+1) >= randomness_const:
        message(ft)


@hook.regex(re.compile(r'\\bown(s|ed)?\\b', re.I))
def owns(message):
    ons = "owns " * random.randint(1, 3) + "OWNS " * random.randint(1, 3) + "o-(' 'Q)"
    if random.randrange(1,10+1) >= randomness_const:
        message(ons)


@hook.regex(re.compile(r'\\bapple\\b', re.I))
def apple(message):
    if random.randrange(1,10+1) >= randomness_const:
        message(ap)


@hook.regex(re.compile(r'weedbot', re.I))
def weedbotname(message):
    if random.randrange(1,10+1) >= randomness_const:
        message(random.choice([":D", "hi!", "weed", "gotta love me!", "guess who has a boner", "weeeeeeed", "weeeeeeeeeeeeeeeeed"]))


@hook.regex(re.compile(r'\\bdad\\b', re.I))
def dad(message):
    if random.randrange(1,10+1) >= randomness_const:
        message(da)


@hook.regex(re.compile(r'\\b(mad|angry)\\b', re.I))
def mad(message):
    if random.randrange(1,10+1) >= randomness_const:
        message(ta)


@hook.regex(re.compile(r'\\bgirl\\b', re.I))
def girl(message):
    if random.randrange(1,10+1) >= randomness_const:
        message(gi)
