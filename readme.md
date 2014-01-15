Подготовка окружения:
---------------------

1. поставить sqlite, python2.7 и virtualenvwrapper (в Arch Linux это пакеты sqlite, python2, python-virtualenvwrapper)

2. создать virtualenv

    $ mkvirtualenv --no-site-packages --python=python2.7 filmfest

3. из корневой папки проекта выполнить

    $ python setup.py develop
    $ filmfest_manage syncdb
    $ filmfest_manage migrate

Запуск:
-------

1. из корневой папки проекта выполнить

    $ workon filmfest
    $ filmfest_manage runserver

3. приложение доступно по адресу http://127.0.0.1:8000/


Обновление:
-----------

    $ fab -H user@host:port update
