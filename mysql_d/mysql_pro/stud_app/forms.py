from django import forms
from .models import Register_model


class RegisterForm(forms.Form):
    # error_css_class = 'error'
    uid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'uid'
                                                                    }),
                                      required=True, max_length=30)
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}),
                                 required=True, max_length=30)
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email','type':'email'
                                                                    }),
                                 required=True, max_length=30)
    branch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'branch'
                                                           }),
                             required=True, max_length=30)
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password','type':'password'
                                                           }),
                             required=True, max_length=30)
    image = forms.FileField()



#uid validate
    def clean_uid(self):
        uid = self.cleaned_data.get('uid')
        is_exists = Register_model.objects.filter(uid=uid).exists()
        if is_exists:
            raise forms.ValidationError("User already exists with this Uid")
        return uid
    # def clean_input_file_name(self):
    #     input_file_name = self.cleaned_data['input_file_name']
    #     if input_file_name.isdigit():
    #         raise forms.ValidationError("digit should be not allowed in this name")
    #     return input_file_name

class LoginForm(forms.Form):
    uid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'uid'
                                                        }),
                          required=True, max_length=30)
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
                           required=True, max_length=30)

