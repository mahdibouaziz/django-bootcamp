from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['title','content']
    
    #To validate the title
    def clean_title(self):
        data=self.cleaned_data.get('title')

        if len(data)<4:
            raise forms.ValidationError("This is not long enough Title")
        return data
    
    #To validate the content
    def clean_content(self):
        data=self.cleaned_data.get('content')

        if len(data)<4:
            raise forms.ValidationError("This is not long enough Content")
        return data



#Define a Form class with a single field "your_name"
class NameForm (forms.Form):
    your_name=forms.CharField(label='Your name',max_length=100)
    #The label if human-friendly which will appear in the label when it's rendered
