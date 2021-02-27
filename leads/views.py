from django.shortcuts import render, HttpResponse, redirect
from .models import Lead
from .forms import LeadFrom, LeadModelForm
from .models import Agent


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


# create leads with model form provided by django frameworks Model from has been defined into the forms.py file with the database model name + ModelForm as a class name.

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


# update the leads with the help of model forms very similear to the create with model form. to update the data pass the instance with the modelform. in this case it is a id.
def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    context = {
        'form': form,
        'lead': lead
    }
    return render(request, "leads/lead_update.html", context)


def leads_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')

# update the data with the default dajngo form methoad  
# def lead_update(request, pk):
#     form = LeadFrom()
#     lead = Lead.objects.get(id=pk)
#     if request.method == "POST":
#         form = LeadFrom(request.POST)
#         if form.is_valid():
#             lead.first_name = form.cleaned_data['first_name']
#             lead.last_name = form.cleaned_data['last_name']
#             lead.age = form.cleaned_data['age']
#             lead.save()
#             return redirect('/leads')

#     context = {
#         'form': form,
#         'lead': lead
#     }
#     return render(request, "leads/lead_update.html", context)


# create a lead with defaut from provided by the django frameworks

# def lead_create(request):
#     # Inilize the emapty form to render and display
#     form = LeadFrom()
#     if request.method == "POST":

#         # Inilize the form with the data that cames with form when user sunit the form.
#         # This form object has entire html form with the html tags into it
#         form = LeadFrom(request.POST)
#         print("Form Data:")
#         print(form)

#         if form.is_valid():
#             print("Cleaned data:")
#             # cleaned_data is get the user submited data and conver into the python dictionary
#             print(form.cleaned_data)

#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )

#             return redirect('/leads')

#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)
