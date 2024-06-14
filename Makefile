up:
	docker compose up -d

down:
	docker compose down

restart: down up

extract:
	docker exec -it bunker-test-airflow-worker-1 /bin/bash -c "airflow tasks test nobel_prize extract_nobel_prize 2024-06-14"

explore:
	@if [ "$(OS)" = "Windows_NT" ]; then \
		start http://localhost:8888/notebooks/notebooks/playground.ipynb; \
	else \
		if [ "$$(uname)" = "Darwin" ]; then \
			open http://localhost:8888/notebooks/notebooks/playground.ipynb; \
		else \
			xdg-open http://localhost:8888/notebooks/notebooks/playground.ipynb; \
		fi \
	fi

.PHONY: up down