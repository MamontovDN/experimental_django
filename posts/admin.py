from django.contrib import admin
from django.utils.safestring import mark_safe

from posts.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'upd_date', 'get_img']
    list_display_links = ['id', 'title', 'pub_date']
    empty_values = '--None--'
    fields = ('title', 'category', 'text', 'pub_date', 'upd_date',
              'views', 'img', 'get_img')
    readonly_fields = ('get_img', 'pub_date', 'upd_date', 'views',)
    save_on_top = True

    def get_img(self, obj):
        if not obj.img:
            return '-'
        return mark_safe(f'<img src="{obj.img.url}" width="205px">')

    get_img.short_description = 'Картинка'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('title',)
    empty_values = '--None--'


admin.site.site_title = 'Управление сайта'
admin.site.site_header = 'Управление новостями'
