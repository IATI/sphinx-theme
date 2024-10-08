# VARIABLE      = value
MESSAGE_CATALOG_NAME = iati-sphinx-theme

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  extract       to extract translatable strings into POT files"

.PHONY: extract
extract:
	@echo "Extracting messages from theme templates"
	pybabel extract -o iati_sphinx_theme/locale/$(MESSAGE_CATALOG_NAME).pot -F babel.cfg iati_sphinx_theme
	@echo "Extracting messages from docs/conf.py"
	pybabel extract -o docs/locale/${MESSAGE_CATALOG_NAME}.pot -F babel.cfg docs/conf.py
	@echo "Extracting messages from RST files"
	sphinx-build -b gettext docs docs/locale

.PHONY: init
init:
	pybabel init -i iati_sphinx_theme/locale/$(MESSAGE_CATALOG_NAME).pot -d iati_sphinx_theme/locale --domain=$(MESSAGE_CATALOG_NAME) -l ${lang}
	sphinx-intl update -p docs/locale -d docs/locale -l ${lang}

.PHONY: update
update:
	pybabel update -i iati_sphinx_theme/locale/$(MESSAGE_CATALOG_NAME).pot -d iati_sphinx_theme/locale --domain=${MESSAGE_CATALOG_NAME}
	sphinx-intl update -p docs/locale -d docs/locale

.PHONE: compile
compile:
	pybabel compile --directory=iati_sphinx_theme/locale --domain=${MESSAGE_CATALOG_NAME}
