all :
	find . -name 'example-*.py' -exec python3 \{} \;
	find . -name '*-cheatsheet.tex' -exec latexmk -pdf \{} \;
	mv *.pdf cheat-sheets
	make clean

clean:
	rm -f *.aux *.tex *.log *.fls *.fdb_latexmk *~ *.pdf
