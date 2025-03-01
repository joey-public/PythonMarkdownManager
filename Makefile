PYTHON = ~/PythonEnvs/myenv/bin/python


vim:
	$(PYTHON) ./src/md2html.py ./markdown/hello.md ./html/ 

format_md:
	$(PYTHON) ./src/format_md.py ./markdown/hello.md  -o ./temp.md -rn_e

ffox:
	firefox ./html/hello.html &

