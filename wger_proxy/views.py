import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class ExerciseSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.GET.get('q', '')
        url = "https://wger.de/api/v2/exercise/?language=2&limit=100"
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

class ExerciseRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "message": "Welcome to the Exercise API",
            "available_endpoints": {
                "search": "/api/exercises/search/?q=bench"
            }
        })
