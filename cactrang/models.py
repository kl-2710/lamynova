from django.db import models
from django.utils import timezone # Để sử dụng timezone.now()
from django.template.defaultfilters import slugify # Để tạo slug tự động


    
# Model cho Bài viết/Tin tức (Blog Post)
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tiêu đề bài viết")
    slug = models.SlugField(max_length=200, unique=True, blank=True,
                            help_text="Đường dẫn URL thân thiện. Để trống để tự động tạo.")
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True,
                              verbose_name="Hình ảnh đại diện",
                              help_text="Hình ảnh cho bài viết (kích thước đề xuất: 800x450px)")
    excerpt = models.TextField(blank=True, verbose_name="Tóm tắt ngắn",
                               help_text="Một đoạn tóm tắt ngắn gọn về bài viết (hiển thị trên trang danh sách)")
    content = models.TextField(verbose_name="Nội dung bài viết")
    author = models.CharField(max_length=100, default="LAMYNOVA", verbose_name="Tác giả")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Ngày xuất bản")
    is_published = models.BooleanField(default=True, verbose_name="Hiển thị trên trang web")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bài viết / Tin tức"
        verbose_name_plural = "Bài viết / Tin tức"
        ordering = ['-published_date'] # Sắp xếp bài mới nhất lên đầu

    def save(self, *args, **kwargs):
        if not self.slug:
            # Tạo slug từ tiêu đề. Đảm bảo slug là duy nhất nếu tiêu đề trùng lặp.
            original_slug = slugify(self.title)
            queryset = BlogPost.objects.all().exclude(pk=self.pk) # Loại trừ chính bài viết này khi update
            count = 0
            slug = original_slug
            while queryset.filter(slug=slug).exists():
                count += 1
                slug = f"{original_slug}-{count}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Model cho FAQ (Câu hỏi thường gặp)
class FAQ(models.Model):
    question = models.CharField(max_length=500, verbose_name="Câu hỏi")
    answer = models.TextField(verbose_name="Câu trả lời")
    order = models.IntegerField(default=0, verbose_name="Thứ tự hiển thị", help_text="Số nhỏ hơn sẽ hiển thị trước")
    is_published = models.BooleanField(default=True, verbose_name="Hiển thị trên trang web")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    class Meta:
        verbose_name = "Câu hỏi thường gặp"
        verbose_name_plural = "Câu hỏi thường gặp"
        ordering = ['order', 'created_at'] # Sắp xếp theo thứ tự và ngày tạo

    def __str__(self):
        return self.question[:50] + "..." if len(self.question) > 50 else self.question