from rest_framework import serializers
from .models import Poll, Choice, Vote

# vote -> choice ->poll


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
