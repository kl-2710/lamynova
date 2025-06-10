from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import SetPasswordForm

#Form đăng ký
class CustomUserCreationForm(UserCreationForm):
    last_name = forms.CharField(label='Họ', max_length=20, required=True)
    first_name = forms.CharField(label='Tên', max_length=20, required=True)
    email = forms.EmailField(label='Email', required=False, help_text="Nhập địa chỉ email hợp lệ.")
    password1 = forms.CharField(
        label='Đặt mật khẩu',
        strip=False,
        widget=forms.PasswordInput,
        help_text="<ul><li>Mật khẩu của bạn không thể quá giống với các thông tin cá nhân khác.</li><li>Mật khẩu của bạn phải chứa ít nhất 8 ký tự.</li><li>Mật khẩu của bạn không thể là một mật khẩu thường dùng.</li><li>Mật khẩu của bạn không thể chỉ gồm toàn số.</li></ul>"
    )
    password2 = forms.CharField(
        label='Xác nhận mật khẩu',
        strip=False,
        widget=forms.PasswordInput,
        help_text="Nhập lại mật khẩu của bạn để xác nhận."
    )
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')
        labels = {
            'username': 'Tên tài khoản',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email này đã được sử dụng. Vui lòng chọn một email khác.")
        return email
    
    def save(self, commit=True):
        # Gọi phương thức save của lớp cha để lưu username, password
        user = super().save(commit=False)
        # Lưu các trường mới được thêm vào
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email'] # Đảm bảo email được lưu
        if commit:
            user.save()
        return user
    
#Form đăng nhập
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Tên tài khoản' # Dịch nhãn username
        self.fields['password'].label = 'Mật khẩu'   # Dịch nhãn password
        self.error_messages['invalid_login'] = 'Tên tài khoản hoặc mật khẩu không đúng'
        self.error_messages['inactive'] = 'Tài khoản này đã bị vô hiệu hóa'

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                )
        return self.cleaned_data
    
#Form đặt lại mật khẩu
class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].label = 'Mật khẩu mới'
        self.fields['new_password2'].label = 'Xác nhận mật khẩu mới'
