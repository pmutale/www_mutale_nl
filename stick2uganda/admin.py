from django.contrib import admin

from stick2uganda.models import Project, ContactPerson, Report, Question


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'location', 'start_implementation', 'end_implementation', 'project_summary')
        }),
        ('Contact:', {
            'classes': ('collapse',),
            'fields': ('contact', )
        }),
        ('Reports:', {
            'classes': ('collapse',),
            'fields': ('report', )
        })
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactPerson)
admin.site.register(Report)
admin.site.register(Question)

