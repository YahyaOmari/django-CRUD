from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.

class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Yahya",
             email="yahya@test.com", 
             password="test123"
        )

        self.snack = Snack.objects.create(
            title="Asac", purchaser=self.user, description="Student" 
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Asac")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "Asac")
        self.assertEqual(f"{self.snack.purchaser}", "Yahya")
        self.assertEqual(self.snack.description,"Student")


    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Asac")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: Yahya")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "Student",
                "purchaser": self.user.id,
                "description": "Asac",
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "Student")



    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated title","purchaser":self.user.id,"description":"New description"}
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)