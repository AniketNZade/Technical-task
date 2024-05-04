FROM python:3.8-slim


WORKDIR /app

RUN apt-get update -y \
   && apt-get upgrade -y\


COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
