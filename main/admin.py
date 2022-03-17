from django.contrib import admin
from .models import Group , Student ,Payment ,Blog ,Tutorial,Contact

admin.site.register(Group)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "group","gender","admission_date")
    list_filter = ("roll","admission_date","group")
    search_fields = ("name__startswith","roll__startswith")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("student_name","january","february","march","april","may","june","july","august","september","october","november","december")
    list_filter = ("january","february","march","april","may","june","july","august","september","october","november","december")
    search_fields = ("student__name","student__roll")

    def student_name(self, obj):
        return obj.student.name

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("user_name","title","created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username",)

    def user_name(self,obj):
        return obj.user.username



@admin.register(Tutorial)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","group_name","created_at")
    list_filter = ("created_at",)
    search_fields = ("title__startswith","group__group")

    def group_name(self,obj):
        return obj.group.group


@admin.register(Contact)
class BlogAdmin(admin.ModelAdmin):
    list_filter = ("name",)
    search_fields = ("name",)


admin.site.site_header = "SEROV ACADEMY OF FINE ARTS"
# admin.site.site_title = "AppTitle"
admin.site.index_title = "ACADEMY DATATBSE"
# admin.site.site_url = "Url for view site button"