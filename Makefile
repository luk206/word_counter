# Application name
APP_NAME = word_counter

# Command to create the virtual environment
VENV_CREATE = python3 -m venv venv

# Command to activate the virtual environment
VENV_ACTIVATE = source venv/bin/activate

# Command to install dependencies
INSTALL_DEPS = pip3 install -r requirements.txt

# Command to run the application
RUN_APP = python3 ${APP_NAME}.py

# Command to test the application
TEST_APP = python3 -m unittest ${APP_NAME}_test.py

CODE_STANDARDS = flake8 --ignore=E501 *.py && pylint --disable=import-error *.py

# Rule to create virtual environment
venv:
	$(VENV_CREATE)

# Default rule
all: deps format test run-locally

# Rule to install dependencies
deps:
	$(VENV_ACTIVATE) && $(INSTALL_DEPS)

# Rule to run the application
run-locally:
	$(VENV_ACTIVATE) && $(RUN_APP) textfile.txt

format:
	$(CODE_STANDARDS)

# Tests
test:
	$(VENV_ACTIVATE) && $(TEST_APP)

# Rule to clean the directory
clean:
	rm -rf venv __pycache__

# Rule to remove the virtual environment
venv-clean:
	rm -rf venv

.PHONY: all venv deps run clean venv-clean
