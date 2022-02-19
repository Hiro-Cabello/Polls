from django.urls import path

from . import views

#para poder usar el reverso es necesario
app_name="polls"

urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),


    #ex: /polls/5/
    #si lo quieo trabajar todo como clase tambien cambiar <int:pk>
    path("<int:question_id>/",views.detail,name="details"),
    path("<int:question_id>/results/",views.results,name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote"),

]







