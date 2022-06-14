from django.forms import ModelForm, Textarea
from .models import foodProducts


class addItemForm(ModelForm):
    class Meta:
        model = foodProducts
        fields = {'name', 'description'}
        widgets = {
            'description': Textarea(attrs={'cols': 100}),

        }