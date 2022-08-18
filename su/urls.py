from django.urls import path
from su import views

urlpatterns = [

    path('signup', views.CustomerSignUp.as_view(), name='signup'),
    path('signin', views.CustomerSignIn.as_view(), name='signin'),
    path('signout', views.signout, name='signout'),
    path('listemployee', views.ListEmployeeView.as_view(), name='listemployee'),
    path('createemployee', views.CreateEmployeeView.as_view(), name='createemployee'),
    path('editemployee/<int:id>', views.UpdateEmployeeView.as_view(), name='editemployee'),
    path('deleteemployee/<int:id>', views.DeleteEmployeeView.as_view(), name='deleteemployee'),





]