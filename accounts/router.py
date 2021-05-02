from accounts.views import EmployeeViewset
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('employee',EmployeeViewset)
router=routers.DefaultRouter()
router.register('SIGNUP',EmployeeViewset)



