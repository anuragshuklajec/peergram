from django.urls import path
from .views import *

urlpatterns = [
    path('createDomain/',domain),
    path('getDomain/',domain),
    path('createTag/',tag),
    path('getTag/',tag),

]