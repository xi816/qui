import sys

from os import path, system
from lex import lex_file
from parselexed import parse_tokens

cfile = path.dirname(__file__)

def rfile(filename):
    with open(filename, "r") as file:
        return file.read()

argv = sys.argv[1:]
if argv[0] in ["-c", "--compile", "-C", "--full-compile"]:
    infile, outfile = argv[1:3]
    if (infile.split(".")[-1] != "qui") or (outfile.split(".")[-1] != "c"):
        raise TypeError("Invalid file types")

sqfile = ""
if argv[3].startswith("--std="):
    sqfile = argv[3][6:]

contents = rfile(f"{cfile}/{infile}")
tokens = lex_file(contents)
with open(f"{cfile}/{outfile}", "w") as out:
    out.write(parse_tokens(tokens, sqfile))

if argv[0] in ["-C", "--full-compile"]:
    system(f"gcc {outfile} -o {'.'.join(outfile.split('.')[:-1])}")
    system(f"./{'.'.join(outfile.split('.')[:-1])}")
