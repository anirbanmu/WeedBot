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

@hook.nonick
@hook.regex(*("cum", re.I))
@hook.randreply(0.0)
def cum(text):
    return cs

@hook.nonick
@hook.regex(*("mitten", re.I))
@hook.randreply(0.0)
def mitten(text):
    return ms

@hook.nonick
@hook.regex(*("crap", re.I))
@hook.randreply(0.0)
def crap(text):
    return cp

@hook.nonick
@hook.regex(*("ass", re.I))
@hook.randreply(0.0)
def ass(text):
    return cp

@hook.nonick
@hook.regex(*("\\bftw\\b", re.I))
@hook.randreply(0.0)
def ftw(text):
    return ft

@hook.nonick
@hook.regex(*("\\bown(s|ed)?\\b", re.I))
@hook.randreply(0.0)
def owns(text):
    ons = "owns " * random.randint(1, 3) + "OWNS " * random.randint(1, 3) + "o-(' 'Q)"
    return ons

@hook.nonick
@hook.regex(*("\\bapple\\b", re.I))
@hook.randreply(0.0)
def apple(text):
    return ap

@hook.nonick
@hook.regex(*("weedbot", re.I))
@hook.randreply(0.0)
def weedbotname(text):
    return random.choice([":D", "hi!", "weed", "gotta love me!", "guess who has a boner", "weeeeeeed", "weeeeeeeeeeeeeeeeed"])

@hook.nonick
@hook.regex(*("\\bdad\\b", re.I))
@hook.randreply(0.0)
def dad(text):
    return da

@hook.nonick
@hook.regex(*("\\b(mad|angry)\\b", re.I))
@hook.randreply(0.0)
def mad(text):
    return ta

@hook.nonick
@hook.regex(*("\\bgirl\\b", re.I))
@hook.randreply(0.0)
def girl(text):
    return gi
