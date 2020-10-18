from django.urls import path
from . import views
import xadmin
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    path('staffs/', views.staff_list.as_view()),
    path('staffs/<int:pk>/', views.staff_detail.as_view()),
    path('deps/',views.dep_list.as_view()),
    path('deps/<int:pk>/', views.dep_detail.as_view()),
    # 概要
    # path('schema/', schema_view),
    path('api/meal/<int:pk>',views.Meal_personal),
    # path('dismissstaff/<int:pk>/detail/custom_form',views.staff_form_iframe),
    # path('currentstaff/<int:pk>/detail/custom_form',views.staff_form_iframe),
    # path('allstaff/<int:pk>/detail/custom_form',views.staff_form_iframe),
    # path('department/<int:pk>/detail/custom_form',views.dep_form_iframe),
    # path('meal_allow/statistic',views.Meal_statistic),

]
