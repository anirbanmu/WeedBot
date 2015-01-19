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


@hook.regex(*("cum", re.I))
def cum(bot):
    bot.reply(cs)


@hook.regex(*("mitten", re.I))
def mitten(bot):
    bot.reply(ms)


@hook.regex(*("crap", re.I))
def crap(bot):
    bot.reply(cp)


@hook.regex(*("ass", re.I))
def ass(bot):
    bot.reply(cp)


@hook.regex(*("\\bftw\\b", re.I))
def ftw(bot):
    bot.reply(ft)


@hook.regex(*("\\bown(s|ed)?\\b", re.I))
def owns(bot):
    ons = "owns " * random.randint(1, 3) + "OWNS " * random.randint(1, 3) + "o-(' 'Q)"
    bot.reply(ons)


@hook.regex(*("\\bapple\\b", re.I))
def apple(bot):
    bot.reply(ap)


@hook.regex(*("weedbot", re.I))
def weedbotname(bot):
    bot.reply(random.choice([":D", "hi!", "weed", "gotta love me!", "guess who has a boner", "weeeeeeed", "weeeeeeeeeeeeeeeeed"]))


@hook.regex(*("\\bdad\\b", re.I))
def dad(bot):
    bot.reply(da)


@hook.regex(*("\\b(mad|angry)\\b", re.I))
def mad(bot):
    bot.reply(ta)


@hook.regex(*("\\bgirl\\b", re.I))
def girl(bot):
    bot.reply(gi)
