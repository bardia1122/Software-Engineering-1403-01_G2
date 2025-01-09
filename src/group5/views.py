from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from group5.ngram_utils import NGramModel

ngram_model = NGramModel()


def home(request):
    return render(request, 'group5.html', {'group_number': '5'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def suggest_word_api(request):
    text = request.GET.get('text', '')
    dataset_name = request.GET.get('dataset', 'fa')
    suggestion = ngram_model.suggest_word(text, dataset_name)
    return Response({'suggestion': suggestion})
