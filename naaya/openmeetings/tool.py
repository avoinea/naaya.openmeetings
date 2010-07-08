from zope.interface import implements
from interfaces import IOpenMeetingsTool
from OFS.Folder import Folder

import config

class Tool(Folder):
    """ Open meetings configuration tool
    """
    implements(IOpenMeetingsTool)

    meta_type = config.TYPE
    server = config.SERVER
    port = config.PORT
