from django.contrib import admin
from .models import BlogPost, FAQ  # Import các Model đã tạo



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_published', 'slug')
    list_filter = ('is_published', 'author', 'published_date')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)} # Tự động tạo slug từ tiêu đề
    date_hierarchy = 'published_date' # Cho phép lọc theo ngày
    ordering = ('-published_date',) # Sắp xếp bài mới nhất lên đầu
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'excerpt', 'content', 'image')
        }),
        ('Thông tin xuất bản', {
            'fields': ('author', 'published_date', 'is_published'),
            'classes': ('collapse',) # Có thể ẩn phần này
        }),
    )

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('question', 'answer')
    list_editable = ('order', 'is_published') # Cho phép chỉnh sửa trực tiếp trên danh sách
    ordering = ('order',) # Sắp xếp theo thứ tự hiển thị

# Register your models here.
