Process Of deploying on AWS ECR

# Steps to push dockerfile to AWS ECR
1)Build the Docker image
  docker build -t <your-image-name> .

2)Tag the Docker image
  docker tag <your-image-name>:latest <your-account-id.dkr.ecr.your-region.amazonaws.com/your-repository-name>:latest

3)Login to AWS ECR
  aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id.dkr.ecr.your-region.amazonaws.com>

4)Push the Docker image to AWS ECR
  docker push <your-account-id.dkr.ecr.your-region.amazonaws.com/your-repository-name>:latest


# Steps for testing image on lambda
1)Create Lambda function using the image
  aws lambda create-function \
    --function-name <your-function-name> \
    --package-type Image \
    --code ImageUri=<your-ecr-repository-url>:latest \
    --role <your-iam-role-arn> \
    --region <your-region>

2) for Testing the Lambda function
   aws lambda invoke --function-name your-function-name --payload '{}' output.py
