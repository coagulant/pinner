# coding: utf-8
import codecs
import glob
from itertools import chain
import re
from os.path import join

import requirements
from requirements.requirement import Requirement

from .exceptions import *


SHA1 = re.compile('[a-f0-9]{6,40}')


def is_commit(vcs, revision):
    if vcs in ['git', 'hg']:
        if not SHA1.match(revision):
            return False
    return True


def find_requirements(base_dir):
    possible_patterns = ('*requirements*.txt',
                         'requirements.pip',
                         'reqs.txt',
                         'requirements/*.txt',
                         'requirements/*.pip')
    files = []
    for pattern in chain(map(glob.iglob, [join(base_dir, pattern) for pattern in possible_patterns])):
        for file in pattern:
            files.append(file)
    return sorted(files)


def check_requirement(req):
    if not isinstance(req, Requirement):
        requirement = next(requirements.parse(req), None)
    else:
        requirement = req

    if not requirement:  # skip string
        return True

    if requirement.vcs:
        if not requirement.revision:
            raise UnpinnedVcs(requirement)
        elif not is_commit(requirement.vcs, requirement.revision):
            raise NotStrictVcs(requirement)
    elif requirement.specs:
        if requirement.specs[0][0] != '==':
            raise NotStrictSpec(requirement)
    else:
        raise UnpinnedDependency(requirement)

    return True


def process_file(path, emit_warning):
    warnings = []
    with codecs.open(path, 'r') as f:
        for i, line in enumerate(f, start=1):
            req = next(requirements.parse(line), None)
            if not req:
                continue
            try:
                check_requirement(req)
            except PinnerWarning as e:
                warnings.append(emit_warning(path, i, e))
    return warnings
