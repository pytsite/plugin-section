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

    def _pre_save(self, **kwargs):
        super()._pre_save()

        if self.is_new and self.has_field('order') and not self.f_get('order'):
            e = _taxonomy.find(self.model).eq('_parent', self.parent).sort([('order', _odm.I_DESC)]).first()
            self.f_set('order', ((int(ceil(e.f_get('order') / 10.0)) * 10) + 10) if e else 10)

    def _pre_delete(self, **kwargs):
        super()._pre_delete(**kwargs)

        _events.fire('section@pre_delete', section=self)

    @classmethod
    def odm_ui_browser_widget_class(cls):
        return _widget.misc.TreeTable
