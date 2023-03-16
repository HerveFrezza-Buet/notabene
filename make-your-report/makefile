help:
	@echo
	@echo "You can run the following commands"
	@echo
	@echo "make report          <-- builds up the report (pdf)."
	@echo "make cheat-sheet     <-- builds up the cheat sheet (pdf)."
	@echo "make help            <-- displays this message"
	@echo


report: report.pdf
	@evince report.pdf &

report.pdf: report.tex introduction.tex main.tex conclusion.tex notations.tex
	@pdflatex report
	@bibtex   report
	@pdflatex report
	@pdflatex report

notations.tex: notations.py
	@python3 notations.py

notations-cheatsheet.tex: notations.py
	@python3 notations.py

notations-cheatsheet.pdf: notations-cheatsheet.tex
	@pdflatex notations-cheatsheet.tex
	@pdflatex notations-cheatsheet.tex

cheat-sheet: notations-cheatsheet.pdf
	@evince notations-cheatsheet.pdf &


