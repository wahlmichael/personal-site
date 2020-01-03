from django import forms

class EmailForm(forms.Form):
    your_name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control px-4 py-3 my-3',
                'placeholder': 'Your Name'
            }
        ))
    your_email = forms.EmailField(
        max_length=254,
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control px-4 py-3 my-3',
                'placeholder': 'Your Email'
            }
        ))
    your_message = forms.CharField(
        max_length=2000,
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control px-4 py-3 my-3',
                'placeholder': 'Write a Message',
                }
            )
        )
