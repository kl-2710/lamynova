from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    # Thêm 'display_admin_response_summary' vào list_display
    # Bạn có thể điều chỉnh thứ tự các cột tùy ý
    list_display = ('name', 'email', 'display_message_summary', 'display_admin_response_summary', 'created_at', 'is_processed')

    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'email', 'message', 'admin_response')
    readonly_fields = ('created_at',)

    # Đảm bảo 'admin_response' vẫn có trong fields để bạn có thể chỉnh sửa nó khi xem chi tiết
    fields = ('name', 'email', 'phone', 'message', 'created_at', 'is_processed', 'admin_response')

    # Phương thức tùy chỉnh để hiển thị tóm tắt nội dung tin nhắn của khách hàng
    def display_message_summary(self, obj):
        if obj.message: # Đảm bảo rằng tin nhắn không rỗng
            return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
        return "Không có nội dung" # Hoặc bất kỳ chuỗi nào bạn muốn hiển thị nếu tin nhắn trống
    display_message_summary.short_description = 'Nội dung KH' # Tên cột thân thiện cho phản hồi khách hàng

    # --- Phương thức mới để hiển thị tóm tắt nội dung phản hồi của Admin ---
    def display_admin_response_summary(self, obj):
        if obj.admin_response: # Kiểm tra xem có phản hồi admin không
            return obj.admin_response[:50] + '...' if len(obj.admin_response) > 50 else obj.admin_response
        return "Chưa phản hồi" # Hoặc 'N/A' nếu chưa có nội dung
    display_admin_response_summary.short_description = 'Phản hồi Admin' # Tên cột thân thiện