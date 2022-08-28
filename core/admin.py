from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as UserAdmin1


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)


class TitleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Title, TitleAdmin)


class UserAdmin(UserAdmin1):
    pass


admin.site.register(User, UserAdmin)


class BookTrackingAdmin(admin.ModelAdmin):
    pass


admin.site.register(BookTracking, BookTrackingAdmin)


class RoleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Role, RoleAdmin)
