from django.urls import path
from .views import HomeView, BlogList, BlogDetail, AboutView,BlogCreate, BlogDelete, EuropeList,EuroBlogDetail, MessageView

urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("list/", BlogList.as_view(), name="list"),
    path("detail/<int:pk>/", BlogDetail.as_view(), name="detail"),
    path("about/", AboutView.as_view(), name="about"),
    path("create/",BlogCreate.as_view(), name="create"),
    path("detail/<int:pk>/delete/", BlogDelete.as_view(), name="delete"),
    path("europelist/", EuropeList.as_view(),name="europelist"),
    path("eurodetail/<int:pk>/", EuroBlogDetail.as_view(), name="europe_detail"),
    path("message/", MessageView.as_view(),name="message"),
]
