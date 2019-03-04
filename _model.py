"""PytSite Section Plugin Models
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import events as _events
from plugins import taxonomy as _taxonomy, widget as _widget


class Section(_taxonomy.model.Term):
    """Section Model
    """

    def _setup_fields(self):
        super()._setup_fields()

        self.remove_field('weight')

    def _on_pre_delete(self, **kwargs):
        super()._on_pre_delete(**kwargs)

        _events.fire('section@pre_delete', section=self)

    @classmethod
    def odm_ui_browser_widget_class(cls):
        return _widget.misc.TreeTable
