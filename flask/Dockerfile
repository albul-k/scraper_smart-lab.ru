FROM python:3.7.9-slim-stretch

EXPOSE 8080

WORKDIR /usr/src/predict-hosp-days

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]