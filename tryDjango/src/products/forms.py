from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title= forms.CharField(label='',
                           widget=forms.TextInput(
                               attrs={
                                  
                               }
                           ))
    # email=forms.EmailField()
    description=forms.CharField(required=False,
                                widget=forms.Textarea(
                                        attrs={
                                                    "placeholder":"description",
                                                    "class":"new-class-name two",
                                                    "id":"my-id-for-textarea",
                                                    "rows":20,
                                                    "columns":20
                                              }
                                    ))
    price=forms.DecimalField(initial='99.65')

    class Meta:
        model = Product
        fields=[
            'title',
            'description',
            'price'
        ]
    def clean_title(self,*args,**kwargs):
        title=self.cleaned_data.get("title")   # djamgo cleans up the form itself and activates get title
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title ")
        else:
            return title
    # def clean_email(self,*args,**kwargs):
    #     email=self.cleaned_data.get("email")   # djamgo cleans up the form itself and activates get title
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not a valid email ")
    #     else:
    #         return email


class RawProductForm(forms.Form):
    title= forms.CharField(label='',
                           widget=forms.TextInput(
                               attrs={
                                   "placeholder":"writeplzzzzzz"
                               }
                           ))
    description=forms.CharField(required=False,
                                widget=forms.Textarea(
                                        attrs={
                                                    "placeholder":"description",
                                                    "class":"new-class-name two",
                                                    "id":"my-id-for-textarea",
                                                    "rows":20,
                                                    "columns":20
                                              }
                                    ))
    price=forms.DecimalField(initial='99.65')
