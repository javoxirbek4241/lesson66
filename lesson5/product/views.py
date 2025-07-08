from django.shortcuts import render, redirect, get_object_or_404
from .models import Apartments
from .forms import ApartmentsForm
from django.views.generic import View
from django.urls import reverse_lazy
from django.db.models import Q


class ApartmentsList(View):
    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            apartments = Apartments.objects.filter(
                Q(title__icontains=query) | Q(price__icontains=query)
            )
        else:
            apartments = Apartments.objects.all().order_by('-id')
        return render(request, 'apartments_list.html', {'apartments':apartments})


class ApartmentsDetail(View):
    def get(self, request, pk):
        apartments = Apartments.objects.get(id=pk)
        return render(request, 'apartments_detail.html', {'apartments': apartments})


class ApartmentsCreate(View):
    def get(self,request):
        form = ApartmentsForm()
        return render(request, 'apartments_create.html', {'form':form})

    def post(self, request):
        form = ApartmentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('apartments_create')
        return render(request, 'apartments_create.html', {'form':form})


class ApartmentsUpdate(View):
    def get(self, request, pk):
        apartments = Apartments.objects.get(id=pk)
        form = ApartmentsForm(instance=apartments)
        return render(request, 'apartments_update.html', {'form': form, 'apartments': apartments})

    def post(self, request, pk):
        apartments = Apartments.objects.get(id=pk)
        form = ApartmentsForm(request.POST, request.FILES, instance=apartments)
        if form.is_valid():
            form.save()
            return redirect('apartments_detail', apartments.id)
        return render(request, 'apartments_update.html', {'form': form, 'apartments': apartments})


class ApartmentsDelete(View):
    def get(self, request, pk):
        apartments = get_object_or_404(Apartments, pk=pk)
        return render(request, 'apartments_delete.html', {'apartments': apartments})

    def post(self, request, pk):
        apartments = get_object_or_404(Apartments, pk=pk)
        apartments.delete()
        return redirect('apartments_list')













