from django.urls import path
from dashboard import views


urlpatterns = [
    path('index/',views.DashboardIndexView.as_view(),name='dashboard_index')
]
