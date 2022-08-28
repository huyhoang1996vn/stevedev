from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .api import *

urlpatterns = [
    path(r"login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(r"login/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path(r"login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(r"book", get_book, name="get book"),
    path(r"borrow/book", BookTrackingCreateAPI.as_view(), name="borrow book"),
    path(r"return/book", return_book, name="return book"),
    path(r"tracking/book", get_book_tracking, name="tracking book"),
    path(r"renew/book", renew_tracking, name="renew book"),
]
