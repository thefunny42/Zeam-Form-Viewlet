"""

We define a viewlet manager form here.

Let's grok our example:

  >>> from zeam.form.viewlet.testing import grok
  >>> grok('zeam.form.viewlet.ftests.forms.viewletmanager')

Let's render the view that use our viewlet now:

  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()

  >>> from zeam.form.viewlet.ftests.forms.viewletmanager import Context
  >>> context = Context()

Integration tests
-----------------

  >>> root = getRootFolder()
  >>> root['content'] = context

  >>> from zope.app.wsgi.testlayer import Browser
  >>> browser = Browser()
  >>> browser.handleErrors = False

Submission
~~~~~~~~~~

We are going just to submit the form without giving any required
information, and we should get an error:

  >>> browser.open('http://localhost/content/index')
  >>> print browser.contents
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
  <div>
    <form action="http://localhost/content/index" method="post" enctype="multipart/form-data">
      <h3>Subscription corner</h3>
      <div class="fields">
        <div class="field">
          <label class="field-label" for="registration-field-name">Name</label>
          <br />
          <input type="text" id="registration-field-name" name="registration.field.name" class="field" value="" />
        </div> <div class="field">
          <label class="field-label" for="registration-field-email">Email</label>
          <br />
          <input type="text" id="registration-field-email" name="registration.field.email" class="field" value="" />
        </div>
      </div>
      <div class="actions">
        <div class="action">
          <input type="submit" id="registration-action-subscribe" name="registration.action.subscribe" value="Subscribe" class="action" />
        </div>
      </div>
    </form>
  </div>

  >>> 'Registration done for Sylvain' not in browser.contents
  True
  >>> browser.getControl('Name').value = "Sylvain"
  >>> browser.getControl('Email').value = "sylvain at example dot com"
  >>> browser.getControl('Subscribe').click()
  >>> 'Registration done for Sylvain' in browser.contents
  True

"""

from zeam.form import viewlet as zeam
from grokcore import viewlet as grok


class Context(grok.Context):
    pass


class Index(grok.View):
    grok.context(Context)


class Registration(zeam.ViewletManagerForm):
    grok.context(Context)
    grok.view(Index)

    label = 'Subscription corner'
    fields = zeam.Fields(zeam.Field('Name'), zeam.Field('Email'))

    @zeam.action("Subscribe")
    def subscribe(self):
        data, errors = self.extractData()
        if errors:
            return zeam.FAILURE
        self.status = "Registration done for %s" % (data['name'])
        return zeam.SUCCESS
