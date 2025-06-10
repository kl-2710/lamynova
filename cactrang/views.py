from django.shortcuts import render, get_object_or_404
from .models import BlogPost, FAQ  # Import các Model đã tạo

# View cho trang "pages-cactrang.html"
def pages(request):
    latest_posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')[:4]
    context = {
        'latest_posts': latest_posts,
      
    }
    return render(request, 'cactrang/pages.html', context)

# View cho trang danh sách Blog / Tin tức (blog-tin-tuc.html, bạn đang gọi là blog.html)
def blog(request):
    posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')
    context = {
        'posts': posts
    }
    return render(request, 'cactrang/blog.html', context) # Đảm bảo tên template là blog.html

# View cho trang chi tiết Bài viết (blog-details.html)
# View này sẽ thay thế blog-details1, blog-details2, blog-details3
def blog_details(request, slug): # Dùng slug để tìm bài viết
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    context = {
        'post': post
    }
    return render(request, 'cactrang/blog-details.html', context)

# View cho trang FAQ (faq.html)
def faq(request):
    faqs = FAQ.objects.filter(is_published=True).order_by('order', 'created_at')
    context = {
        'faqs': faqs
    }
    return render(request, 'cactrang/faq.html', context)

