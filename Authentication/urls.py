from django.urls import include, path
from Authentication import views
urlpatterns = [
    path('', views.index, name='index'),
    path('api/get-super-user', views.GetSuperUser.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]   