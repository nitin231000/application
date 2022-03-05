from poll.models import Poll
from poll.api.serializers import PollSerializer
from rest_framework import viewsets

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer



