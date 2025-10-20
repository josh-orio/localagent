PYTHON := python3
MAIN_SCRIPT := main.py
SRC := . # doesnt include modules yet

.PHONY: all
all: run

.PHONY: run
run:
	@echo "🏃 Running $(MAIN_SCRIPT)..."
	$(PYTHON) $(MAIN_SCRIPT)

.PHONY: lint
lint:
	@echo "🔍 Running lint checks..."
	flake8 $(SRC)
	mypy $(SRC)

.PHONY: format
# is recursive so it gets the module code too
format:
	@echo "🧹 Formatting code..."
	autopep8 --in-place --recursive --aggressive .


.PHONY: install
install:
	@echo "📦 Installing development tools..."
	pip install -r requirements.txt
