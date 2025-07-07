from django import forms
from.models import Cameras
class CamerasForm(forms.ModelForm):
    class Meta:
        model = Cameras
        fields = ['name', 'brand', 'resolution', 'lens', 'night_vision', 'connectivity', 'power', 'features', 'price','image']