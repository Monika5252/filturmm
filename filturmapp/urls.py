
from django.urls import path
from . import views
urlpatterns = [
    path('form1',views.fun1,name='form1'),
    path('', views.logdata),
    path( 'd', views.dashbord ,name='dashboard'),
    path('emplogin',views.elogin,name='login'),
    path('approv', views.approve, name="approve"),
    path('logout',views.logout,name='logout'),
    path('empleave', views.empLeave, name='empleave'),
    path('empleavedata',views.empleavedata,name='empleavedata'),
    path('punchin',views.punchdata,name='punchdata')

]