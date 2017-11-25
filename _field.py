"""PytSite Section Plugin ODM Fields
"""
from plugins import odm as _odm

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Section(_odm.field.Ref):
    def __init__(self, name: str, **kwargs):
        """Init
        """
        kwargs['model'] = 'section'

        super().__init__(name, **kwargs)