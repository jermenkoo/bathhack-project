import json
import random
import string

import requests as r

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext


@csrf_exempt
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('shortenersite/index.html', c)


@csrf_exempt
def shortenUrl(request):
    url = request.POST.get("url", '')
    print("POST", url)
    resp = r.get(
        "https://api.facebook.com/method/links.getStats?urls={}&format=json".format(url))
    resp_json = json.loads(resp.text)
    T = resp_json[0]['like_count']
    print("Facebook:", resp_json)

    R = r.get(
        "https://urls.api.twitter.com/1/urls/count.json?url={}".format(url))
    R_json = json.loads(R.text)
    print("Twitter", R_json)
    U = R_json['count']

    return render_to_response('shortenersite/result.html',
                              {'url': url,
                               "fb": T, "tw": U},
                              context_instance=RequestContext(request))
