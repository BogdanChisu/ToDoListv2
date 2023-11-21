from django.contrib import admin

from todo.models import Task

# Register your models here.

# in order to change the way this model is handled in the admin page
class TaskAdmin(admin.ModelAdmin):
    # create a list of all the objects to be displayed in the admin page
    list_display = ('task', 'is_completed')
    search_fields = ('task',)

# add the new task to the admin registry
admin.site.register(Task, TaskAdmin)