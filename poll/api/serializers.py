from poll.models import Poll
from rest_framework import serializers

class PollSerializer(serializers.ModelSerializer):
   class Meta:
       model = Poll
       fields = ['question','option_one','option_two','option_three','option_one_count','option_two_count','option_three_count']