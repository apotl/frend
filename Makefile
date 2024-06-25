all: build deploy

# Rule for building the code
build: build.sh build.py
		sudo ./build.sh

run-local: build
		docker stop frend || true
		sleep 3
		docker run -d --net=host --name frend --rm frend

init: build
		cd tf && \
		terraform init && \
		terraform import aws_ecr_repository.my_repo frend

# Rule for running the code
deploy: build
		cd tf && \
		terraform taint aws_ecs_task_definition.fargate_task && \
		terraform apply -auto-approve

clean:
		sudo rm -rf venv/
		sudo rm -rf __pycache__/
		docker rm frend

destroy: clean
		cd tf && \
		terraform destroy
		rm -rf tf/.terraform*
		docker stop frend
		docker rmi frend
