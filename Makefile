up:
	docker-compose up
down:
	docker-compose down && docker network prune --force

run:
	docker-compose docker-compose-ci.yaml up
