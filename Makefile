FRENDCONFIG=config.yml

all: build deploy

# Rule for building the code
build: build.sh main.py
		./build.sh "${FRENDCONFIG}"

init: build
		cd tf && \
		terraform init && \
		terraform import module.fargate.module.ecr.aws_ecr_repository.ecr_repository frendstaging

# Rule for running the code
deploy: build
#terraform taint aws_ecs_task_definition.fargate_task
		cd tf && \
		terraform apply -auto-approve

clean:
		sudo rm -rf venv/
		sudo rm -rf __pycache__/

destroy: clean
		cd tf && \
		terraform destroy
		rm -rf tf/.terraform*

tfplan:
		cd tf && \
		terraform plan