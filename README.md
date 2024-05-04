## Process of deploying on AWS ECR and testing on lambda 

# Steps to push dockerfile to AWS ECR

1. Build the Docker image
  
   ```bash
   docker build -t <your-image-name> .
   ```
2. Tag the Docker image
  
   ```bash
   docker tag <your-image-name>:latest <your-account-id.dkr.ecr.your-region.ama   zonaws.com/your-repository-name>:latest
   ```

3. Login to AWS ECR

  ```bash
  aws ecr get-login-password --region <your-region> | docker login --username A  WS --password-stdin <your-account-id.dkr.ecr.your-region.amazonaws.com>
  ```

4. Push the Docker image to AWS ECR

  ```bash
  docker push <your-account-id.dkr.ecr.your-region.amazonaws.com/your-repositor  y-name>:latest
  ```


# Steps for testing image on lambda

1. Create Lambda function using the image
  
   ```bash
   aws lambda create-function \
    --function-name <your-function-name> \
    --package-type Image \
    --code ImageUri=<your-ecr-repository-url>:latest \
    --role <your-iam-role-arn> \
    --region <your-region>
      ```

2. For testing the Lambda function
   
   ```bash
   aws lambda invoke --function-name your-function-name --payload '{}' output.p   y
   ```
