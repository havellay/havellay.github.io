from django.contrib import admin

from oldgold.models import GoldPrice, Item, DetailImg

# TODO : there is a lot of redundant name tags / labels
# in the admin page, get rid of the unnecessary stuff

class DetailImgInline(admin.TabularInline):
    model = DetailImg

class GoldPriceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['rate']}),
    ]
    list_display = ('rate',)

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['description']}),
        ('Cover Image',     {'fields': ['cover_img']}),
        ('Weight',          {'fields': ['weight']}),
        ('Date Added',      {'fields': ['pub_date']}),
        ('Post valid for',  {'fields': ['valid_for']}),
    ]
    inlines = [DetailImgInline]
    list_display = ('description', 'cover_img', 'weight', 'pub_date', 'valid_for')

admin.site.register(GoldPrice, GoldPriceAdmin)
admin.site.register(Item, ItemAdmin)
