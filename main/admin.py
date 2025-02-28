from django.contrib import admin
from main.models import(Topic, Resource, Problem, CodeSnippet)
# Register your models here.

admin.site.register(Topic)
admin.site.register(Resource)
admin.site.register(Problem)
admin.site.register(CodeSnippet)
