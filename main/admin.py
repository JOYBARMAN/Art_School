from django.contrib import admin
from .models import Group , Student ,Payment ,Blog ,Tutorial,Contact

admin.site.register(Group)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "group","gender","admission_date")
    list_filter = ("roll","admission_date","group")
    search_fields = ("name__startswith","roll__startswith")


admin.site.register(Payment)
admin.site.register(Blog)
admin.site.register(Tutorial)
admin.site.register(Contact)