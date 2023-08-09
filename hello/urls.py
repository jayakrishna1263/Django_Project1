from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path("<str:name>",views.greet,name="greet"),
    path("jk",views.jk,name="jk"),
    path("david",views.david,name="david"),
]
