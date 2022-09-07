from django.urls import path
from . import views
urlpatterns = [
    path("",views.hello,name='home'),
    path("register/",views.register,name='register'),
    path("login/",views.login_with_otp,name="login"),
    path("verify/",views.verify_otp,name='verify'),
    path("product/",views.ProductListView.as_view(),name="all-product"),
    path("product/<int:pk>",views.ProductDetailView.as_view(),name='detail-product'),
    path("logout/",views.log_out,name='logout'),
]