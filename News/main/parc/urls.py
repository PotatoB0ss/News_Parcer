from django.urls import path
from .views import Base, f_scrap, Rubric, Search

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('custom_admin', f_scrap, name="custom_admin"),
    path('rubric/<sstr>', Rubric.as_view(), name='rubric'),
    path('search/', Search.as_view(), name='search'),
]