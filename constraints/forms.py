from django.forms import ModelForm
from constraints.models import *

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ["symbol", "name"]
        
