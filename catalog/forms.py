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

    def clean_name(self):
        worst_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data.get('name')

        for word in worst_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError("В имени продукта гадкое слово, придумайте что-то получше!")

        return cleaned_data

    def clean_description(self):
        worst_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data: str = self.cleaned_data.get('description')

        for word in worst_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(
                    f"В описании жуткое написано! Проверьте, нет ли там следующих слов: {', '.join(worst_words)}")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
