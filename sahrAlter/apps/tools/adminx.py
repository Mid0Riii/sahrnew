import xadmin
from . import views

xadmin.site.register_view(r'countDuty/$', views.CountDutyView, name='countDuty')
