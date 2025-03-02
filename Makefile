PYTHON = ~/PythonEnvs/myenv/bin/python


vim:
	$(PYTHON) ./src/format_md.py ./markdown/hello.md  -o ./markdown/hello.md -rn
	$(PYTHON) ./src/md2html.py ./markdown/hello.md ./html/ 
	$(PYTHON) ./src/format_html.py ./html/hello.html -o ./html/hello.html ~/hello.html -rp

format_md:
	$(PYTHON) ./src/format_md.py ./markdown/hello.md  -o ./temp.md -rn

format_html:
	$(PYTHON) ./src/format_html.py ./html/hello.html ~/hello.html -rp


ffox:
	firefox ./html/hello.html &

