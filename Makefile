run:
	uvicorn app.main:app --reload

test:
	pytest

lint:
	flake8 app tests

