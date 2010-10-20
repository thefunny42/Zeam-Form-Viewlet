
import martian
import grokcore.component
import grokcore.view

from zeam.form.viewlet.form import ViewletManagerForm


class ManagerGrokker(martian.ClassGrokker):
    martian.component(ViewletManagerForm)
    martian.directive(grokcore.component.name,
                      get_default=grokcore.view.meta.views.default_view_name)

    def execute(self, factory, config, name, **kw):
        if factory.prefix is None:
            factory.prefix = name
            return True
        return False
