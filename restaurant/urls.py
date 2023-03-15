from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path("menu/", views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
    # path("booking/", views.bookingview.as_view()),
    path('booking/', include(router.urls)),

]
