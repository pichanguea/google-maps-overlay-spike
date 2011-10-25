from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def google(request):
    return render_to_response(
        'maps.html', 
        {
            'lat': request.GET['latitude'],
            'long': request.GET['longitude'],
            'zoom': request.GET['zoom']
        }, 
        context_instance=RequestContext(request)
    )

