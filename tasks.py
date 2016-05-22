from invoke import run, task
from invoke.util import cd
import sys


@task
def mkdir(path):
    if sys.platform == 'win32':
        run('mkdir %s' % path)
    elif sys.platform == 'unix':
        run('mkdir -p %s' % path)


@task
def create_test_app():
    """Create a test app structure

    :return:
    """
    mkdir(path='tests')
    with cd('tests'):
        run('django-admin.exe startproject config .')


@task
def clean(docs=False, bytecode=False, extra=''):
    patterns = ['build']
    if docs:
        patterns.append('docs/_build')
    if bytecode:
        patterns.append('**/*.pyc')
    if extra:
        patterns.append(extra)
    for pattern in patterns:
        run("rm -rf %s" % pattern)


@task
def build(docs=False):
    run("python setup.py build")
    if docs:
        run("sphinx-build docs docs/_build")
