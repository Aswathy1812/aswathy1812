# from django import forms
# from django.contrib import admin
#
# # Register your models here.
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from app_user.models import AppUser
#
#
# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
#     password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
#
#     class Meta:
#         model = AppUser
#         fields = ('username',)
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('Passwords do not match')
#         return password2
#
#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = AppUser
#         fields = ('first_name', 'last_name', 'username', 'email', 'is_active', 'is_admin', 'password')
#
#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]
#
#
# class AppUserAdmin(UserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     list_display = ('id', 'first_name', 'last_name', 'username', 'email')
#     list_filter = ('is_admin',)
#
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('email', 'phone')}),
#         ('Permissions', {'fields': ('is_admin', 'is_active')}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'username', 'password1', 'password2', 'phone')}
#         ),
#     )
#
#     search_fields = ('email', 'username', 'phone')
#     ordering = ('id',)
#     filter_horizontal = ()
#
# admin.site.register(AppUser, AppUserAdmin)