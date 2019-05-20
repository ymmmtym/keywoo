# Operation
#### コンテナの起動

`$ docker-compose up -d --build`

#### コンテナ内でbashを実行

`$ docker exec -it work_container bash`

#### コンテナ削除

`$ docker-compose down`

必要なライブラリが増えてきた場合は、
リポジトリに仮想環境ディレクトリを保存してマウントさせるか検討


### Reference
https://tech.plaid.co.jp/tutorial-for-docker-beginners/
