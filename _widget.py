"""PytSite Section Plugin Widgets
"""
from plugins import taxonomy as _taxonomy

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class SectionSelect(_taxonomy.widget.TermSelect):
    """Section Select Widget.
    """

    def __init__(self, uid: str, **kwargs):
        """Init.
        """
        kwargs.setdefault('sort_field', 'title')

        super().__init__(uid, model='section', **kwargs)
