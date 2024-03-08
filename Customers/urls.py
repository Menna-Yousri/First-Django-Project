from django.urls import path
from Customers.views import customer1, customern
urlpatterns = [
    path("customer1", customer1),
    path("customern/<str:data>", customern)
]