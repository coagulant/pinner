======
pinner
======

.. image:: https://img.shields.io/travis/coagulant/pinner.svg
        :target: https://travis-ci.org/coagulant/pinner

.. image:: https://img.shields.io/pypi/v/pinner.svg
        :target: https://pypi.python.org/pypi/pinner

.. image:: https://img.shields.io/badge/licence-BSD-blue.svg

A tiny console script to verify you have pinned all of your python requirements.

`Why you should specify exact version in requirements.txt <http://nvie.com/posts/pin-your-packages/>`_

Example::

  $ cat requirements.txt
  PIL
  coveralls>=1.0a1
  responses==0.3.0
  git+https://github.com/miracle2k/django-assets.git@master#egg=django_assets
  -e git+git://github.com/miracle2k/webassets.git@9956fb86c1c750672324b2c95c9a464a0ef11a4f#egg=webassets
  git+https://github.com/fcurella/django-recommends.git#egg=django_recommends

  $ pinner
  ./requirements.txt:1:1: R001 Dependency PIL not pinned
  ./requirements.txt:2:1: R002 Dependency coveralls should be pinned to exact version
  ./requirements.txt:4:1: R004 VCS dependency django_assets specifies branch/tag, commit expected
  ./requirements.txt:6:1: R003 VCS dependency django_recommends lacks revision specifier
  [4]

You can use it in your commit hook or CI tests
