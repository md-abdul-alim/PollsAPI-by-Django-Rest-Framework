from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Poll, Choice, Vote

# vote -> choice ->poll

# We have overriden the ModelSerializer method’s create() to save the User instances. We ensure that we set the password correctly using user.set_password, rather than setting the raw password as the hash. We also don’t want to get back the password in response which we ensure using extra_kwargs = {'password':
# {'write_only': True}}.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        user = User(
            email=validate_data['email'],
            username=validate_data['username']
        )
        user.set_password(validate_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'


"""
What have we got with this? The PollSerializer class has a number of methods,
•	A is_valid(self, ..) method which can tell if the data is sufficient and valid to create/update a model instance.
•	A save(self, ..) method, which knows how to create or update an instance.
•	A create(self, validated_data, ..) method which knows how to create an instance. This method can be overriden to customize the create behaviour.
•	A update(self, instance, validated_data, ..) method which knows how to update an instance. This method can be overriden to customize the update behaviour.
"""
