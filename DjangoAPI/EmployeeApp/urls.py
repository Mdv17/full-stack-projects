from django.urls import path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('department/', views.departmentApi),
    path('department/<int:id>/', views.departmentApi),

    path('employee/', views.employeeApi),
    path('employee/<int:id>/', views.employeeApi),

    path('employee/SaveFile/', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Add the static files URL configuration
