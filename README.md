# Development

#### Working with venv:

```shell
cd Backend

python -m venv venv # create environment

# activate your environment
venv\Scripts\activate
# or
vnev\bin\activate

pip install -r requirements.txt # install dependencies
```

#### Running flask:
```shell
# inside venv
flask --app server run
```
#### Development server for frontend:
```shell
pnpm dev
```

# Running

Run MySQL instance:

```shell
docker run --name lego-mysql -d `
    -p 3306:3306 `
    -e MYSQL_ROOT_PASSWORD=change-me `
    --restart unless-stopped `
    mysql:8
```

# Resources

Flask-Migrate - https://flask-migrate.readthedocs.io/en/latest/