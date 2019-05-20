# Django
from django.views import View
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateResponseMixin, ContextMixin

# Project
from .forms import ContactForm

# Home Page
class HomeView(TemplateView):
    template_name = "home.html"

    # Context Data
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context["title"] = _("Home Page")
        context["content"] = "Duis veniam velit dolor ex aute in magna. Ullamco mollit nisi ea cillum do laborum eu. Tempor sunt sint ipsum velit id deserunt cupidatat cillum est pariatur ex. Tempor elit fugiat commodo aliquip elit nisi incididunt consequat minim. Voluptate non pariatur sit dolor adipisicing aute minim ipsum veniam ex nostrud cillum eiusmod. Laborum exercitation consequat elit consequat non nostrud. Fugiat cillum esse ullamco minim aute minim ex do exercitation veniam."
        return context

class InternationalizationView(TemplateView):
    template_name = "Internationalization.html"

    # Context Data
    def get_context_data(self, *args, **kwargs):
        context = super(InternationalizationView, self).get_context_data(*args,**kwargs)
        context["title"] = _("Internationalization")
        return context

# Contact Page
class ContactView(FormView, TemplateView):
    template_name = "contact.html"
    form_class = ContactForm

    # Context Data
    def get_context_data(self, *args, **kwargs):
        context = super(ContactView, self).get_context_data(*args,**kwargs)
        context["title"] = _("Contact Page")
        context["content"] = "Spanish Main Jolly Roger walk the plank warp cutlass Sink me main sheet lad belay weigh anchor. List chantey spike chase guns jib Spanish Main salmagundi hempen halter topmast strike colors. Driver boatswain pirate Privateer bucko topmast topgallant rigging hang the jib hempen halter."
        form = ContactForm(self.request.POST or None)
        context["form"] = form
        return context
    
    def form_valid(self, form):
        print(form)
        return redirect('dashboards:home')