"""PytSite Section Plugin API
"""

from typing import Iterable as _Iterable, Optional as _Optional
from plugins import odm as _odm, taxonomy as _taxonomy
from . import _model

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def dispense(title: str, alias: str = None, language: str = None, parent: _model.Section = None) -> _model.Section:
    """Create a new tag
    """
    return _taxonomy.dispense('section', title, alias, language, parent)  # type: _model.Section


def get(language: str = None) -> _Iterable[_model.Section]:
    """Get sections
    """
    return _taxonomy.find('section', language).sort([('order', _odm.I_ASC)]).get()


def find_by_title(title: str, language: str = None) -> _Optional[_model.Section]:
    """Find section by title
    """
    return _taxonomy.get('section', title, language)  # type: _Optional[_model.Section]


def find_by_alias(alias: str, language: str = None) -> _Optional[_model.Section]:
    """Find section by alias
    """
    return _taxonomy.get('section', alias=alias, language=language)  # type: _Optional[_model.Section]
