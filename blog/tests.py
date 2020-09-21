from django.test import TestCase

from django.urls import reverse
class SnackTest(TestCase):

    def status_code(self,page_name):
        expected = 200
        url = reverse(page_name)
        response = self.client.get(url)
        actual = response.status_code # Request to the application
        self.assertEquals(expected, actual)

    def page_template(self,page_name):
        url = reverse(page_name)
        response = self.client.get(url)
        actual = page_name + '.html'
        self.assertTemplateUsed(response, actual)
        self.assertTemplateUsed(response,'base.html')
    
    def test_template_page1(self): 
        self.status_code('home')
    
    # def test_template_page2(self): 
    #     self.status_code('postdetail_view')
    
    def test_templet_home_page(self): 
        self.page_template('home')
    
    # def test_templet_about_page(self): 
    #     self.page_template('snacks-about')