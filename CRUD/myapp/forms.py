from django.forms import ModelForm
from .models import img

class imgForm(ModelForm):
    
    class Meta:
        model = img
        fields = '__all__'
