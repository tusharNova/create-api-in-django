
from django.contrib import admin
from django.urls import path
from webapp import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.employeeList.as_view()),
]
