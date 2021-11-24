from django.urls import path
from .views import CreateAdvisorView, RegisterUserView, LoginUserView, AdvisorListView, BookAdvisorView, BookingView


urlpatterns = [
    path('advisor/', CreateAdvisorView.as_view(), name='admin-advisor'),
    path('user/register/', RegisterUserView.as_view(), name='user-registraion'),
    path('user/login/', LoginUserView.as_view(), name='user-login'),
    path('user/<int:user_id>/advisor/', AdvisorListView.as_view(), name='advisor-list'),
    path('user/<int:user_id>/advisor/<int:advisor_id>/', BookAdvisorView.as_view(), name='create-booking'),
    path('user/<int:user_id>/advisor/booking/', BookingView.as_view(), name='booking-list'),
]