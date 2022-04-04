from webbrowser import get
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
class GetSuperUser(APIView):
    def get(self,request):
        users = User.objects.all()
        responseData = {
            'id': 1,
            'name': 'admin',
            'password' : 'admin'    
        }
        return JsonResponse(responseData)

def index(request):
   text = "<p>Creating successful RESTful API Setups...</p>"
   return HttpResponse(text)