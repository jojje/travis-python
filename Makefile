.PHONY: test

test: install-reqs
	flake8
	py.test

dist: clean docs
	ls -al
	git tag
	git describe --match '[0-9.]*' --tags HEAD > app/VERSION
	python setup.py bdist_wheel

install-reqs:
	pip install -q -r requirements.txt -r requirements_dev.txt

docs:
	pandoc -f markdown -t rst < README.md  > README.rst

clean:
	find . -type d -name __pycache__ | xargs rm -rf
	find . -type f -name '*.pyc' | xargs rm
	rm -rf build dist *.egg-info .tox README.rst


