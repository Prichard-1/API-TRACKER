from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the API root",
        "endpoints": [
            "/api/users/",
            "/api/activities/",
            "/api/login/",
            "/api/register/",
            "/api/user-detail/"
        ]
    })

