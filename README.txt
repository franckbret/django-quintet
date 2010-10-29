==============
Django Quintet
==============

Django quintet provides helpers to deal with html5 tags.

The first focus is on forms with the usage of placeholder.

More to come soon !

===============
Example with forms
===============

    from django.utils.translation import gettext_lazy as _
    from django import forms
    from django.template.loader import render_to_string
    from quintet.forms.widgets import *
    
    class ContactForm(forms.Form):
        sender = forms.EmailField(
            required=True,
            label = _('Sender E-mail address'),
            help_text = _('Please fill in a valid and reliable e-mail address.'),
            error_messages= {
                'required': _('An e-mail address is required'),
                'invalid': _('The syntax of the filled e-mail address is invalid')
                },
            widget=EmailInput(
                attrs={
                    'title': _('Please fill in a valid and reliable e-mail address.'),
                    'placeholder':'me@myself.com',
                    }
                )
             )
        message = forms.CharField(widget=forms.Textarea)
    



