from django.contrib import admin
from .models import GearRequest


@admin.register(GearRequest)
class GearRequestAdmin(admin.ModelAdmin):
    list_display = ['requester', 'item_name', 'quantity', 'urgency', 'status', 'created_at']
    list_filter = ['status', 'urgency']
    search_fields = ['item_name', 'requester__name', 'justification']
    actions = ['approve_requests', 'deny_requests']

    def approve_requests(self, request, queryset):
        from django.utils import timezone
        queryset.update(status='approved', reviewed_by=request.user, reviewed_at=timezone.now())
    approve_requests.short_description = "Approve selected requests"

    def deny_requests(self, request, queryset):
        from django.utils import timezone
        queryset.update(status='denied', reviewed_by=request.user, reviewed_at=timezone.now())
    deny_requests.short_description = "Deny selected requests"
