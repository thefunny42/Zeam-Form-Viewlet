"""

We define a viewlet form here.

Let's grok our example:

  >>> from zeam.form.viewlet.testing import grok
  >>> grok('zeam.form.viewlet.ftests.forms.viewlet')

Let's render the view that use our viewlet now:

  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()

  >>> from zeam.form.viewlet.ftests.forms.viewlet import Context
  >>> context = Context()

Integration tests
-----------------

  >>> root = getRootFolder()
  >>> root['content'] = context

  >>> from zope.testbrowser.testing import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False

Empty submission
~~~~~~~~~~~~~~~~

We are going just to submit the form without giving any required
information, and we should get an error:

  >>> browser.open('http://localhost/content/index')
  >>> print browser.contents
  <div>
    <form action="http://localhost/content/index" method="post" enctype="multipart/form-data">
      <h3>Subscription corner</h3>
      <div class="fields">
        <div class="field">
          <label class="field-label" for="form-field-name">Name</label>
          <br />
          <input type="text" id="form-field-name" name="form.field.name" class="field" value="" />
        </div> <div class="field">
          <label class="field-label" for="form-field-email">Email</label>
          <br />
          <input type="text" id="form-field-email" name="form.field.email" class="field" value="" />
        </div>
      </div>
      <div class="actions">
        <div class="action">
          <input type="submit" id="form-action-subscribe" name="form.action.subscribe" value="Subscribe" class="action" />
        </div>
      </div>
    </form>
  </div>



"""

from zeam.form import viewlet as zeam
from grokcore import viewlet as grok


class Context(grok.Context):
    pass


class Index(grok.View):
    pass


class Manager(grok.ViewletManager):
    grok.context(Context)
    grok.view(Index)
    grok.name('manager')


class Form(zeam.ViewletForm):
    grok.context(Context)
    grok.view(Index)
    grok.viewletmanager(Manager)

    label = 'Subscription corner'
    fields = zeam.Fields(zeam.Field('Name'), zeam.Field('Email'))

    @zeam.action("Subscribe")
    def subscribe(self):
        pass
