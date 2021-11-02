from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Project

class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title = "test",
            body= "a small test"
            )

    def test_string(self):
        project = Project(title="a test")
        self.assertEqual(str(project),project.title)

    def test_project_content(self):
        self.assertEqual(f'{self.project.title}','test')
        self.assertEqual(f'{self.project.body}','a small test')
    
    def test_project_home_view(self):
        resp = self.client.get(reverse('project_home'))
        self.assertEqual(resp.status_code,200)
        self.assertContains(resp, 'test')
        self.assertTemplateUsed(resp, 'projects.html')

    def test_project_detail_view(self):
        resp = self.client.get('/myportfolio/1/')
        self.assertEqual(resp.status_code,200)
        self.assertContains(resp, 'a small test')
        self.assertTemplateUsed(resp, 'projectdetail.html')