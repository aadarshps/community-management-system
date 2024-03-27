from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.index,name='index'),
    path('sign-in/',views.sign_in,name='sign-in'),
    path('sign-out/',views.sign_out,name='sign-out'),
    path('admin-dashboard/',views.admin_dashboard,name='admin-dashboard'),
    path('add-volunteer/',views.add_volunteer,name='add-volunteer'),
    path('view-volunteer/',views.view_volunteers,name='view-volunteer'),
    path('view-beneficary_ad/',views.view_beneficaries_admin,name='view-beneficary_ad'),
    path('add-welfareprograms/',views.add_welfareprograms,name='add-welfareprograms'),
    path('view-welfareprograms-admin/',views.view_welfareprograms_ad,name='view-welfareprograms-admin'),
    path('assign-programs/<int:pk>/',views.assign_programs,name='assign-programs'),
    path('assistance-list-admin/',views.view_assistance_admin,name='assistance-list-admin'),
    path('assistance-list-approve/<int:pk>/',views.approve_assistance,name='assistance-list-approve'),


]