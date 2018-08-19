from glob import glob
import os

HEADER = r"""\documentclass[a4paper,11pt]{standalone}
\usepackage[utf8]{inputenc}
\input{preamble}
\input{tikz/general-setup}
\begin{document}
"""
FOOTER = r"""\end{document}
"""
FIGS_PATH = "*/figs/*.tex"
OUT_DIR = "figs-out"
COMPILE = "pdflatex -output-directory={} ".format(OUT_DIR)

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

for inFilename in glob(FIGS_PATH):
    filename = inFilename.rsplit("/", 1)[1]
    outFilename = OUT_DIR + "/" + filename
    if not os.path.exists(outFilename) or os.path.getmtime(inFilename) > os.path.getmtime(outFilename):
        with open(inFilename, "r") as inF:
            with open(outFilename, "w") as outF:
                outF.write(HEADER)
                outF.write(inF.read())
                outF.write(FOOTER)
        os.system(COMPILE + outFilename)
