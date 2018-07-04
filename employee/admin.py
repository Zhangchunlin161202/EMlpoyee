# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from employee.models import *

admin.site.register(CustomerLinkman)
admin.site.register(HouseInfo)
admin.site.register(HouseType)
admin.site.register(UserRole)
admin.site.register(DepartmentInfo)
admin.site.register(UserInfo)
