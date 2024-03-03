from django.urls import path
from placement_app import views


urlpatterns = [ 


# <------------------------------ Admin login Only------------------------------->
path('admin_login/',views.admin_login,name="admin_login"),
path('adminloginsave/',views.adminloginsave,name="adminloginsave"),
path('admin_logout/',views.admin_logout,name="admin_logout"),


path('profile/',views.profile,name="profile"),




# <----------- Login | admin Only------------>

path('main_admin_master/',views.main_admin_master,name="main_admin_master"),
path('admin_home/',views.admin_home,name="admin_home"),

# <----------- Student data | admin Only------------>

path('student_table/',views.student_table,name="student_table"),
path('student_delete/<int:id>/',views.student_delete,name="student_delete"),


# <----------- Company data | admin Only------------>

path('company_table/',views.company_table,name="company_table"),
path('company_delete/<int:id>/',views.company_delete,name="company_delete"),

# <----------- PS report data | admin Only------------>

path('ps_report_table/',views.ps_report_table,name="ps_report_table"),
path('download_ps_report/', views.download_ps_report, name='download_ps_report'),

]
