from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class Messagepagetests(SimpleTestCase):
    def test_url_existance(self):
        response = self.client.get("/message/")
        self.assertEqual(response.status_code,200)


    def test_url_name_availabe(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code,200)
    
    def test_template_name(self):
        response = self.client.get(reverse('message'))
        self.assertTemplateUsed(response,'home.html')
    
    def test_template_content(self):
        response = self.client.get("/message/")
        self.assertContains(response,'<h1>helloooooo world</h1>')