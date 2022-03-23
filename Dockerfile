FROM python:3.8.13-slim-buster

WORKDIR /new_app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=new_app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]