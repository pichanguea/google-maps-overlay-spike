from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def google(request, lt, lg, zoom):
    return render_to_response(
        'maps.html', 
        {
            'lat': lt,
            'long': lg,
            'zoom': zoom
        }, 
        context_instance=RequestContext(request)
    )

