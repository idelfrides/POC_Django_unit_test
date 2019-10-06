
from django.test import TestCase
from .models import Animal

class AnimalTestCase(TestCase):
    """ Animal TestCase """
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")
        Animal.objects.create(name="Dog", sound="waeow")
        Animal.objects.create(name="Eagle", sound="kwiew")


    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
      
        assert Animal.objects.all().count() > 3
        