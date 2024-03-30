check:
	.venv/bin/ruff check

fix:
	.venv/bin/ruff check --fix

format:
	.venv/bin/ruff format

tests:
	pytest

coverage:
	coverage run -m pytest
	coverage html


migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

build:
	docker build . -t macwdo/brotherhoods-app

run:
	docker compose down
	docker compose up

up:
	docker compose down
	docker compose up -d

down:
	docker compose down