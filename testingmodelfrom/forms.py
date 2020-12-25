from django import forms

from .models import Author,Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name','title','birth_date']

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','authors']


TITLE_CHOICES=[
    ('MR','Mr.'),
    ('MRS','Mrs.'),
    ('MS','Ms.'),
]

class AuthorFormV2 (forms.Form):
    name=forms.CharField(max_length=100)
    title=forms.CharField(max_length=3,widget=forms.Select(choices=TITLE_CHOICES))
    birth_date=forms.DateField(required=False)

class BookFormV2(forms.Form):
    name=forms.CharField(max_length=100)
    authors=forms.ModelMultipleChoiceField(queryset=Author.objects.all())




