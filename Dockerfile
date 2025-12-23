# base image
FROM python:3.12
# set info
LABEL version="2.0"
LABEL description="This is the datarobot Ml model  docker image"
LABEL maintainer="Rajendra"
LABEL email="rajendra@gmail.com"
LABEL company="atai.ai"

# create default ENV
ENV HOME /backend

# Create group and user
RUN groupadd -r appgroup && \
    useradd -r -g appgroup -d /home/appuser -m appuser

# Create dir
WORKDIR $HOME

# Change ownership of app directory
RUN chown -R appuser:appgroup $HOME

# copy files into image
COPY . .

# pipenv package install
RUN pip install pipenv 

# dependices installation
RUN pipenv install 

# Switch to non-root user
USER appuser

# default commands to run 
CMD ["pipenv", "run", "python", "run_server.py"]


