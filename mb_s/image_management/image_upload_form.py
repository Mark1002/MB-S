from django import forms


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField(label='image', widget=forms.ClearableFileInput(attrs={'multiple': True}))
