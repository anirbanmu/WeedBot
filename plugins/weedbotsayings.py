import random
from util import hook
import re
cs = unicode("( .__.) . o O ( cum )", encoding="utf-8")
ms = unicode("( ï¾Ÿ ãƒ®ï¾Ÿ)ã€€ï¼­ï¼©ï¼´ï¼¯ï¼® ï¼§ï¼¡ ï¼³ï¼µï¼«ï¼©ï¼ï¼ï¼ï¼", encoding="utf-8")
cp = unicode("( ãƒ»Ï‰ãƒ») . o O ( crap ass )", encoding="utf-8")
ft = unicode("ãƒ¾(Â´â–¡ï½€* )ãƒŽ ftw ãƒ¾(@ã‚œâˆ‡ã‚œ@)ãƒŽ ftw o(â‰§âˆ‡â‰¦o) ftw (Â´âˆ‡ï¾‰ï½€*)ãƒŽ", encoding="utf-8")
ap = unicode("( ï½¥à¸´Ð·ï½¥à¸´) apple basically makes the best computers.. heh", encoding="utf=8")
da = unicode("Î¾ ãƒ»_>ãƒ»ï¼‰don't touch dad's diskettes", encoding="utf-8")
ta = unicode("(â•¯Â°â–¡Â°ï¼‰â•¯ï¸µ â”»â”â”» i'm so fuckin mad right now", encoding="utf-8")
gi = unicode("ï½·ï¾€ï¾œã‚¡*ï½¥ã‚œï¾Ÿï½¥*:.ï½¡..ï½¡.:*ï½¥ã‚œ(nâ€˜âˆ€â€˜)Î·ï¾Ÿï½¥*:.ï½¡. .ï½¡.:*ï½¥ã‚œï¾Ÿï½¥* !!!!! oh my god i'm a girl!!!", encoding="utf-8")

@hook.nonick
@hook.regex(*("cum", re.I))
@hook.randreply(0.1)
def cum(inp):
    return cs

@hook.nonick
@hook.regex(*("mitten", re.I))
@hook.randreply(0.1)
def mitten(inp):
    return ms

@hook.nonick
@hook.regex(*("crap", re.I))
@hook.randreply(0.1)
def crap(inp):
    return cp

@hook.nonick
@hook.regex(*("ass", re.I))
@hook.randreply(0.1)
def ass(inp):
    return cp

@hook.nonick
@hook.regex(*("\\bftw\\b", re.I))
@hook.randreply(0.1)
def ftw(inp):
    return ft

@hook.nonick
@hook.regex(*("\\bown(s|ed)?\\b", re.I))
@hook.randreply(0.1)
def owns(inp):
    ons = unicode("owns "*random.randint(1, 3) + "OWNS "*random.randint(1, 3) + "o-(' 'Q)")
    return ons

@hook.nonick
@hook.regex(*("\\bapple\\b", re.I))
@hook.randreply(0.1)
def apple(inp):
    return ap

@hook.nonick
@hook.regex(*("weedbot", re.I))
@hook.randreply(0.1)
def weedbotname(inp):
    return random.choice([":D", "hi!", "weed", "gotta love me!", "guess who has a boner", "weeeeeeed", "weeeeeeeeeeeeeeeeed"])

@hook.nonick
@hook.regex(*("\\bdad\\b", re.I))
@hook.randreply(0.1)
def dad(inp):
    return da

@hook.nonick
@hook.regex(*("\\b(mad|angry)\\b", re.I))
@hook.randreply(0.1)
def mad(inp):
    return ta

@hook.nonick
@hook.regex(*("\\bgirl\\b", re.I))
@hook.randreply(0.1)
def girl(inp):
    return gi
