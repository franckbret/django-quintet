from django.forms.widgets import Input

class QuintetInput(Input):
    def render(self, *args, **kwargs):
        rendered_string = super(QuintetInput, self).render(*args, **kwargs)

        return rendered_string
    
class TextInput(QuintetInput):
    input_type = 'text'
    
class SearchInput(QuintetInput):
    input_type = 'search'

class EmailInput(QuintetInput):
    input_type = 'email'
    
class UrlInput(QuintetInput):
    input_type = 'url'
    
class NumberInput(QuintetInput):
    input_type = 'number'
    
class RangeInput(QuintetInput):
    input_type = 'range'
    
class TelephoneInput(QuintetInput):
    input_type = 'telephone'
    

    

    
