from django.shortcuts import render

# Create your views here.
# 导入 HttpResponse 模块
# from django.http import HttpResponse
# 导入数据模型ArticlePost
from .models import ArticlePost


# 视图函数
def article_list(request):
    # return HttpResponse("Hello World!")
    # 取出所有博客文章
    # articles = ArticlePost.object.all()
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates) 的对象
    context = {'articles': articles}
    # render 函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)

# 文章详情
def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)
    # 需要传递给模板的对象
    context = { 'article': article }
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)




