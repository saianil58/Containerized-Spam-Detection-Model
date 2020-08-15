FROM tiangolo/uwsgi-nginx-flask:python3.6

# Creating a working path in the OS
WORKDIR /app/

# copying the file from local to container
COPY requirements.txt /app/

# adding the data file from local to container
ADD spam.csv /data/

# installing all the requirements
RUN pip install -r ./requirements.txt

# set the environment as production
ENV ENVIRONMENT production

# copy the server code into new file on container
COPY main.py __init__.py /app/
