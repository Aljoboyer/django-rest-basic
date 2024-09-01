from rest_framework import serializers
from . models import Aiquest
from . models import Students

class AiquestSerializer(serializers.Serializer):
    teacher_name = serializers.CharField(max_length=25)
    course_name = serializers.CharField(max_length=25)
    course_duration = serializers.IntegerField()
    seat = serializers.IntegerField()

    def create(self, validate_data):
        return Aiquest.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.teacher_name = validated_data.get('teacher_name', instance.teacher_name)
        instance.course_name = validated_data.get('course_name', instance.course_name)
        instance.course_duration = validated_data.get('course_duration', instance.course_duration)
        instance.seat = validated_data.get('seat', instance.seat)

        instance.save()
        return instance

class StudentSerializer(serializers.Serializer):
    st_name = serializers.CharField(max_length=25)
    roll = serializers.IntegerField()
    section = serializers.CharField(max_length=2)
    classname = serializers.CharField(max_length=24)

    def create(self, validate_data):
        return Students.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.st_name = validated_data.get('st_name', instance.st_name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.section = validated_data.get('section', instance.section)
        instance.classname = validated_data.get('classname', instance.classname)

        instance.save()
        return instance