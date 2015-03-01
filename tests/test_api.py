# coding: utf-8
from os.path import join, basename, abspath, relpath

import pytest

from pinner.api import check_requirement, find_requirements
from pinner.exceptions import *


def test_requirement_needs_version():
    with pytest.raises(UnpinnedDependency):
        check_requirement('Django')
    with pytest.raises(NotStrictSpec):
        check_requirement('pytest>=2.6')
    with pytest.raises(NotStrictSpec):
        check_requirement('requirements-parser<=1')


def test_requirement_needs_revision():
    with pytest.raises(UnpinnedVcs):
        check_requirement('-e git+git://github.com/mitsuhiko/jinja2.git#egg=jinja2')
    with pytest.raises(NotStrictVcs):
        check_requirement('git://git.myproject.org/MyProject.git@master#egg=MyProject')


def test_requirement_has_version():
    assert check_requirement('coveralls==0.5')
    assert check_requirement('-r otherfile.pip'), 'Skipping'


def test_requirement_has_revision():
    assert check_requirement('-e hg+https://bitbucket.org/coagulant/django-autoslug@903a9fd#egg=django-autoslug')
    assert check_requirement('-e svn+http://svn.myproject.org/svn/MyProject/trunk@2019#egg=MyProject')
    assert check_requirement('-e git+https://github.com/mvasilkov/django-google-charts@abcde1#egg=django-google-charts')


def test_find_requirements():
    test_dir = abspath(join(basename(__file__), '..', 'test_project'))
    assert list([relpath(path, test_dir) for path in find_requirements(test_dir)]) == [
        'reqs.txt',
        'requirements-dev.txt',
        'requirements.pip',
        'requirements.txt',
        'requirements/local.txt',
        'requirements/production.pip'
    ]
