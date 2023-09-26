from django.forms import ModelForm
from main.models import Pesanan

class PesananForm(ModelForm):
    class Meta:
        model = Pesanan
        fields = ["name", "skinType","amount","payment"]

