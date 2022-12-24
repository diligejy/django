from django.test import TestCase
from .models import Post 
from http import HTTPStatus


# Create your tests here.
class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()
        
        self.assertEqual(posts, 0)
        
    def test_string_rep_of_objects(self):
        post = Post.objects.create(
            title="Test Post",
            body="Test Body"
        )
        
        self.assertEqual(str(post), post.title)
    
class HomepageTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(
            title="sample title 1",
            body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet vulputate neque. Integer lacus elit, lacinia in arcu a, ornare fringilla erat. Suspendisse venenatis urna nec sem ultricies dapibus. Integer nec lacinia massa, feugiat aliquet turpis. Sed luctus erat vel lectus luctus, ornare volutpat est pharetra. Curabitur porta scelerisque enim, in dapibus erat molestie sit amet. Sed ultricies vulputate porta. Etiam vel libero eu nulla consequat condimentum in non quam. Praesent justo dolor, convallis sit amet ante in, lacinia elementum dui. Praesent in diam in tellus mollis aliquet. In vitae dui dui. Quisque lacinia metus eu tristique molestie."
        )
        
        Post.objects.create(
            title="sample title 2",
            body="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet vulputate neque. Integer lacus elit, lacinia in arcu a, ornare fringilla erat. Suspendisse venenatis urna nec sem ultricies dapibus. Integer nec lacinia massa, feugiat aliquet turpis. Sed luctus erat vel lectus luctus, ornare volutpat est pharetra. Curabitur porta scelerisque enim, in dapibus erat molestie sit amet. Sed ultricies vulputate porta. Etiam vel libero eu nulla consequat condimentum in non quam. Praesent justo dolor, convallis sit amet ante in, lacinia elementum dui. Praesent in diam in tellus mollis aliquet. In vitae dui dui. Quisque lacinia metus eu tristique molestie."
        )
    
    def test_homepage_returns_correct_response(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'posts/index.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)