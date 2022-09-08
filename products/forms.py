from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)
    image1 = forms.ImageField(label='',
                              required=False, widget=CustomClearableFileInput)
    image2 = forms.ImageField(label='',
                              required=False, widget=CustomClearableFileInput)
    price = forms.CharField(required=False)
    discount = forms.CharField(required=False)

    def clean_price(self, *args, **kwargs):
        """ Validate Price field  """

        price = self.cleaned_data.get("price")
        if len(price) == '' or len(price) < 1:
            raise forms.ValidationError("Price field is required.")
        if '@' in price or '-' in price or '|' in price or '*' in price:
            raise forms.ValidationError(
                "Price should not have special characters.")
        return price

    def clean_discount(self, *args, **kwargs):
        """ Validate Discount field  """

        discount = self.cleaned_data.get("discount")
        if len(discount) == '' or len(discount) < 1:
            raise forms.ValidationError("Discount field is required.")
        if '@' in discount or '-' in discount or '|' in discount or '*' in discount:
            raise forms.ValidationError(
                "Discount should not have special characters.")
        return discount

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """Rating and Review Form"""
    class Meta:
        """Form model and Fields"""
        model = Review
        fields = ['rating', 'review']
