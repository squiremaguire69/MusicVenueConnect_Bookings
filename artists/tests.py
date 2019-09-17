from django.test import TestCase
from .models import Artist

# Create your tests here.
class ArtistTests(TestCase):
    
    
    def test_str(self):
        test_artist_name = Artist(artist_name="Artist")
        self.assertEqual(str(test_artist_name), 'Artist')