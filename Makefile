# Exibir comandos disponíveis
default: 
	@echo "Available commands"
	@echo "make build           - Builds the Docker containers"
	@echo "make start           - Starts the application containers"
	@echo "make stop            - Stops the application containers"
	@echo "make restart         - Restarts the application containers"
	@echo "make logs            - Shows the logs of the application container"
	@echo "make shell           - Opens a shell inside the app container"
	@echo "make db-shell        - Opens a PostgreSQL shell inside the database container"

# Construção do ambiente
build:
	docker-compose up --build -d

# Gerenciamento de containers
start:
	docker-compose up -d

stop:
	docker-compose down

restart:
	docker-compose restart

logs:
	docker-compose logs -f app

# Acessar containers
shell:
	docker exec -ti fastapi_weather bash

db-shell:
	docker exec -ti postgres_weather psql -U user -d weather_db

