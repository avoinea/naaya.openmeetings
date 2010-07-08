from Products.Five.browser import BrowserView
from naaya.openmeetings import config

class Meetings(BrowserView):
    """ Meetings
    """

    def href(self):
        tool = getattr(self.context, config.ID, None)
        if not tool:
            return ''

        server = getattr(tool, 'server', '')
        if not server:
            return ''

        port = getattr(tool, 'port', '')
        if port:
            server = '%s:%s' % (server, port)

        return '/'.join((server, 'openmeetings/'))
