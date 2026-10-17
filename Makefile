# SignalGEO local development. Everything here runs offline: no external provider calls.

BACKEND_DIR := backend
FRONTEND_DIR := frontend
VENV := $(BACKEND_DIR)/.venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

.PHONY: help install install-backend install-frontend test lint typecheck format migrate \
        revision bootstrap dev-backend dev-frontend dev up down logs clean

help:
	@echo "SignalGEO — M1 targets"
	@echo "  make install        create backend venv + install python & node deps"
	@echo "  make test           run backend tests (SQLite; postgres tests skip)"
	@echo "  make lint           ruff check + format --check"
	@echo "  make typecheck      mypy --strict + tsc --noEmit"
	@echo "  make migrate        alembic upgrade head"
	@echo "  make bootstrap      create a workspace and print its key ONCE"
	@echo "  make dev-backend    uvicorn on 0.0.0.0:8000 (SQLite by default)"
	@echo "  make dev-frontend   next dev on 0.0.0.0:3000"
	@echo "  make up             docker compose up --build (PostgreSQL + API + web)"
	@echo "  make down           docker compose down (keeps the pgdata volume)"

install: install-backend install-frontend

install-backend:
	cd $(BACKEND_DIR) && python3 -m venv .venv && $(PIP) install --upgrade pip && $(PIP) install -r requirements-dev.txt

install-frontend:
	cd $(FRONTEND_DIR) && npm install --no-audit --no-fund

test:
	cd $(BACKEND_DIR) && $(PY) -m pytest -q

lint:
	cd $(BACKEND_DIR) && $(PY) -m ruff check . && $(PY) -m ruff format --check .

format:
	cd $(BACKEND_DIR) && $(PY) -m ruff format . && $(PY) -m ruff check . --fix

typecheck:
	cd $(BACKEND_DIR) && $(PY) -m mypy
	cd $(FRONTEND_DIR) && npx --no-install tsc --noEmit

migrate:
	cd $(BACKEND_DIR) && $(PY) -m alembic upgrade head

revision:
	cd $(BACKEND_DIR) && $(PY) -m alembic revision --autogenerate -m "$(m)"

# Usage: make bootstrap NAME="Acme Analytics"
bootstrap:
	cd $(BACKEND_DIR) && $(PY) -m scripts.bootstrap_workspace "$(or $(NAME),Demo Workspace)"

dev-backend:
	cd $(BACKEND_DIR) && $(PY) -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev-frontend:
	cd $(FRONTEND_DIR) && npm run dev

dev:
	@echo "Run 'make dev-backend' and 'make dev-frontend' in two terminals (or 'make up' for Docker)."

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f --tail=100

clean:
	rm -rf $(BACKEND_DIR)/.venv $(BACKEND_DIR)/.pytest_cache $(BACKEND_DIR)/.mypy_cache $(BACKEND_DIR)/.ruff_cache
	rm -rf $(FRONTEND_DIR)/node_modules $(FRONTEND_DIR)/.next
