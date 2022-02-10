from django.forms import ModelForm
from .models import ContactMe
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactMeForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = ContactMe
        fields = '__all__'
