devtools:
	@echo "Installing Devtools \n"
	pip install -r requirements.txt

run:
	@echo "Running the Proxy Miner! \n"
	python3 proxy_miner/__main__.py


lint:
	@echo "Formatting the Code via Black! \n"
	black .
	@echo "Linting the Code via Pylint! \n"
	pylint proxy_miner/