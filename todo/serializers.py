from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model

User = get_user_model()

class TodoSerializer(serializers.ModelSerializer):
    
    def validate_priority(self, priority):
        
        if priority >= 10:
            raise serializers.ValidationError('priority must be less than 10')
        
        return priority
    
    
    class Meta:
        model = Todo
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    
    # from related_name='todos'
    todos= TodoSerializer(read_only=True, many=True)
    
    class Meta:
        model = User
        fields = '__all__'