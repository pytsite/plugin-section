"""PytSite Section Plugin API
"""

from typing import Iterable as _Iterable, Optional as _Optional
from plugins import odm as _odm, taxonomy as _taxonomy
from . import _model

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get(language: str = None) -> _Iterable[_model.Section]:
    """Get sections
    """
    return _taxonomy.find('section', language).sort([('order', _odm.I_ASC)]).get()


def dispense(title: str, alias: str = None, language: str = None) -> _model.Section:
    """Get or create section
    """
    return _taxonomy.dispense('section', title, alias, language)  # type: _model.Section


def find_by_title(title: str, language: str = None) -> _Optional[_model.Section]:
    """Find section by title
    """
    return _taxonomy.find_by_title('section', title, language)  # type: _Optional[_model.Section]


def find_by_alias(alias: str, language: str = None) -> _Optional[_model.Section]:
    """Find section by alias
    """
    return _taxonomy.find_by_alias('section', alias, language)  # type: _Optional[_model.Section]
