import nlp_processing as np
import resources as rs
import faqManager as fm

class AcademyChatBot:
    """
    Class: AcademyChatBot
    Handles user inputs, detects intent
    """

    def __init__(self):
        self.tp = np.TextPreprocessor()
        self.__resource = rs.Resources()
        self.__faq = fm.FAQ('data/faq.csv', self.tp)
        self.__greetings = ['hi', 'hey', 'hello', 'hey there']
        self.waiting_for_topic = False

    def process_user_request(self, req):
      if not req.strip():
         return "Please type something!"

      tokens = self.tp.preprocess(req)
      entities = self.tp.extract_entities(req)

      if self.waiting_for_topic:
         self.waiting_for_topic = False
         flag, response = self.__resource.get_resource_type(entities if entities else tokens)
         return response

      intents = self.get_intents(tokens)
      responses = []

      if 'greeting' in intents:
         responses.append('Hey there!')

      if 'faq' in intents:
         clean_input = ' '.join([t for t in tokens if t not in self.__greetings])
         faq_answer = self.__faq.find_answer(clean_input)
         if faq_answer:
               responses.append(faq_answer)

      if 'resource' in intents:
         flag, resource_answer = self.__resource.get_resource_type(entities if entities else tokens)
         if flag:
               responses.append(resource_answer)
         else:
               self.waiting_for_topic = True
               responses.append(resource_answer)

      if 'unknown' in intents and not responses:
         responses.append("I can't answer that question yet.")

      return '\n'.join(responses)


    def get_intents(self, tokens):
        intents = set()

        if any(token in self.__greetings for token in tokens):
            intents.add('greeting')

        if any(token in self.__faq.faq_keywords for token in tokens):
            intents.add('faq')

        if any(token in self.__resource.resource_keywords for token in tokens) or any(token in self.__resource.topics for token in tokens):
            intents.add('resource')

        if not intents:
            intents.add('unknown')

        return intents
