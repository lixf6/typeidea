from django.shortcuts import render
from django.http import HttpResponse
# from .models import Post, Tag, Category

# Create your views here.
def post_list(request, category_id=None, tag_id=None):
    # content = 'post_list category_id={category_id}, tag_id={tag_id}'.format(category_id=category_id, tag_id=tag_id)
    # return HttpResponse(content)
    return render(request, 'blog/list.html', context={'name': 'post_list'})

def post_detail(request, post_id=None):
    # return HttpResponse('detail')
    return render(request, 'blog/detail.html', context={'name': 'post_detail'})