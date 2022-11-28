.PHONY: up
up:
	@docker-compose up --build -d


.PHONY: down
down:
	@docker-compose down 


.PHONY: start
start:
	@poetry run uvicorn app.main:app --reload --ssl-keyfile=./localhost+2-key.pem --ssl-certfile=./localhost+2.pem


.PHONY: autoflake_format
autoflake_format: ## Format project with autoflake
	@poetry run autoflake ./app


.PHONY: isort_format
isort_format: ##Format project with isort
	@poetry run isort ./app


.PHONY: black_format
black_format: ##Format project with black
	@poetry run black ./app


format: autoflake_format isort_format black_format ## Alias to run all formats