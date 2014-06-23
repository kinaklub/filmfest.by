#!/usr/bin/env python
import os.path

from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'requirements')) as f:
    install_requires = [line.strip() for line in f.readlines() if line.strip()]

setup(
    name='filmfest',
    version='1.8.0',
    description='filmfest.by, a Django-based project',
    author='Stas Rudakou',
    author_email='stas@garage22.net',
    url='https://github.com/kinaklub/filmfest.by',
    license='WTFPL',

    platforms=['any'],
    install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,

    packages=find_packages(),
    py_modules=['manage'],
    entry_points = {
        'console_scripts': [
            'filmfest_manage = manage:main',
        ],
    },
)
