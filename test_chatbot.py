import unittest
from chatbot import AcademyChatBot
from nlp_processing import TextPreprocessor
from resources import Resources
from faqManager import FAQ

class TestTextPreprocessor(unittest.TestCase):

    def setUp(self):
        self.tp = TextPreprocessor()

    def test_preprocess(self):
        text = "What's the exam schedule?"
        tokens = self.tp.preprocess(text)
        self.assertIn('exam', tokens)
        self.assertNotIn('the', tokens)

    def test_entity_extraction(self):
        text = "The deadline is July 20, 2025"
        entities = self.tp.extract_entities(text)
        self.assertTrue(any("2025" in e for e in entities))


class TestFAQ(unittest.TestCase):

    def setUp(self):
        self.tp = TextPreprocessor()
        self.faq = FAQ('data/faq.csv', self.tp)

    def test_answer_found(self):
        question = "When is the exam?"
        answer = self.faq.find_answer(question)
        self.assertIsInstance(answer, str)
        self.assertNotIn("couldn't find", answer.lower())

    def test_no_answer(self):
        question = "Tell me about yor day."
        answer = self.faq.find_answer(question)
        self.assertIn("couldn't find", answer.lower())

 
class TestResources(unittest.TestCase):

    def setUp(self):
        self.res = Resources('data/resource.csv')

    def test_resource_found(self):
        tokens = ['python', 'book']
        flag, response = self.res.get_resource_type(tokens)
        self.assertTrue(flag)
        self.assertIn("resources", response.lower())

    def test_resource_not_found(self):
        tokens = ['alien', 'manual']
        flag, response = self.res.get_resource_type(tokens)
        self.assertFalse(flag)
        self.assertIn("what topic", response.lower())


class TestChatBot(unittest.TestCase):

    def setUp(self):
        self.bot = AcademyChatBot()

    def test_greeting(self):
        response = self.bot.process_user_request("hello")
        self.assertIn("hey", response.lower())

    def test_faq_flow(self):
        response = self.bot.process_user_request("When is the exam?")
        self.assertIsInstance(response, str)

    def test_resource_flow(self):
        response = self.bot.process_user_request("I want python books")
        self.assertIn("resources", response.lower())


if __name__ == '__main__':
    unittest.main()
