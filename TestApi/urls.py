
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from TestApi import views

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'Employees', views.EmployeeViewSet)
router.register(r'Devices', views.DeviceViewSet)
router.register(r'Checkouts', views.CheckoutViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]