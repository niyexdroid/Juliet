from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    title = forms.CharField(label='Title',
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Your Title"
                                    })
                            )
    # email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "Placeholder": "your Description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "row": 20,
                "cols": 100
            }
        )
    )
    price = forms.DecimalField(initial=0.00)
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError("This is not valid title")
    #     if not "." in title:
    #         raise forms.ValidationError("This is not valid title")
    #     return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("title")
    #     if not email.endswith("edu") in email:
    #         raise forms.ValidationError("This is not valid email")
    #     if not "NEWS" in email:
    #         raise forms.ValidationError("This is not valid email")
    #     return email
    
class RawProductForm(forms.Form):
    title       = forms.CharField(label='', 
                    widget=forms.TextInput(
                    attrs={
                        "placeholder": "Your Title"
                    })
                )

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not valid title")
        if not "." in title:
            raise forms.ValidationError("This is not valid title")
        return title

    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "Placeholder": "your Description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "row": 20,
                                    "cols": 100
                                }
                            )         
                        ) 
    price = forms.DecimalField(initial=0.00)
