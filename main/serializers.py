from rest_framework import serializers
from .models import StudentBasicDetail, LeaveHistory, StudentContactDetail, FacultyDetail, Department


class StudentBasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBasicDetail
        fields = '__all__'

class LeaveHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveHistory
        fields = '__all__'

class StudentContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentContactDetail
        fields = '__all__'

class FacultyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyDetail
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'