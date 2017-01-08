"""PytSite Section Plugin.
"""
# Public API
from ._api import dispense, find_by_alias, find_by_title, get
from . import _model as model, _widget as widget

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang
    from plugins import taxonomy

    lang.register_package(__name__, alias='section')
    taxonomy.register_model('section', model.Section, 'section@sections')


_init()
