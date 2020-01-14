
VERSION := $(shell python -c 'from lazy_rpc.version import VERSION; print(VERSION)')

export LANG=C

clean:
	rm -rf dist

output-requirements:
	pipenv lock -r -d > requirements-dev.txt
	pipenv lock -r > requirements.txt

packaging: output-requirements
	python setup.py sdist

tagging: output-requirements
	# check git status
	bash -c "git status | grep 'modified:' | wc -w | xargs test 0 -eq"

	git tag -a "v$(VERSION)" -m 'release-v$(VERSION)'

upload: packaging
	twine upload --repository pypi dist/*

release: clean packaging tagging upload

test-release: clean packaging
	twine upload --repository testpypi dist/*
