all: build deploy

# Rule for building the code
build: build.sh build.py
		sudo ./build.sh

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

destroy: clean
		cd tf && \
		terraform destroy
		rm -rf tf/.terraform*