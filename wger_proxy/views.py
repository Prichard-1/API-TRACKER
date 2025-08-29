from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class ExerciseSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.GET.get('q', '')
        url = f"https://wger.de/api/v2/exercise/?language=2&limit=100"
        response = requests.get(url)
        data = response.json()

        if query:
            filtered = [
                ex for ex in data['results']
                if query.lower() in ex['name'].lower()
            ]
        else:
            filtered = data['results']

        return Response(filtered)


# Create your views here.
