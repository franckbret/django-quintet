from django.forms.widgets import Input

class QuintetInput(Input):
    def render(self, *args, **kwargs):
        rendered_string = super(QuintetInput, self).render(*args, **kwargs)

        return rendered_string
    
class TextInput(QuintetInput):
    input_type = 'text'

class EmailInput(QuintetInput):
    input_type = 'email'