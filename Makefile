# Slides Makefile
#
# Gerard Marull-Paretas <gmarull@ingeniamc.com>
# Copyright (c) 2016 Ingenia Motion Control

.PHONY: all clean

all:
	latexmk -pdf \
		-pdflatex="pdflatex -shell-escape -interaction=nonstopmode" \
		cffi.tex

clean:
	latexmk -CA
	rm -rf *.bbl *.nav *.snm *.vrb _minted-*
