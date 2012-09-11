Подготовка окружения:
---------------------

1. поставить sqlite, python2.7 и virtualenvwrapper (в Arch Linux это пакеты sqlite, python2, python-virtualenvwrapper)

2. создать virtualenv

    $ mkvirtualenv --no-site-packages --python=python2.7 filmfest

3. из корневой папки проекта выполнить

    $ pip install -r requirements

4. перейти в директорию filmfest проекта и выполнить

    $ python manage.py syncdb
    $ python manage.py migrate

Запуск:
-------

1. перейти в директорию filmfest проекта

2. выполнить

    $ workon filmfest
    $ python manage.py runserver

3. приложение доступно по адресу http://127.0.0.1:8000/
