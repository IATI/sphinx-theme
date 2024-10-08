MESSAGE_CATALOG_NAME = sphinx

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  extract       to extract translatable strings into POT files"
	@echo "  init          to initialise a PO file for a new language"
	@echo "  update        to update existing PO files"
	@echo "  compile       to compile updated PO files"

.PHONY: extract
extract:
	pybabel extract -o iati_sphinx_theme/locale/$(MESSAGE_CATALOG_NAME).pot -F babel.cfg iati_sphinx_theme

.PHONY: init
init:
	pybabel init -i iati_sphinx_theme/locale/$(MESSAGE_CATALOG_NAME).pot -d iati_sphinx_theme/locale --domain=$(MESSAGE_CATALOG_NAME) -l ${lang}

.PHONY: update
update:
	pybabel update -i iati_sphinx_theme/locale/$(MESSAGE_CATALOG_NAME).pot -d iati_sphinx_theme/locale --domain=${MESSAGE_CATALOG_NAME}

.PHONE: compile
compile:
	pybabel compile --directory=iati_sphinx_theme/locale --domain=${MESSAGE_CATALOG_NAME}
