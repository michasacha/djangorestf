import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_view(request, *args, **kwargs):
    print(request.body)
    data = json.loads(request.body)
    pre_data = json.dumps(data)
    print(data)
    data['headers'] = dict(request.headers)
    print(request.headers)
    data['content_type'] = request.content_type
    
    data['params'] = dict(request.GET)
    data['post-data'] = dict(request.POST)
    return JsonResponse(data)
        
          
  