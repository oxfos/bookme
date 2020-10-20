from django.test import TestCase
from django.contrib.auth.models import User
from account.models import Profile


class Images_urls_test(TestCase):

    @classmethod
    def setUpTestData(self):
        # Set up data for the whole TestCase
        self.olmo = User.objects.create_user(username='username', password='password')
        self.olmo_prof = Profile.objects.create(user=self.olmo)

    def test_rankings_url(self):
        self.client.login(username='username', password='password')
        response = self.client.get('/ranking/')
        self.assertTemplateUsed(response, 'images/image/ranking.html')
        # self.assertEqual(response.context['most_viewed'], 'most_viewed') there are no images!