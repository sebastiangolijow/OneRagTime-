"""OneRagTime_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from  OneRagTime_app.api.router import router_endpoint_investment, router_endpoint_investor, router_endpoint_bill, router_endpoint_cashcall, router_endpoint_generate_bills, router_endpoint_send_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_endpoint_investment.urls)),
    path('api/', include(router_endpoint_investor.urls)),
    path('api/', include(router_endpoint_bill.urls)),
    path('api/', include(router_endpoint_cashcall.urls)),
    path('api/', include(router_endpoint_generate_bills.urls)),
    path('api/', include(router_endpoint_send_email.urls)),
]
