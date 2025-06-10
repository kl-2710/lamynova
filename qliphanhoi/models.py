from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Họ và tên")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Số điện thoại")
    message = models.TextField(verbose_name="Nội dung tin nhắn")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Thời gian gửi")
    is_processed = models.BooleanField(default=False, verbose_name="Đã xử lý")
    admin_response = models.TextField(blank=True, null=True, verbose_name="Phản hồi của Admin")

    class Meta:
        verbose_name = "Phản hồi"
        verbose_name_plural = "Phản hồi Khách hàng"
        ordering = ['-created_at'] # Mặc định sắp xếp theo thời gian gửi giảm dần

    def __str__(self):
        return f"Phản hồi từ {self.name} ({self.email})"
