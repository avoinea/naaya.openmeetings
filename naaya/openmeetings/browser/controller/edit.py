from zope.formlib.form import Fields
from Products.Five.formlib.formbase import SubPageEditForm
from naaya.openmeetings.interfaces import IOpenMeetingsTool

class Edit(SubPageEditForm):
    """ Edit
    """
    form_fields = Fields(IOpenMeetingsTool)
