# -*- coding: utf-8 -*-
# Copyright (c) 2010 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$


from zeam.form.base.interfaces import IFormCanvas


class IInlineForm(IFormCanvas):
    """A form that can be inserted inside an another page / layout.
    """
