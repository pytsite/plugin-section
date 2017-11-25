"""PytSite Section Plugin Models
"""
from pytsite import events as _events
from plugins import taxonomy as _taxonomy

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Section(_taxonomy.model.Term):
    """Section Model
    """

    def _pre_delete(self, **kwargs):
        super()._pre_delete(**kwargs)

        _events.fire('section.pre_delete', section=self)
