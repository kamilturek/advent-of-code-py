flake8:
	flake8 .
black:
	black --check --target-version py310 .
mypy:
	mypy --strict .
isort:
	isort --check .
lint: flake8 black isort
