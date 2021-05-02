from django.contrib import admin
from django.urls import path,include
from .import views
from .router import router
from .views import EmployeeViewset

urlpatterns = [
	path('',include(router.urls)),
	#path('api/',include(accounts.urls)),
	path('GET/',views.get_data,name="GET"),
	#path('SIGNUP/',views.sign_up,name="SIGNUP"),
	]

"""app_name='accounts'
urlpatterns = [
	path('',api_detail_employee_view,name ="detail"),

]"""


