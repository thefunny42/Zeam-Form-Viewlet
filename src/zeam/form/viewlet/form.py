from zeam.form.base.form import FormCanvas

from megrok import pagetemplate as pt
from grokcore import viewlet as grok

pt.templatedir('default_templates')


class ViewletForm(grok.Viewlet, FormCanvas):
    """A form as a viewlet.
    """
    grok.baseclass()
    i18nLanguage = None

    def __init__(self, context, request, view, manager):
        grok.Viewlet.__init__(self, context, request, view, manager)
        FormCanvas.__init__(self, context, request)

    def update(self):
        grok.Viewlet.update(self)
        FormCanvas.update(self)
        self.updateForm()

    def default_namespace(self):
        namespace = super(ViewletForm, self).default_namespace()
        if self.i18nLanguage is not None:
            namespace['target_language'] = self.i18nLanguage
        return namespace

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
