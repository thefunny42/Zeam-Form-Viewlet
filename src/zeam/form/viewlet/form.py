
from zeam.form.base.form import FormCanvas

from megrok import pagetemplate as pt
from grokcore import viewlet as grok

pt.templatedir('default_templates')


class ViewletForm(grok.Viewlet, FormCanvas):
    """A form as a viewlet.
    """
    grok.baseclass()

    def __init__(self, context, request, view, manager):
        grok.Viewlet.__init__(self, context, request, view, manager)
        FormCanvas.__init__(self, context, request)

    def updateForm(self):
        self.updateActions()
        self.updateWidgets()

    def render(self):
        return FormCanvas.render(self)

    render.base_method = True



class ViewletFormTemplate(pt.PageTemplate):
    """Default tempalte for ViewletForm
    """
    pt.view(ViewletForm)
