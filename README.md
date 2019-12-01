# keywoo
[![CircleCI](https://circleci.com/gh/ymmmtym/keywoo.svg?style=svg)](https://circleci.com/gh/ymmmtym/keywoo)

## Operation
### docker
#### startup container
```
docker-compose up -d
```

#### exec bash in container
```
docker-compose exec keywoo /bin/bash
#or
docker exec -it keywoo /bin/bash
```

#### remove container
```
docker-compose down
```

### app
launch debug mode
```
export FLASK_APP=run.py
export FLASK_DEBUG=1
flask run -h 0.0.0.0 -p ${PORT}
```
