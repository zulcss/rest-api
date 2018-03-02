build:
	docker build -t rest-api .
run:
	docker run -d -p 5000:5000 rest-api
