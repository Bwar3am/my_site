from django import forms
from website.models  import Contact , Newsletter
from django.forms import ModelForm 
from captcha.fields import CaptchaField

class nameform(forms.Form):
    name=forms.CharField(max_length=120)
    email=forms.EmailField()
    subject=forms.CharField(max_length=230 ) 
    message=forms.CharField(widget=forms.Textarea)
    
    
 
class ContactForm(forms.ModelForm):
    
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = "__all__"
     
     
     
           
    def save(self,commit=True):
        self.instance.name= "unknown"
        return super().save(commit=commit)    

class NewsletterForm(forms.ModelForm):
     class Meta:
        model = Newsletter
        fields = '__all__'
        
    
   