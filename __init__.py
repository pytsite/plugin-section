"""PytSite Section Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from . import _model as model, _field as field, _widget as widget
from ._api import dispense, find_by_alias, find_by_title, get
from ._model import Section


def plugin_load():
    from pytsite import lang
    from plugins import taxonomy

    lang.register_package(__name__)
    taxonomy.register_model('section', Section, 'section@sections')
