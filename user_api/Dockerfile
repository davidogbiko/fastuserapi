FROM python:3.10-slim-bullseye

WORKDIR /userapi

COPY ./requirements-dev.txt  /userapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /userapi/requirements.txt

COPY . /userapi/app

CMD [   "uvicorn", "app.main:app", \
        "--host", "0.0.0.0",\ 
        "--port", "80",\
        "--header", "server:userapi"\ 
    ]
