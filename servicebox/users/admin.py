from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

#class UserCreateForm(UserCreationForm):
#
#    class Meta:
#        model = User
#        fields = ('email', 'first_name' , 'last_name', 'company' )
#
#class CustomUserAdmin(UserAdmin):
#    add_form = UserCreateForm
#
#    UserAdmin.fieldsets += (
#        (None, {
#            'classes': ('wide',),
#            'fields': ('company', 'role'),
#        }),
#    )
#
#    UserAdmin.add_fieldsets += (
#        (None, {
#            'classes': ('wide',),
#            'fields': ('company', 'role'),
#        }),
#    )
#    UserAdmin.list_display += ('company', 'role')
#
admin.site.register(User)
