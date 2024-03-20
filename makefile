# Clean target
clean:
	# Add clean commands here

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
	source venv/bin/activate && python3 -m src.Make_files $(role) $(Company)

# Phony targets
.PHONY: all build clean setup install new-role