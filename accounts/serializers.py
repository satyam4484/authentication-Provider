from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class userSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields=['id','email','first_name','last_name','is_admin','last_login']
        extra_kwargs = {'email': {'required': False}}
