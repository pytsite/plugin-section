"""PytSite Section Plugin ODM Fields
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import odm as _odm


class Section(_odm.field.Ref):
    def __init__(self, name: str, **kwargs):
        """Init
        """
        kwargs['model'] = 'section'

        super().__init__(name, **kwargs)
