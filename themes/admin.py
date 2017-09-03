from django.contrib import admin
from themes import models


# class DeadlineDate(admin.ModelAdmin):
#     formfield_overrides = {
#         models.ComingSoon.DateField: {'input_formats': ('%Y/%m/%d',)},
#     }
#
# admin.site.register(DeadlineDate, models.ComingSoon)