# Operation
## docker
startup container
```
docker-compose up -d --build
```

exec ash in container
```
docker-compose exec flask /bin/ash
# or
docker exec -it flask-container /bin/aash
```

remove container
```
docker-compose down
```

必要なライブラリが増えてきた場合は、
リポジトリに仮想環境ディレクトリを保存してマウントさせるか検討


## flask


## Reference
https://tech.plaid.co.jp/tutorial-for-docker-beginners/
https://qiita.com/shuichiro/items/adaaeccebdc55089f1b8
[Alpine Linuxにnumpy, scipy, scikit-learn, pandasを入れた](https://qiita.com/ricesho/items/e56bf08f51ea406674eb)
[Pandas installation problems with pip version 10](https://github.com/pandas-dev/pandas/issues/20775)
