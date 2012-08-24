from contextlib import nested

from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['my_server']

def test():
    with lcd('filmfest'):
        local('python manage.py test')

GIT_REPO = 'git://github.com/nott/filmfest.by.git'

def deploy():
    run('virtualenv --no-site-packages --prompt="(filmfest)" --python=python2.7 app')
    with cd('app'):
        run('git clone %s src' % GIT_REPO)

def update():
    code_dir = '/srv/django/myproject'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")
