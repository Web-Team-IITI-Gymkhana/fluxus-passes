from django.contrib import admin

from .models import PassRequested

# Register your models here.
@admin.register(PassRequested)
class PassRequestedAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "requested_at")
    search_fields = ("email","name")
    list_filter = ("requested_at",)
    readonly_fields = ('requested_at',)
    ordering = ("-requested_at",)

    actions = ["issue_pass"]
    def issue_pass(self, request, queryset):
        for pass_requested in queryset:
            PassIssued.objects.create(email=pass_requested.email)
            pass_requested.delete()

from .models import PassIssued
@admin.register(PassIssued)
class PassIssuedAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "issued_at")
    search_fields = ("email","name")
    list_filter = ("issued_at",)
    readonly_fields = ('issued_at',)
    ordering = ("-issued_at",)