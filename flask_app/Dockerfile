FROM python:3.7.7-stretch

# WORKDIR 

ADD . .

# Install the dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]