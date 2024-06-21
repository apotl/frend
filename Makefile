CDK_DOCKER_CMD=docker run -it -v ~/.aws/credentials:/root/.aws/credentials --rm --name frend frend

all: deploy

install:
		pipenv install -d --categories lambda
		pre-commit install

gen-reqs:
		pipenv requirements > requirements.txt
		pipenv requirements --categories lambda > src/requirements-lambda.txt

build: gen-reqs
		docker build -t frend .

init: gen-reqs build
		${CDK_DOCKER_CMD} bootstrap

deploy: gen-reqs build
		${CDK_DOCKER_CMD} deploy --require-approval never

clean:
		pipenv clean
		docker rmi friend
