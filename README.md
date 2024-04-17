# IATI Sphinx Theme

## Development

### Install dependencies
```
pip install -r requirements_dev.txt
```

### Update dependencies
```
python -m piptools compile --extra=dev -o requirements_dev.txt pyproject.toml
```

### Run linting

```
black iati_sphinx_theme
isort iati_sphinx_theme
flake8 iati_sphinx_theme
```
