build:
	docker-compose build --force-rm --no-cache --pull

up:
	docker-compose up -d

down:
	docker-compose down -v
