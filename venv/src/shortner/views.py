from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent
from .forms import SubmitUrlForm
from .models import UrlprojectURL
# Create your views here.


def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "shortner/home.html", {})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "URL Project",
            "form": the_form
        }
        return render(request, "shortner/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "URL Project",
            "form": form
        }
        template = "shortner/home.html"

        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = UrlprojectURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created":created,    
                }
            if created:
                template = "shortner/success.html"
            else:
                template = "shortner/already-exists.html"

        return render(request, template , context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = UrlprojectURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
        


    def post(self,request,*args,**kwargs):
        return HttpResponse()

