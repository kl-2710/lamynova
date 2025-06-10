from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cảm ơn bạn! Phản hồi của bạn đã được gửi thành công. Chúng tôi sẽ liên hệ lại trong thời gian sớm nhất.')
            return redirect('contact')
        else:
            messages.error(request, 'Có lỗi xảy ra khi gửi phản hồi. Vui lòng kiểm tra lại thông tin.')
    else:
        form = FeedbackForm()

    context = {
        'form': form
    }
  
    return render(request, 'qliphanhoi/contact.html', context)


