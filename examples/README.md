# Examples

We provide you with examples of the notabene features. Examples are python files. Executing an example requires that you have installed notabene beforehand.

For running example `example-001-001-basics.py`, you only have to execute it.

~~~{.console}
python example-001-001-basics.py
~~~

It generates a `001-001-basic.tex` file, where all your cammands are defined. This is aimed to be "input" in your tex file.

Running the example generates a `001-001-basics-cheatsheet.tex`, that actually inputs `001-001-basic.tex`. This file is ready to be processed by latex (run twice)


~~~{.console}
pdflatex 001-001-basics-cheatsheet.tex
pdflatex 001-001-basics-cheatsheet.tex
~~~

Then you get a pdf. All the generated pdfs are available in the `cheat-sheets` directory.

