from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/',views.home),
    path('signup/',views.SignupPage),
    path('login/',views.loginpage),
    path('logout/',views.pagelogout),
    path('post/',views.postdata),
    path('profile/',views.profilehome),
    path('edit/<int:id>',views.updatedata),
    path('delet/<int:id>',views.deletfun),
    path('profilepage/',views.profile),
    path('pro/',views.alldata),
    path('comment/<int:id>', views.add_comment),
    path('profile/<str:author>', views.pro),
    path('contact/',views.contact),
    path('fullp/<int:id>', views.fullp),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
