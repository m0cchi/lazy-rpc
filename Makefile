VERSION := $(shell python -c 'from lazy_rpc.version import VERSION; print(VERSION)')

packaging: 
	pipenv lock -r -d > requirements-dev.txt
	pipenv lock -r > requirements.txt
	python setup.py sdist

tagging:
	echo "$(VERSION)"

upload: packaging
	twine upload --repository pypi dist/*
