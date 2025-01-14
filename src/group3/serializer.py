from rest_framework import serializers

class SuggestionSerializer(serializers.Serializer):
    start = serializers.IntegerField()
    end = serializers.IntegerField()
    suggestion = serializers.CharField(max_length=255)

class TextSuggestionSerializer(serializers.Serializer):
    text = serializers.CharField()
