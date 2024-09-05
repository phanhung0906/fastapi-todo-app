# FastAPI Todo App
A FastAPI Todo application to learn how to use FastAPI with SQLAlchemy and PostGreSQL.

# Setup 
- Create a virtual environment using `virtualenv` module in python.
```bash
# Install module (globally)
pip install virtualenv

# Generate virtual environment
virtualenv --python=<your-python-runtime-version> venv

# Activate virtual environment
source venv/bin/activate

# Install depdendency packages
pip install -r requirements.txt
```
- Configure `.env` file by creating a copy from `.env.sample`
- Setup a postgres docker container
```bash
docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=<your-preferred-one> -d postgres:13
```
- Create Database name as config in env file in DB_NAME
- At `app` directory, run `alembic` migration command. Please make sure your postgres DB is ready and accessible.
```bash
# Migrate to latest revison
alembic upgrade head
```
- Run `uvicorn` web server from `app` directory (`reload` mode is for development purposes)
```bash
uvicorn main:app --reload
```
# Login Data demo
- Admin: 
  - username:user1
  - password:[DEFAULT_PASSWORD]
- Normal User:
  - username:user2
  - password:[DEFAULT_PASSWORD]