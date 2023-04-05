# Running

Run MySQL instance:

```
docker run --name mysql -d `
    -p 3306:3306 `
    -e MYSQL_ROOT_PASSWORD=change-me `
    --restart unless-stopped `
    mysql:8
```