from django.contrib import admin
from .models import Advertisement
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'price', 'auction', 'photo']
    list_filter = ['auction', 'created_at', 'id']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    search_fields = ['title']
    fieldsets = (
        ('Общее', {'fields': ('id', 'title', 'description', 'user', 'image')}),
        ('Финансы', {'fields': ('price', 'auction'),
                     'classes': ['collapse']})
    )
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
admin.site.register(Advertisement, AdvertisementAdmin)

