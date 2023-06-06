from rest_framework import serializers
from .models import User, Pet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = '__all__'

    def get_age(self, obj):
        import datetime
        today = datetime.date.today()
        age = today.year - obj.date_of_birth.year
        if today < datetime.date(today.year, obj.date_of_birth.month, obj.date_of_birth.day):
            age -= 1
        return age
