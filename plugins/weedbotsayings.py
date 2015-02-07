# WeedBot Refresh's weedbotsayings.py - Py3 version

import random
from cloudbot import hook
import re

cs = "( .__.) . o O ( cum )"
ms = "( ï¾Ÿ ãƒ®ï¾Ÿ)ã€€ï¼­ï¼©ï¼´ï¼¯ï¼® ï¼§ï¼¡ ï¼³ï¼µï¼«ï¼©ï¼ï¼ï¼ï¼"
cp = "( ãƒ»Ï‰ãƒ») . o O ( crap ass )"
ft = "ãƒ¾(Â´â–¡ï½€* )ãƒŽ ftw ãƒ¾(@ã‚œâˆ‡ã‚œ@)ãƒŽ ftw o(â‰§âˆ‡â‰¦o) ftw (Â´âˆ‡ï¾‰ï½€*)ãƒŽ"
ap = "( ï½¥à¸´Ð·ï½¥à¸´) apple basically makes the best computers.. heh"
da = "Î¾ ãƒ»_>ãƒ»ï¼‰don't touch dad's diskettes"
ta = "(â•¯Â°â–¡Â°ï¼‰â•¯ï¸µ â”»â”â”» i'm so fuckin mad right now"
gi = "ï½·ï¾€ï¾œã‚¡*ï½¥ã‚œï¾Ÿï½¥*:.ï½¡..ï½¡.:*ï½¥ã‚œ(nâ€˜âˆ€â€˜)Î·ï¾Ÿï½¥*:.ï½¡. .ï½¡.:*ï½¥ã‚œï¾Ÿï½¥* !!!!! oh my god i'm a girl!!!"

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
