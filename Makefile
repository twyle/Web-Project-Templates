update:
	@pip install --upgrade pip

install:
	@pip install -r services/app/requirements.txt

create-db:
	@python services/app/manage.py create_db

seed-db:
	@python services/app/manage.py seed_db

build:
	@docker build -f services/app/Dockerfile -t web-template:latest ./services/app

tag:
	@docker tag web-template:latest lyleokoth/web-template:latest

push:
	@docker login
	@docker push lyleokoth/web-template:latest

run-dev:
	@docker run -p5000:5000 --env-file=./.env web-template:latest

run-app:
	@docker-compose up --build

run-logger:
	@docker-compose -f services/logging/docker-compose.yml up --build