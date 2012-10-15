all: help

help:
	@echo "Available Targets:"
	@cat Makefile | egrep '^(\w+?):' | sed 's/:\(.*\)//g' | sed 's/^/- /g'

install_linux: install_node_in_linux install_jshint install_csslint

install_mac: install_node_in_mac install_jshint install_csslint

install_node_in_linux:
	@apt-get install python-software-properties
	@apt-add-repository ppa:chris-lea/node.js
	@apt-get update
	@apt-get install nodejs npm -y

install_node_in_mac:
	@brew upgrade $(node)
	@curl http://npmjs.org/install.sh | sh

install_jshint:
	@npm install jshint -g

install_csslint:
	@npm install csslint -g

test:
	@python code_quality_tools/tests/test_code_quality_tools.py
