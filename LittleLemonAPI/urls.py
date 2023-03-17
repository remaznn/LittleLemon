from django.urls import path , include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [

    path('api-token-auth/', obtain_auth_token),
    path("menu/", views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    # path("booking/", views.bookingview.as_view()),
    path('booking/', include(router.urls)),
    path('message/', views.msg),
]
