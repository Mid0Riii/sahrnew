from django.urls import path
from . import views
import xadmin

urlpatterns = [
    path('signs/add/sign_create_view',views.create_sign,name='create_sign'),
    path('signs/<int:pk>/detail/sign_detail_view',views.detail_sign),
    path('signs/<int:pk>/update/sign_edit_view',views.edit_sign,name='update_sign'),
]