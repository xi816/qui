import math
import random

from tokentypes import Token, String
from kws import keywords

def lex_file(ctoks):
    buf = [String(), String(), String()]
    ftokens = []
    commode = False
    c = ""

    for line in ctoks.split("\x0a"):
        c += line + " \x0a"

    for line in c.split("\x0a"):
        for tk in line + "\x0a":
            if commode and tk != "\x0a":
                continue
            if commode and tk == "\x0a":
                commode = False
                continue
            if tk == "#":
                commode = True
                continue

            if tk in "0123456789":
                buf[1].add(tk)
                continue
            elif tk in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-{}<>()[]!~=+-*/%&|_":
                buf[0].add(tk)
                continue
            elif (tk == " ") and (buf[1].cont):
                ftokens.append(Token("int", buf[1]))
                buf[1] = String()
            elif (tk == " ") and (buf[0].cont):
                if "".join(buf[0].cont) in keywords:
                    ftokens.append(Token("keyword", buf[0]))
                else:
                    ftokens.append(Token("var", buf[0]))
                buf[0] = String()

    ftokens.append(Token("EOF"))
    return ftokens
