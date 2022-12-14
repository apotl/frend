
resource "aws_iam_role" "ecs_execution_role" {
  name = "ecs_execution_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_policy" "ecs_execution_policy" {
  name = "ecs_execution_policy"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:BatchCheckLayerAvailability",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "logs:CreateLogStream",
        "logs:CreateLogGroup",
        "logs:PutLogEvents",
        "kms:Decrypt",
        "ssm:GetParameters",
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "*"
    }
  ]
}
EOF
}

resource "aws_iam_policy_attachment" "ecs_execution_attachment" {
  name = "ecs_execution_attachment"
  policy_arn = aws_iam_policy.ecs_execution_policy.arn
  roles = [aws_iam_role.ecs_execution_role.name]
}
