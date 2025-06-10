from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'h-12 w-full rounded-[10px] border-[1px] border-colorAshGray bg-white px-5 font-bold outline-none focus:border-colorOrangyRed', 'id': 'contact-name', 'placeholder': 'Họ và tên của bạn'}),
            'email': forms.EmailInput(attrs={'class': 'h-12 w-full rounded-[10px] border-[1px] border-colorAshGray bg-white px-5 font-bold outline-none focus:border-colorOrangyRed', 'id': 'contact-email', 'placeholder': 'Email của bạn'}),
            'phone': forms.TextInput(attrs={'class': 'h-12 w-full rounded-[10px] border-[1px] border-colorAshGray bg-white px-5 font-bold outline-none focus:border-colorOrangyRed', 'id': 'contact-phone', 'placeholder': 'Số điện thoại của bạn (tùy chọn)'}),
            'message': forms.Textarea(attrs={'class': 'h-44 w-full rounded-[10px] border-[1px] border-colorAshGray bg-white px-5 py-4 font-bold outline-none focus:border-colorOrangyRed', 'id': 'contact-message', 'placeholder': 'Viết tin nhắn của bạn...', 'rows': '1'}),
        }
        labels = {
            'name': 'Họ và tên',
            'email': 'Email',
            'phone': 'Số điện thoại',
            'message': 'Lời nhắn',
        }
