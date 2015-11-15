from django.contrib import admin
from shortenersite.models import Urls
# Register your models here.


class UrlsAdmin(admin.ModelAdmin):
    list_display = (
        'short_id', 'httpurl', 'pub_date', 'count', 'count_fb', 'count_tw')
    ordering = ('-pub_date',)

# Register the Urls model with UrlsAdmin options
admin.site.register(Urls, UrlsAdmin)
