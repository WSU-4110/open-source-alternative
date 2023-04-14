from django.test import TestCase
from django.urls import reverse

class NavigationBarTest(TestCase):
    def test_homepage(self):
        response = self.client.get(reverse('software_index'))
        self.assertEqual(response.status_code, 200)
    def test_aboutpage(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    def test_softwaresubmission(self):
        response = self.client.get(reverse('software_submit'))
        self.assertEqual(response.status_code, 200)
    def test_reportbugs(self):
        response = self.client.get(reverse('bug_submit'))
        self.assertEqual(response.status_code, 200)
    def test_aboutpage_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, "About FOSS")
class DarkMode(TestCase):
    def test_darkmode(self):
        response = self.client.get(reverse('software_index'))
        self.assertEqual(response.status_code, 200)