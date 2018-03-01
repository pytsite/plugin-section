"""PytSite Section Plugin Models
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from math import ceil
from pytsite import events as _events
from plugins import odm as _odm, taxonomy as _taxonomy, widget as _widget


class Section(_taxonomy.model.Term):
    """Section Model
    """

    def _setup_fields(self):
        super()._setup_fields()

        self.remove_field('weight')

    def _pre_delete(self, **kwargs):
        super()._pre_delete(**kwargs)

        _events.fire('section@pre_delete', section=self)

    @classmethod
    def odm_ui_browser_widget_class(cls):
        return _widget.misc.TreeTable
