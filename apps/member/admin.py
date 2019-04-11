from django.contrib import admin

from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    search_fields = ('user',)