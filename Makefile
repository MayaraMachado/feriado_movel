run:
	docker-compose up -d

stop:
	docker-compose down

shell:
	docker exec -it verifica_feriado bash

test:
	pytest --cov=api api/tests/ -vv