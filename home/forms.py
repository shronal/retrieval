from django import forms
from .models import LostItem, FoundItem


class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = '__all__'  # or specify fields explicitly

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = '__all__'
        
        # fields = [
        #     'name', 'email', 'phone', 
        #     'item_name', 'item_type', 
        #     'color', 'brand', 'date_lost', 
        #     'location_lost', 'details', 'photo'
        # ]
