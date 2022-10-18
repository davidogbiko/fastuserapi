# User API

This is a simple API that allows us to create and read user(s) and store their data in the DB.

We can create create or read users through the a single endpoint:

```shell
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
2. Setup a virtual environment by running the command below.
3. Install dependencies.
4. Configure `DATABASE_URL` environment variable. (If not configured, a default sqlite database is used)

### Commands To Run

```shell
git clone https://github.com/davidogbiko/fastuserapi
python -m venv venv
pip install -r requirements-dev.txt
export DATABASE_URL={Your custom DB URL}
uvicorn user_api.main:app --port 8080 --reload
```

Tests are written in the `test_main.py` file. You can modify these tests as necessary and run them using: `pytest`

### Running App in Docker

The provided `Dockerfile` and `docker-compose.yml` files enable seamless local run using docker.
Commands:

```shell
docker compose up
```

Once you are done, press `Ctrl+C` to quit.
To run in the background:

```shell
docker compose up -d
```

When done, run:

```shell
docker compose down
```
