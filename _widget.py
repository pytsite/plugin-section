"""PytSite Section Plugin Widgets
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import taxonomy as _taxonomy


class SectionSelect(_taxonomy.widget.TermSelect):
    """Section Select Widget.
    """

    def __init__(self, uid: str, **kwargs):
        """Init.
        """
        kwargs.setdefault('sort_field', 'title')

        super().__init__(uid, model='section', **kwargs)
