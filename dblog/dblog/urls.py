
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import static

from dblog import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('user.urls','user'),namespace='user')),
    path('article/', include(('article.urls','article'),namespace='article')),
    path('category/', include(('category.urls','category'),namespace='category')),

]

# 配置media访问路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

