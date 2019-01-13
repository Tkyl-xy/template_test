from django.urls import path
from .views import reg, index1

urlpatterns = [
	path('reg', reg),
	path('index1', index1)
]