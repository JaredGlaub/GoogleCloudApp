install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		pip install --upgrade 'google-cloud-bigquery[bqstorage,pandas]'

test:
	#python -m pytest -vv test_hello.py

format:
	black *.py


lint:
	pylint --disable=R,C main.py

all: install lint test