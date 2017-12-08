# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Blogpost


# Register your models here.

class BlogpostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blogpost, BlogpostAdmin)
