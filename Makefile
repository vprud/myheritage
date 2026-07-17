APP_NAME = heritage

docker-build:
	docker build --tag $(APP_NAME):latest .

docker-run:
	docker run --env-file .env $(APP_NAME):latest

docker-run-log:
	docker run --env-file .env --log-driver=fluentd $(APP_NAME):latest

docker-push:
	sudo docker image tag $(APP_NAME) cut4cut/$(APP_NAME):1.0
	sudo docker image push cut4cut/$(APP_NAME):1.0

sync:
	uv sync

run:
	uv run python -m $(APP_NAME)

lint:
	uv run ruff check .
	uv run ruff format --check .

fmt:
	uv run ruff check --fix .
	uv run ruff format .

typecheck:
	uv run ty check

test:
	uv run pytest
