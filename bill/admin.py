from django.contrib import admin
from .models import cosutomer_detailes,employee_detailes,reading
from django.contrib.auth.models import User
@admin.register(cosutomer_detailes)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'name','meter_num','address','email','mobile_num','gst','pan','ty')

class MyModelAdmin(admin.ModelAdmin):
    def result_display(self, obj):
        return obj.total

    result_display.short_description = 'total'

    def save_model(self, request, obj, form, change):
        obj.total = obj.reading * obj.price
        super().save_model(request, obj, form, change)






admin.site.register(reading, MyModelAdmin)


@admin.register(employee_detailes)
class Employee_detailesAdmin(admin.ModelAdmin):
    list_display = ('user', 'data_added',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
                return qs
        return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
