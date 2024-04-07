check:
	@echo Checking code 🧐
	.venv/bin/ruff check

fix:
	@echo Fixing code 🧹
	.venv/bin/ruff check --fix

format:
	@echo Formatting code 🧹
	.venv/bin/ruff format

tests:
	@echo Running tests 🧪
	pytest

coverage:
	@echo Running tests with coverage 🧪
	coverage run -m pytest
	coverage html


migrations:
	@echo Creating migrations 🛠️
	python manage.py makemigrations

migrate:
	@echo Migrating database 🛠️
	python manage.py migrate

build:
	@echo Building image 🏗️
	docker build . -t macwdo/brotherhoods-app

run:
	@echo Running containers 🚀
	docker compose down
	docker compose up

up:
	@echo Starting containers 🚀
	docker compose down
	docker compose up -d

down:
	@echo Stopping containers 🛑
	docker compose down

load_data:
	@echo Loading data 📦
	python manage.py loaddata */fixtures/**/*.json
