import os
import sys
import math

def parse_tokens(tokens, stdquif):
    outc = f"#include \"{stdquif}\"\x0a"
    pos = 0
    spaces = 0
    while tokens[pos].type != "EOF":
        ct = tokens[pos]
        if (ct.type == "int"):
            outc += f"{'  '*spaces}stpush({ct.value.acstr()});\x0a"
        elif (ct.type == "keyword"):
            acstr = ct.value.acstr()
            if acstr == "{":
                outc += f"{'  '*(spaces-1)}{'{'}\x0a"
                spaces += 1
            elif acstr == "}":
                outc += f"{'  '*(spaces-1)}{'}'}\x0a"
                spaces -= 1
            elif acstr == "+":
                outc += f"{'  '*spaces}stadd();\x0a"
            elif acstr == "-":
                outc += f"{'  '*spaces}stsub();\x0a"
            elif acstr == "*":
                outc += f"{'  '*spaces}stmul();\x0a"
            elif acstr == "/":
                outc += f"{'  '*spaces}stdiv();\x0a"
            elif acstr == "%":
                outc += f"{'  '*spaces}stmod();\x0a"
            elif acstr == "==":
                outc += f"{'  '*spaces}steq();\x0a"
            elif acstr == "!=":
                outc += f"{'  '*spaces}stneq();\x0a"
            elif acstr == ">":
                outc += f"{'  '*spaces}stgt();\x0a"
            elif acstr == "<":
                outc += f"{'  '*spaces}stlt();\x0a"
            elif acstr == ">=":
                outc += f"{'  '*spaces}stgeq();\x0a"
            elif acstr == "<=":
                outc += f"{'  '*spaces}stleq();\x0a"
            elif acstr == "print":
                outc += f"{'  '*spaces}stprt();\x0a"
            elif acstr == "emit":
                outc += f"{'  '*spaces}stemit();\x0a"
            elif acstr == "input":
                outc += f"{'  '*spaces}stintinput();\x0a"
            elif acstr == "dup":
                outc += f"{'  '*spaces}stdup();\x0a"
            elif acstr == "pop":
                outc += f"{'  '*spaces}stpop();\x0a"
            elif acstr == "swap":
                outc += f"{'  '*spaces}stswap();\x0a"
            elif acstr == "++":
                outc += f"{'  '*spaces}{tokens[pos+1].value.acstr()}++;\x0a"
            elif acstr == "--":
                outc += f"{'  '*spaces}{tokens[pos+1].value.acstr()}--;\x0a"
            elif acstr == "&":
                outc += f"{'  '*spaces}stband();\x0a"
            elif acstr == "|":
                outc += f"{'  '*spaces}stbor();\x0a"
            elif acstr == "^":
                outc += f"{'  '*spaces}stbxor();\x0a"
            elif acstr == "ret":
                outc += f"{'  '*spaces}return stpop();\x0a"
            elif acstr == "exit":
                outc += f"{'  '*spaces}exit(stpop());\x0a"

        elif (ct.value.acstr() == "func"):
            outc += f"\x0aint {tokens[pos+1].value.acstr()}() "
        elif (ct.value.acstr() == "call"):
            outc += f"{'  '*spaces}{tokens[pos+1].value.acstr()}();\x0a"
        elif (ct.value.acstr() == "retcall"):
            outc += f"{'  '*spaces}stpush({tokens[pos+1].value.acstr()}());\x0a"
        elif (ct.value.acstr() == "char"):
            outc += f"{'  '*spaces}char {tokens[pos+1].value.acstr()} = (char)stpop();\x0a"
        elif (ct.value.acstr() == "int"):
            outc += f"{'  '*spaces}int {tokens[pos+1].value.acstr()} = (int) stpop();\x0a"
        elif (ct.value.acstr() == "val"):
            outc += f"{'  '*spaces}stpush({tokens[pos+1].value.acstr()});\x0a"
        elif (ct.value.acstr() == "ptrint"):
            outc += f"{'  '*spaces}long long int* {tokens[pos+1].value.acstr()} = (long long int*) stpop();\x0a"
        elif (ct.value.acstr() == "if"):
            outc += f"{'  '*spaces}if (stpop() != 0) "
        elif (ct.value.acstr() == "else"):
            outc += f"{'  '*spaces}else "
        elif (ct.value.acstr() == "while"):
            outc += f"{'  '*spaces}while (stpop() != 0) "
        elif (ct.value.acstr() == "whilenot"):
            outc += f"{'  '*spaces}while (stpop() == 0) "
        elif (ct.value.acstr() == "repeat"):
            outc += f"{'  '*spaces}for (int i = 0; i < {tokens[pos+1].value.acstr()}; i++) "
            pos += 1

        pos += 1
    return outc
