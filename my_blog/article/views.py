from django.shortcuts import render
# 引入markdown模块
import markdown
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


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)

    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         # 包含 缩写、表格等常用扩展
                                         'markdown.extensions.extra',
                                         # 语法高亮扩展
                                         'markdown.extensions.codehilite',
                                     ])

    context = {'article': article}
    return render(request, 'article/detail.html', context)
