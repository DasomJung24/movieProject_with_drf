<h1>movieProject_with_drf</h1>

<h3>virtual env (Mac)</h3>
```
# create
python -m venv .venv

# activate
. .venv/bin/activate

# deactivate
deactivate
```
<br>
<h3>virtual env (Windows)</h3>

```
# create
python -m venv venv

# activate
venv/Scripts/activate

# deactivate
deactivate
```
<br>
<h3>설치</h3>

```
# clone
git clone https://github.com/DasomJung24/movieProject_with_drf.git

# pip upgrade
python -m pip install --upgrade pip

# package install
pip install -r requirements.txt
```
<br>
<h3>my_settings.py 작성</h3>

```
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306',
    }
}

SECRET = {
        'secret': '',
}
```
<br>
<h3>database migration</h3>

```
python manage.py migrate
```
<br>
<h3>commands</h3>

```
# show all route url
python manage.py show_urls

# shell
python manage.py shell_plus

# database make migration all applications
python manage.py makemigrations

# migrate
python manage.py migrate

# create super user
python manage.py superuser
```
<br>
<h3>init Data</h3>

```
# all
sh init.sh

# actors
python manage.py loaddata init/fixtures/actors.yaml

# audience_raitngs
python manage.py loaddata init/fixtures/audience_ratings.yaml

# directors
python manage.py loaddata init/fixtures/directors.yaml

# genres
python manage.py loaddata init/fixtures/genres.yaml

# tags
python manage.py loaddata init/fixtures/tags.yaml

# types
python manage.py loaddata init/fixtures/types.yaml

# cities
python manage.py loaddata init/fixtures/cities.yaml

# theaters
python manage.py loaddata init/fixtures/theaters.yaml
```
<br>
<h3>seeds</h3>

```
# movies
python manage.py movies

# screens
python manage.py screens

# screening
python manage.py screenings
```