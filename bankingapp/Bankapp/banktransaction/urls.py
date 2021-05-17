from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('view_all_customers',views.view_all_customers,name = 'view_all_customers'),
    path('create_your_account',views.create_your_account,name = 'create_your_account'),
    path('account_detail/<int:pk>/',views.view_a_customer,name = 'account_detail' ),
    path('transferMoney',views.moneyTransfer,name = 'transferMoney'),
   ]