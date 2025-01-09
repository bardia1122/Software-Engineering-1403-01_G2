from rest_framework import serializers
from .models import TextOptimization
import json

def toJson(output_text):
    return json.dumps(output_text)