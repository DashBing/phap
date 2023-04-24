python := python
make := make
ifeq ($(OS),Windows_NT)
	mv := move
else
	mv := mv
endif

#all:
#	$(make) build
#	$(make) upload

build:
	$(python) -m build

upload:
	$(python) -m twine upload ./dist/*
	$(mv) ./dist/* ./releases

init:
	$(python) -m pip install -U build
	$(python) -m pip install -U twine
