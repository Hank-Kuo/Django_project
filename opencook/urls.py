
from django.contrib import admin
from django.urls import path, include
from recipes import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_view),
    path('add/$', views.add),
    path('getAllUser/$', views.getAllUser),
    path('index/', views.index),
    path('常見問題/', views.normal,name="normal")
    #url(r'^new_add/(\d+)/(\d+)/$', views.add2, name='add2')
]
