from django.contrib import admin

from .models import Header, HeaderBody, Tariffs

admin.site.register(Header)


admin.site.register(HeaderBody)


admin.site.register(Tariffs)