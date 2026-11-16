# keywoo

![Deploy Site](https://github.com/ymmmtym/keywoo/workflows/Deploy%20Site/badge.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/482c4bf8af724892b725d6308eb6d64d)](https://www.codacy.com/manual/ymmmtym/keywoo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ymmmtym/keywoo&amp;utm_campaign=Badge_Grade) [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ymmmtym/keywoo)

![keywoo](./keywoo/static/keywoo_top.png)

## Site

Access to <https://keywoo.yumenomatayume.net>

## Requirements

- [uv](https://docs.astral.sh/uv/) >= 0.4.27

## Setup

`uv` manages the Python interpreter, virtual environment, and dependencies.
The project supports Python 3.11, matching the pinned dependencies and Docker runtime.

Install the Linux native-build prerequisites before syncing. On Debian or Ubuntu:

```bash
sudo apt-get update
sudo apt-get install -y build-essential libpq-dev
```

These provide the compiler and PostgreSQL headers/`pg_config` needed to build
psycopg2 and uWSGI from source. Other Linux distributions need equivalent packages.

```bash
git clone git@github.com:ymmmtym/keywoo.git
cd keywoo
uv sync
```

`uv sync` creates `.venv` and installs the dependencies pinned in `uv.lock`.

## Test

```bash
uv run pytest
```

## Run (local)

Provision a PostgreSQL server reachable from your host. For example, on Debian or
Ubuntu, install and start PostgreSQL, then create a local role and database:

```bash
sudo apt-get install -y postgresql
sudo service postgresql start
sudo -u postgres createuser --pwprompt keywoo
sudo -u postgres createdb --owner=keywoo keywoo
```

Choose a password when prompted. Before running the app, edit
`SQLALCHEMY_DATABASE_URI` in `keywoo/config.py` to use that password and your
server's host and port, for example:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://keywoo:YOUR_URL_ENCODED_PASSWORD@127.0.0.1:5432/keywoo"
```

URL-encode special characters in the password. The default `db:5432` address is
for the Compose network; it generally cannot be resolved by an app running on
the host. Keep local credentials out of commits. The role must own the database
so it can create tables.

Create the tables before starting the Flask server:

```bash
uv run python manage.py init_db
uv run python run.py
```

Access to <http://localhost:5000>

## Installation(demo)

```bash
git clone git@github.com:ymmmtym/keywoo.git
docker-compose up -d --build
```

Access to <http://localhost:5000>

## License

**keywoo** is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

**keywoo** is not confidential.

## Reference

[Docker+flaskで「URL Opener」的なものを作った](https://qiita.com/ymmmtym/items/eba907b818f0cc70856d)
