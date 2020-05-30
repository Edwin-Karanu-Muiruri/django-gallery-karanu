from django.test import TestCase
from .models import Category,Location,Image
from unittest import skip


class CategoryTestClass(TestCase):
    '''
    Category class tests
    '''
    def setUp(self):
        self.animals = Category(name = "animals")
        self.animals.save_category()
    
    def tearDown(self):
        Category.objects.all().delete()

    def test_category_instance(self):
        self.assertTrue(isinstance(self.animals, Category))

    def test_save_category_method(self):
        self.animals.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)> 0)

    def test_delete_category(self):
        categories1 = Category.objects.all()
        self.assertEqual(len(categories1),1)
        self.animals.delete_category()
        categories2 = Category.objects.all()
        self.assertEqual(len(categories2),0)

    
    def test_update_category(self):
        self.animals.save_category()
        self.animals.update_category(self.animals.id,'wildlife')
        new_update = Category.objects.get(name = "wildlife")
        self.assertEqual(new_update.name, 'wildlife')


class LocationTestClass(TestCase):
    '''
    Location class tests
    '''
    def setUp(self):
        self.nairobi = Location(name = "nairobi")
        self.nairobi.save_location()
    
    def tearDown(self):
        Location.objects.all().delete()

    def test_location_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))

    def test_save_location_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)> 0)

    def test_delete_location(self):
        self.nairobi.save_location()
        locations1= Location.objects.all()
        self.assertEqual(len(locations1),1)
        self.nairobi.delete_location()
        locations2= Location.objects.all()
        self.assertEqual(len(locations2),0)

    def test_update_location(self):
        self.nairobi.save_location()
        self.nairobi.update_location(self.nairobi.id,'kiambu')
        new_update = Location.objects.get(name = "kiambu")
        self.assertEqual(new_update.name, 'kiambu')

    def test_display_locations(self):
        self.nairobi.save_location()
        self.assertEqual(len(Location.display_all_locations()), 1)


class ImageTestClass(TestCase):
    '''
    Image class tests
    '''
    def setUp(self):
        self.animals = Category( name= "animals")
        self.nairobi = Location(name = "nairobi")
        self.snake = Image(image = "image", name ='snake', description = 'green', category= self.animals, location= self.nairobi)

        self.animals.save_category()
        self.nairobi.save_location()
        self.snake.save_image()

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_image_instance(self):
        self.assertTrue(isinstance(self.snake, Image))


    def test_save_image_method(self):
        self.snake.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_display_images(self):
        self.snake.save_image()
        self.assertEqual(len(Image.display_all_images()), 1)

    def test_delete_images(self):
        self.snake.save_image()
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.snake.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    def test_update_image_description(self):
        self.snake.save_image()
        self.snake.update_image_description(self.flower.id,'poisonous')
        new_update = Image.objects.get(name = "snake")
        self.assertEqual(new_update.description, 'poisonous')


    def test_get_image_by_id(self):
        self.snake.save_image()
        image = Image.get_image_by_id(self.snake.id)
        self.assertEqual(image.name, self.snake.name)

    def test_search_image(self):
        self.animals.save_category()
        self.snake.save_image()
        images = Image.search_image("animals")
        self.assertTrue(len(images) > 0)

    
    def test_search_location(self):
        self.nairobi.save_location()
        self.snake.save_image()
        images = Image.filter_by_location("nairobi")
        self.assertTrue(len(images) > 0)