from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack

# Used ChatGPT to replace instances of Thing and replaced with Snack
class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.snack = Snack.objects.create(title="paper", purchaser=self.user, description="crunchy")

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "paper")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "paper")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(self.snack.description, "crunchy")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "paper")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "carpet",
                "description": "soft but dirty",
                "purchaser": self.user.id,
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "carpet")

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "clean carpet", "description": "soft and clean", "purchaser": self.user.id},
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"), target_status_code=200)

    def test_snack_update_bad_url(self):
        response = self.client.post(
            reverse("snack_update", args="9"),
            {"title": "clean carpet", "description": "soft and clean", "purchaser": self.user.id},
        )

        self.assertEqual(response.status_code, 404)

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)

    def test_model(self):
        snack = Snack.objects.create(title="carpet", description="soft and clean", purchaser=self.user)
        self.assertEqual(snack.title, "carpet")
