from dnfpluginscore import logger
import dnf
import dnf.transaction
import dnf.package
import os, re
from os.path import *

class ReleaseMods(dnf.Plugin):

    name = 'releasemods'
    _is_repos_file = re.compile('^/etc/yum.repos.d/.*\.repo$')

    def __init__(self, base, cli):
        super(ReleaseMods, self).__init__(base, cli)
        self.base = base
        self.logger = logger
        self.release_packages = []

    def config(self):
        self.conf = self.read_config(self.base.conf)
        if self.conf.has_section('main'):
            if self.conf.has_option('main', 'release_packages'):
                self.release_packages = self.conf.get('main', 'release_packages').split(' ')

    def transaction(self):
        if len(self.release_packages) > 0:
            for item in self.base.transaction.install_set:
                if item.name in self.release_packages:
                    self.logger.debug('  %s: found %s %s' % (self.name, item.name, item.evr))
                    for f in item.files:
                        if self._is_repos_file.match(f):
                            if isfile(f):
                                self.logger.debug('  %s: removing file %s' % (self.name, f))
                                os.remove(f)
                    if self.conf.has_option(item.name, 'files'):
                        for f in self.conf.get(item.name, 'files').split(' '):
                            if isfile(f):
                                self.logger.debug('  %s: removing file %s' % (self.name, f))
                                os.remove(f)
