from zope import schema
from zope.interface import Interface

import config

class IOpenMeetingsTool(Interface):
    """ OpenMeetings configuration storage
    """
    server = schema.TextLine(title=u"Open meetings server address",
                default=config.SERVER)
    port = schema.Int(title=u"Open meetings server port",
                default=config.PORT)
