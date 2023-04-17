from django.shortcuts import render,redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import AddLinkForm
from .models import Link

# Create your views here.
def home_view(request):
    
    no_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)
    
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "oops ... Couldn't get name or price"
        except:
            error = "oops ... Something wrong Happened"
    
    form = AddLinkForm()

    qs = Link.objects.all()
    no_items = qs.count()

    if no_items > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)

            no_discounted = len(discount_list)  
    
    context = {
        'qs':qs,
        'no_items':no_items,
        'no_discounted':no_discounted,
        'form':form,
        'error':error,
    }

    return render(request=request,template_name="links/main.html",context=context)              

class LinkDeleteView(DeleteView):
    model = Link
    template_name = "links/confirm_del.html"
    success_url = reverse_lazy('home') 

def update_prices(request):
    
    qs = Link.objects.all()
    for link in qs:
        link.save()

    return redirect('home')    

