import config
from tool import Tool

def addTool(context, REQUEST=None):
    """ Add OpenMeetings tool from ZMI
    """
    tool = Tool(id=config.ID)
    tool.title = config.TITLE
    context._setObject(config.ID, tool)
    tool = context._getOb(config.ID)
    if REQUEST:
        return context.manage_main(context, REQUEST, update_menu=1)
    return tool.getId()
