# -*- coding: utf-8 -*-

import zeam.form.viewlet

from zope.app.wsgi.testlayer import BrowserLayer
from zope.configuration.config import ConfigurationMachine
from grokcore.component import zcml

FunctionalLayer = BrowserLayer(zeam.form.viewlet)


def grok(module_name):
    config = ConfigurationMachine()
    zcml.do_grok(module_name, config)
    config.execute_actions()

