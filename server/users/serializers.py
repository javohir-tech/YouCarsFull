from rest_framework import serializers
from .models import User

# 
from rest_framework.exceptions  import ValidationError

class SingUpSarializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(max_length = 128 , required = True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password" , "confirm_password"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "confirm_password" : {"write_only" : True}
        }

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        
        
        if password != confirm_password :
            raise ValidationError({
                "password": "Passwords do not match."
            })

        return attrs
    
    def validate_username(self, value):
        if value.isdigit() :
            raise ValidationError("The username must consist of letters.")
        
        return value
    
    def create(self, validated_data):
        validated_data.pop("confirm_password")
        
        user = User(username = validated_data['username'] , email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user 