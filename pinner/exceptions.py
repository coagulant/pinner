# coding: utf-8

__all__ = ['PinnerWarning', 'UnpinnedDependency', 'NotStrictSpec', 'UnpinnedVcs', 'NotStrictVcs']


class PinnerWarning(Exception):
    template = ''

    def __init__(self, requirement):
        self.requirement = requirement
        super(PinnerWarning, self).__init__(requirement)

    @property
    def text(self):
        return self.template.format(requirement=self.requirement)


class UnpinnedDependency(PinnerWarning):
    template = 'R001 Dependency {requirement.name} not pinned'


class NotStrictSpec(PinnerWarning):
    template = 'R002 Dependency {requirement.name} should be pinned to exact version'


class UnpinnedVcs(PinnerWarning):
    template = 'R003 VCS dependency {requirement.name} lacks revision specifier'


class NotStrictVcs(PinnerWarning):
    template = 'R004 VCS dependency {requirement.name} specifies branch/tag, commit expected'
