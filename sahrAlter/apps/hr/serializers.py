from rest_framework import serializers
from .models import Staff, Department


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id','at_post', 'name', 'gender', 'idNum', 'birth',
                  'rank', 'rankAca', 'enterDate', 'dep', 'duty', 'dutyTime', 'hireMet', 'position', 'title',
                  'eduBkg', 'grade', 'learnExp', 'marry', 'status', 'folk', 'regLoc', 'socIns','socInsNum',
                  'phone', 'phoneOther', 'emerPeople', 'emerPhone', 'more')


class DepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'createTime', 'creator', 'director', 'info')
