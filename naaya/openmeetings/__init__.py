""" Open meetings connecter to Naaya based portals
"""
import zmi
import tool
import config

def initialize(context):
    """ Zope 2
    """
    context.registerClass(
        tool.Tool,
        permission = config.PERMISSION,
        icon='tool.png',
        constructors=(
            zmi.addTool,
        ),
    )
