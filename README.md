# User API

[![Build UserAPI Image](https://github.com/davidogbiko/fastuserapi/actions/workflows/build_image.yaml/badge.svg?branch=main&event=push)](https://github.com/davidogbiko/fastuserapi/actions/workflows/build_image.yaml)

This is a simple API that allows us to create and read user(s) and store their data in the DB.

We can create create or read users through the a single endpoint:

```bash
/users
```

The endpoint supports:

- `GET` method for `/users` to fetch all users in the database.
- `GET` method for `/users/{userID}` to get a single user by ID.
- `POST` method for `/users` to create a single user in the database.
- `POST` method on `/users/upload` to create multiple users from a csv file.

## Local Setup

### Requirements

1. Python 3.10+
2. Docker

## Steps

1. Clone this repository.

    ```bash
    git clone https://github.com/davidogbiko/fastuserapi
    ```

2. Setup a virtual environment by running the command below.

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies.

    ```bash
    cd user_api
    pip install -r requirements-dev.txt
    ```

4. Configure `DATABASE_URL` environment variable. (If not configured, a default sqlite database is used).

    ```bash
    export DATABASE_URL={Your custom DB URL}
    ```

5. Start the application using the following command:

    ```bash
    uvicorn user_api.main:app --port 8080 --reload
    ```

Tests are written in the `test_main.py` file. You can modify these tests as necessary and run them using:

```bash
pytest
```

### Running App in Docker

The provided `Dockerfile` and `docker-compose.yml` files enable seamless local run using docker.
Commands:

```bash
cd user_api
docker compose up
```

Once you are done, press `Ctrl+C` to quit.

To run in the background:

```bash
docker compose up -d
```

When done, run:

```bash
docker compose down
```

### Uploading Data Through CSV

After starting the application ( using docker or uvicorn cli), the application is accessible through:

```bash
http://127.0.0.1:8080
```

This application is written in FastAPI which gives us some extra features including an OpenAPI formatted documentation at:

```bash
http://127.0.0.1:8080/docs
```

We can try out all UserAPI endpoints with sample data here.

You can upload csv using `curl`:

```bash
curl -X 'POST' \
  'http://localhost:8080/users/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@data.csv;type=text/csv'
```

PS: `data.csv` file containing the data you wish to upload to the API.
If you are running `curl` from a directory different from where `data.csv`
is located, ensure you specify the full path as shown in the snippet below.

```bash
curl -X 'POST' \
  'http://localhost:8080/users/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@/Users/david/Documents/data.csv;type=text/csv'
```

## Production Deployment

- The `.github/workflows/deploy.yaml` contains the Github Actions workflow for production deployment.
- The workflow is currently set to be triggered manually.
- To run this workflow, the `DATABASE_URL` and `KUBECONFIG` need to be set in Github Secrets for the project repository.
- Once this is done, trigger the workflow to deploy the application to a kubernetes cluster
