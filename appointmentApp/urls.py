from django.urls import path 
from .views import home_view,blog_detail
urlpatterns=[
    path('' ,home_view , name= 'home'),
    path('/appointed-Created', blog_detail, name='created')
]