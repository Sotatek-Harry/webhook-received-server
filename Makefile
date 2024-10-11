run:
	poetry run uvicorn main:app --reload

deps:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

