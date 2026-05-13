.PHONY: help install dev test eval lint clean

help:
	@echo "Comandos disponibles:"
	@echo "  make install   instala dependencias (uv sync o pip)"
	@echo "  make dev       corre tu pipeline en modo desarrollo (definilo vos)"
	@echo "  make test      corre pytest"
	@echo "  make eval      corre eval/eval.py contra dataset held_out"
	@echo "  make lint      corre ruff check"
	@echo "  make clean     borra caches y artefactos temporales"

install:
	@command -v uv >/dev/null 2>&1 && uv sync || pip install -e ".[dev]"

dev:
	@echo "Definí tu propio comando dev en este Makefile cuando arranques tu pipeline."
	@echo "Sugerido: python -m tu_paquete.main"

test:
	pytest -v

eval:
	python eval/eval.py

lint:
	ruff check .

clean:
	rm -rf __pycache__ .pytest_cache .ruff_cache *.egg-info dist build .venv
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
