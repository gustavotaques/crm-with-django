from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from .models import Lead #Agent
from .forms import LeadModelForm, CustomUserCreationForm #LeadForm


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


# def landing_page(request):
#     return render(request, 'landing.html')

# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         "leads": leads
#     }

#     return render(request, 'leads/lead_list.html', context)

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)

#     context = {
#         "lead": lead
#     }

#     return render(request, 'leads/lead_detail.html', context)

# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form": form
#     }

#     return render(request, "leads/lead_create.html", context)

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect(f"/leads/{pk}")

#     context = {
#         "form": form,
#         "lead": lead
#     }

#     return render(request, "leads/lead_update.html", context)

# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('/leads')
