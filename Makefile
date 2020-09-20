VERSION:=0.1

CONTAINER_NAME:=django-simple-dbbackup:$(VERSION)

.DEFAULT_GOAL := build

CONTEXT:=default

.PHONY: build
build:
	docker build -t $(CONTAINER_NAME) .

.PHONY: build-no-cache
build-no-cache:
	docker build --no-cache -t $(CONTAINER_NAME) .

.PHONY: save
save:
	docker save $(CONTAINER_NAME) -o ./django-simple-dbbackup-$(VERSION).tar

.PHONY: run
run:
	docker-compose stop
	docker-compose up

.PHONY: up
up: build
	docker-compose up -d

.PHONY: down
down:
	docker-compose down
