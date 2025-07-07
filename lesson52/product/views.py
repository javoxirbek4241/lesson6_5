from django.shortcuts import render, redirect, get_object_or_404
from .models import Cameras  # model nomi ham o'zgargan bo'lishi kerak
from .forms import CamerasForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# def camera_list(request):
#     cameras = Cameras.objects.all().order_by('-id')
#     return render(request, 'camera_list.html', {'cameras': cameras})

class CamerasList(ListView):
    model = Cameras
    template_name = 'camera_list.html'
    context_object_name = 'cameras'





# def camera_detail(request, pk):
#     camera = Cameras.objects.filter(id=pk).first()
#     return render(request, 'camera_detail.html', {'camera': camera})

class CamerasDetail(DetailView):
    model = Cameras
    template_name = 'camera_detail.html'
    context_object_name = 'camera'



# def create_camera(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         brand = request.POST['brand']
#         resolution = request.POST.get('resolution')
#         lens = request.POST.get('lens')
#         night_vision = True if request.POST.get('night_vision') == 'on' else False
#         features = request.POST.get('features')
#         price = request.POST['price']
#         image = request.FILES.get('image')
#
#         Cameras.objects.create(
#             name=name,
#             brand=brand,
#             resolution=resolution,
#             lens=lens,
#             night_vision=night_vision,
#             features=features,
#             price=price,
#             image=image
#         )
#         return redirect('cameras')  # bu ro'yxat sahifasi URL nomi
#
#     return render(request, 'create_camera.html')

# def create_camera(request):
#     form = CamerasForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('cameras')
#     return render(request, 'create_camera.html', {'form':form})

class CamerasCreate(CreateView):
    model = Cameras
    form_class = CamerasForm
    template_name = 'create_camera.html'
    success_url = reverse_lazy('cameras')





# def update_camera(request, pk):
#     camera = get_object_or_404(Cameras, pk=pk)
#
#     if request.method == "POST":
#         camera.name = request.POST['name']
#         camera.brand = request.POST['brand']
#         camera.resolution = request.POST.get('resolution')
#         camera.lens = request.POST.get('lens')
#         camera.night_vision = True if request.POST.get('night_vision') == 'on' else False
#         camera.features = request.POST.get('features')
#         camera.price = request.POST['price']
#
#         if request.FILES.get('image'):
#             camera.image = request.FILES.get('image')
#
#         camera.save()
#         return redirect('camera_detail', pk=camera.id)
#
#     return render(request, 'update_camera.html', {'camera': camera})

# def update_camera(request, pk):
#     camera = get_object_or_404(Cameras, pk=pk)
#     form = CamerasForm(request.POST, request.FILES, instance=camera)
#     if form.is_valid():
#         form.save()
#         return redirect('camera_detail', camera.id)
#     else:
#         form = CamerasForm(instance=camera)
#     return render(request, 'update_camera.html', {'form':form})

class CameraUpdate(UpdateView):
    model = Cameras
    form_class = CamerasForm
    template_name = 'update_camera.html'
    success_url = reverse_lazy('cameras')



# def delete_camera(request, pk):
#     camera = get_object_or_404(Cameras, id=pk)
#     if request.method == "POST":
#         if 'yes' in request.POST:
#             camera.delete()
#             return redirect('cameras')
#         elif 'no' in request.POST:
#             return redirect('camera_detail', pk=pk)
#     return render(request, 'camera_del.html', {'camera': camera})

class CamerasDelete(DeleteView):
    model = Cameras
    template_name = 'camera_del.html'
    success_url = reverse_lazy('cameras')
