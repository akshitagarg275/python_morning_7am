from django import forms

class VideoForm(forms.Form):
    videoname = forms.CharField(max_length=70 ,
    widget=forms.TextInput(attrs={
        "class" : "form-control",
        "placeholder" : "name",
        "id" : "inputName"
    }))



    videodesc = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows':'5',
        'id':'comment',
        'placeholder':'Comment'
    }))