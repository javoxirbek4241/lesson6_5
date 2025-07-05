from django.shortcuts import render, redirect, get_object_or_404
from .models import Cameras


def camera_list(request):
    cameras = Cameras.objects.all().order_by('-id')
    return render(request, 'camera_list.html', {'cameras': cameras})


def camera_detail(request, pk):
    camera = get_object_or_404(Cameras, id=pk)
    return render(request, 'camera_detail.html', {'camera': camera})


def create_camera(request):
    if request.method == "POST":
        name = request.POST['name']
        brand = request.POST['brand']
        resolution = request.POST.get('resolution')
        lens = request.POST.get('lens')
        night_vision = True if request.POST.get('night_vision') == 'on' else False
        connectivity = request.POST.get('connectivity')
        power = request.POST.get('power')
        features = request.POST.get('features')
        price = request.POST['price']
        image = request.FILES.get('image')

        Cameras.objects.create(
            name=name,
            brand=brand,
            resolution=resolution,
            lens=lens,
            night_vision=night_vision,
            connectivity=connectivity,
            power=power,
            features=features,
            price=price,
            image=image
        )
        return redirect('cameras')

    return render(request, 'create_camera.html')


def update_camera(request, pk):
    camera = get_object_or_404(Cameras, pk=pk)

    if request.method == "POST":
        camera.name = request.POST['name']
        camera.brand = request.POST['brand']
        camera.resolution = request.POST.get('resolution')
        camera.lens = request.POST.get('lens')
        camera.night_vision = True if request.POST.get('night_vision') == 'on' else False
        camera.connectivity = request.POST.get('connectivity')
        camera.power = request.POST.get('power')
        camera.features = request.POST.get('features')
        camera.price = request.POST['price']

        if request.FILES.get('image'):
            camera.image = request.FILES.get('image')

        camera.save()
        return redirect('camera_detail', pk=camera.id)

    return render(request, 'update_camera.html', {'camera': camera})


def delete_camera(request, pk):
    camera = get_object_or_404(Cameras, id=pk)
    if request.method == "POST":
        if 'yes' in request.POST:
            camera.delete()
            return redirect('cameras')
        elif 'no' in request.POST:
            return redirect('camera_detail', pk=pk)
    return render(request, 'camera_del.html', {'camera': camera})
