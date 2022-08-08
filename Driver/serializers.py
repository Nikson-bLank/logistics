from rest_framework import serializers
from .models import Driver_Detail

# from Logistics.Driver.views import driver_details
class Driver_DetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
    phone_number = serializers.CharField()
    address = serializers.CharField(max_length=300)
    vehicle_registration_number = serializers.CharField(max_length=100)
    driving_licence_number = serializers.CharField(max_length=100)
    registration_card_photo = serializers.FileField()
    driving_licence_photo = serializers.FileField()
    # vehicle_registration_number = serializers.ImageField(upload_to='images/')
    # driving_licence_number = serializers.ImageField(upload_to='images/')


    def create(self, validate_data):
        return Driver_Detail.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.password = validated_data.get('password',instance.password)
        instance.phone_number = validated_data.get('phone_number',instance.phone_number)
        instance.address = validated_data.get('address',instance.address)
        instance.vehicle_registration_number = validated_data.get('vehicle_registration_number',instance.vehicle_registration_number)
        instance.driving_licence_number = validated_data.get('driving_licence_number',instance.driving_licence_number)
        instance.save()
        return instance