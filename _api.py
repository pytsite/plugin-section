"""PytSite Section Plugin API
"""

from typing import Iterable as _Iterable, Optional as _Optional
from pytsite import odm as _odm
from plugins import taxonomy as _taxonomy
from . import _model

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get(language: str = None) -> _Iterable[_model.Section]:
    """Get sections.
    """
    return _taxonomy.find('section', language).sort([('order', _odm.I_ASC)]).get()


def dispense(title: str, alias: str = None, language: str = None) -> _model.Section:
    """Get or create section.
    """
    term = _taxonomy.dispense('section', title, alias, language)  # type: _model.Section

    return term


def find_by_title(title: str, language: str = None) -> _Optional[_model.Section]:
    """Get section by title.
    """
    term = _taxonomy.find_by_title('section', title, language)  # type: _Optional[_model.Section]

    return term


def find_by_alias(alias: str, language: str = None) -> _Optional[_model.Section]:
    """Get section by title.
    """
    term = _taxonomy.find_by_alias('section', alias, language)  # type: _Optional[_model.Section]

    return term
