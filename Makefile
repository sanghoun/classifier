RM = /bin/rm -f

all:
	rm -f *.*~
	rm -f *.~
	rm -f *.log
	rm -f *.aux
	rm -f *.bbl
	rm -f *.blg
	rm -f *.toc
	rm -f *.dvi
	pdflatex classifier
	bibtex classifier
	pdflatex classifier
	pdflatex classifier
	rm -f *.log
	rm -f *.aux
	rm -f *.bbl
	rm -f *.blg
	rm -f *.toc
	rm -f *.dvi
	rm -f *.back
