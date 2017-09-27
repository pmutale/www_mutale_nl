from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin

from stick2uganda.models import Project, ContactPerson, Report, Question


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'location', 'image', 'start_implementation', 'end_implementation', 'project_summary')
        }),
    )


class AddQuestionAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactPerson)
admin.site.register(Report)
admin.site.register(Question, AddQuestionAdmin)

