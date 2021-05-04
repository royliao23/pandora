from rest_framework import routers
from app.viewsets import *

#from user.api.viewsets3 import userviewsets
router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'people', FoodViewSet)

#router.register('user', userviewsets, basename ='user_api')
