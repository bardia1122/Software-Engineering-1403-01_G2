from django.test import TestCase

# test for models
from .models import TextOptimization

class TextOptimizationModelTest(TestCase):

    def test_model_creation(self):
        # Create a TextOptimization object
        text_optimization = TextOptimization.objects.create(
            input_text="This is an example text.",
            optimized_text="This is an improved version of the text."
        )

        # Test if the model is created with correct values
        self.assertEqual(text_optimization.input_text, "This is an example text.")
        self.assertEqual(text_optimization.optimized_text, "This is an improved version of the text.")
    
    def test_str_method(self):
        # Test if the string representation works as expected
        text_optimization = TextOptimization.objects.create(
            input_text="Some text",
            optimized_text="Optimized text"
        )
        # Since created_at is auto_now_add, it should be in the format "Optimization on ..."
        self.assertTrue(text_optimization.__str__().startswith("Optimization on"))

# test for logic
from .logic import process_input

class LogicTest(TestCase):

    def test_process_input(self):
        input_text = "Some text with delimiters)"
        optimized_text = process_input(input_text)
        self.assertEqual(optimized_text, "Some text with delimiters()")

    def test_fix_delimiters(self):
        # Test case where delimiters are not correctly matched
        input_text = "This is (a test with mismatched brackets"
        fixed_text = process_input(input_text)  # This will use fix_delimiters internally
        self.assertEqual(fixed_text, "This is (a test with mismatched brackets)")

# test for views
from django.urls import reverse
class ViewsTest(TestCase):

    def test_optimize_text_post(self):
        url = reverse('optimize_text')  # Replace with the actual URL name for the view
        response = self.client.post(url, {'text': 'Some example text)'})
        
        # Test that the response is a success and the optimized text is in the response
        self.assertEqual(response.status_code, 200)
        self.assertIn('optimized_text', response.context)
    
    def test_optimize_text_get(self):
        url = reverse('optimize_text')  # Replace with the actual URL name for the view
        response = self.client.get(url)
        
        # Test that the response is a success and the correct template is used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'group3/optimize.html')

# test for TextMistakesAPIView
from rest_framework.test import APIClient
from rest_framework import status

class TextMistakesAPIViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()  # Create an API client to make requests
    
    def test_post_text_mistakes(self):
        url = reverse('text_mistakes')  # Replace with the actual URL name for the view
        data = {'text': 'This is some test text.'}
        response = self.client.post(url, data, format='json')
        
        # Check if the API response is correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('suggestions', response.data)
    
    def test_post_text_mistakes_no_text(self):
        url = reverse('text_mistakes')  # Replace with the actual URL name for the view
        data = {}  # Empty data
        response = self.client.post(url, data, format='json')
        
        # Check if the API returns an error for missing text
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

# test for parse
from .parse import generate_suggestions

class ParseTest(TestCase):

    def test_generate_suggestions(self):
        input_text = "من میتوانم    یا می توانم   ."
        output_text = "من می‌توانم یا می‌توانم."
        
        suggestions = generate_suggestions(input_text, output_text)
        
        # Check if the function generates the correct suggestions
        self.assertGreater(len(suggestions), 0)
        self.assertEqual(suggestions[0]['original'], 'می توانم')
        self.assertEqual(suggestions[0]['suggestion'], 'می‌توانم')
    
    def test_empty_suggestions(self):
        input_text = "Some text"
        output_text = "Some text"
        
        suggestions = generate_suggestions(input_text, output_text)
        
        # No changes, so there should be no suggestions
        self.assertEqual(len(suggestions), 0)

# test for database
from .database import query,secret

class DatabaseTest(TestCase):

    def test_save_texts(self):
        mydb = query.create_db_connection(secret.DB_HOST, secret.DB_PORT, secret.DB_USER, secret.DB_PASSWORD, secret.DB_NAME)
        query.save_texts(mydb, "this is a teest", None, "this is a test")
        #self.assertTrue(TextOptimization.objects.exists())