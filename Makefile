flake8:
	flake8 .
black:
	black --check .
mypy:
	mypy --strict .
isort:
	isort --check .
lint: flake8 black mypy isort
