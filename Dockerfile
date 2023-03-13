FROM python:3.11.2-slim-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 5000
CMD [ "flask", "--app", "./flaskr/app.py", "run", "--host=0.0.0.0"]