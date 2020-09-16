.PHONY: test

SHELL := /bin/bash

all: test

test:
	set -a && set +a && \
	python3 -m pytest -q

run:
	@set -a && set +a && \
	python3 -m tftd

