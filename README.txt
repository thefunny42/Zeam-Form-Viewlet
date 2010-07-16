=================
zeam.form.viewlet
=================

``zeam.form.viewlet`` provide you with a `Zeam
Form <http://pypi.python.org/pypi/zeam.form.base>`_ in a viewlet.

Example
=======

Quick example::

  from zeam.form import base
  from zeam.form.viewlet import ViewletForm

  class CallUs(ViewletForm):

     label = u"Call us"

     fields = base.Fields(base.Field("Phone number"))
     actions = base.Actions(base.Action("Call"))

