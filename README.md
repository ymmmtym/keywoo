# keywoo
## Operation
### docker
#### startup container
```
docker-compose up -d --build
```

#### exec bash in container
```
docker-compose exec flask /bin/bash
```
or
```
docker exec -it flask-container /bin/bash
```

#### remove container
```
docker-compose down
```


### flask
