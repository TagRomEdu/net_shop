from django import forms

from catalog.models import Blog, Product


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('name', 'text', 'preview', 'is_published')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'photo', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
