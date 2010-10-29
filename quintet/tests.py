"""
Test for quintet widget rendering. 
"""

from django.test import TestCase
from django.forms.fields import *
from quintet.forms.widgets import *

class QuintetInputTest(TestCase):    
    # Test widgets field types
    def testRenderTextInput(self):
        i = TextInput()
        r = i.render('title','')
        self.assertEqual(r, u'<input type="text" name="title" />')
        
    def testRenderSearchInput(self):
        i = SearchInput()
        r = i.render('find','')
        self.assertEqual(r, u'<input type="search" name="find" />')

    def testRenderEmailInput(self):
        i = EmailInput()
        r = i.render('email','')
        self.assertEqual(r, u'<input type="email" name="email" />')
        
    def testRenderUrlInput(self):
        i = UrlInput()
        r = i.render('website','')
        self.assertEqual(r, u'<input type="url" name="website" />')
        
    def testRenderNumberInput(self):
        i = NumberInput()
        r = i.render('howmuch','')
        self.assertEqual(r, u'<input type="number" name="howmuch" />')
        
    def testRenderNumberInput(self):
        i = RangeInput()
        r = i.render('width','')
        self.assertEqual(r, u'<input type="range" name="width" />')
        
    def testRenderTelephoneInput(self):
        i = TelephoneInput()
        r = i.render('tel','')
        self.assertEqual(r, u'<input type="telephone" name="tel" />')
        

