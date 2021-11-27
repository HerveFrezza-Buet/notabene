all :
	find . -name 'example-*.py' -exec python3 \{} \;
	find . -name '*-cheatsheet.tex' -exec latexmk -pdf \{} \;
	mv *.pdf cheat-sheets
	find cheat-sheets -name '*-cheatsheet.pdf' -exec git add \{} \;
	make clean

clean:
	rm -f *.aux *.tex *.log *.fls *.fdb_latexmk *~ *.pdf
