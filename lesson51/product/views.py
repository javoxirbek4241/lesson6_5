from django.shortcuts import render, redirect,get_object_or_404
from .models import Conditioners


def conditioner_list(request):
    conditioners = Conditioners.objects.all().order_by('-id')
    return render(request, 'conditioner_list.html', {'conditioners' : conditioners})
# Create your views here.

def conditioner_detail(request, pk):
    conditioners = Conditioners.objects.filter(id=pk).first()
    return render(request, 'conditioner_detail.html', {'conditioners':conditioners})

def create_conditioner(request):
    if request.method == "POST":
        name = request.POST['name']
        brand = request.POST['brand']
        cooling_capacity = request.POST.get('cooling_capacity')
        power_consumption = request.POST.get('power_consumption')
        inverter = True if request.POST.get('inverter') == 'on' else False
        room_size = request.POST.get('room_size')
        noise_level = request.POST.get('noise_level')
        functions = request.POST.get('functions')
        price = request.POST['price']
        image = request.FILES.get('image')

        Conditioners.objects.create(
            name=name,
            brand=brand,
            cooling_capacity=cooling_capacity,
            power_consumption=power_consumption,
            inverter=inverter,
            room_size=room_size,
            noise_level=noise_level,
            functions=functions,
            price=price,
            image=image
        )
        return redirect('conditioners')  # bu URL nomi sendagi list sahifa nomi bo'lishi kerak

    return render(request, 'create_conditioner.html')


def update_conditioner(request, pk):
    conditioners = get_object_or_404(Conditioners, pk=pk)

    if request.method == "POST":
        conditioners.name = request.POST['name']
        conditioners.brand = request.POST['brand']
        conditioners.cooling_capacity = request.POST.get('cooling_capacity')
        conditioners.power_consumption = request.POST.get('power_consumption')
        conditioners.inverter = True if request.POST.get('inverter') == 'on' else False
        conditioners.room_size = request.POST.get('room_size')
        conditioners.noise_level = request.POST.get('noise_level')
        conditioners.functions = request.POST.get('functions')
        conditioners.price = request.POST['price']

        # Agar yangi rasm yuklangan bo‘lsa — almashtiramiz
        if request.FILES.get('image'):
            conditioners.image = request.FILES.get('image')

        conditioners.save()
        return redirect('conditioner_detail', pk=conditioners.id)

    return render(request, 'update_conditioner.html', {'conditioners': conditioners})

def delete_conditioner(request, pk):
    conditioners = get_object_or_404(Conditioners, id=pk)
    if request.method == "POST":
        if 'yes' in request.POST:
            conditioners.delete()
            return redirect('conditioners')  # bu sizning ro'yxat sahifangiz
        elif 'no' in request.POST:
            return redirect('conditioner_detail', pk=pk)  # detail sahifa
    return render(request, 'conditioner_del.html', {'conditioners': conditioners})































































