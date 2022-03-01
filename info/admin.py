from django.contrib import admin
import logging
from .models import News, Country, Crossing

logger = logging.getLogger(__name__)


class StaffRequiredAdminMixin(object):

    def check_perm(self, user_obj):
        if not user_obj.is_active or user_obj.is_anonymous:
            return False
        if user_obj.is_superuser or user_obj.is_staff:
            return True
        return False

    def has_add_permission(self, request):
        return self.check_perm(request.user)

    def has_change_permission(self, request, obj=None):
        return self.check_perm(request.user)

    def has_module_permission(self, request):
        return self.check_perm(request.user)

class NewsAdmin(StaffRequiredAdminMixin, admin.ModelAdmin):
    list_display = ('heading', 'updated_at')
    
class CountryAdmin(StaffRequiredAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'order', 'name')

class CrossingAdmin(StaffRequiredAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'order', 'name', 'country')
    list_filter = ['country__name']


admin.site.register(News, NewsAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Crossing, CrossingAdmin)