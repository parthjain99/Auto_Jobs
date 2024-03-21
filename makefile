# Setup target
setup:
	python3 -m src.setup

# Install target
install:
	# Add install commands here
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt

# New role target
run:
	source venv/bin/activate && python3 -m src.Make_files $(r) $(c)

# Phony targets
.PHONY: setup install run
