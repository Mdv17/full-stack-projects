# The variable notes inside the get notes cant be passed inside the response thats why we need serializers
# This is its gonna turn our python objects into json format

from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'