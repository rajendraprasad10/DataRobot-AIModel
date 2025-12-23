FROM python:3.12-alpine

LABEL version="2.0"
LABEL description="This is the datarobot Ml model  docker image"
LABEL maintainer="Rajendra"
LABEL email="rajendra@gmail.com"
LABEL company="atai.ai"


ENV HOME /backend

WORKDIR $HOME

COPY . .

RUN pip install pipenv 

RUN pipenv install 


CMD ["pipenv", "run", "python", "run_server.py"]


