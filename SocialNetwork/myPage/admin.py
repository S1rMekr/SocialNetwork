from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from myPage.models import CustomUser, PostModel

# Register your models here.



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email', 'password','birth_date', 'country', 'profile_image', 'is_superuser', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields':('first_name', 'last_name', 'birth_date', 'country', 'profile_image')} ),
        ('Admin info', {'fields':('is_superuser', 'is_staff')})
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PostModel)