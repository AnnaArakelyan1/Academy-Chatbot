import pandas as pd
from sentence_transformers import SentenceTransformer, util

class FAQ:
    def __init__(self, filepath, textprocessor):
        self.__faqs = pd.read_csv(filepath)
        self.__tp = textprocessor
        self.__model = SentenceTransformer('all-MiniLM-L6-v2')
        self.__faq_embeddings = self.__model.encode(self.__faqs['question'].tolist(), convert_to_tensor=True)
        self.faq_keywords=['exam', 'schedule', 'date', 'library', 'policy', 'academy', 'open', 'time', 'study','final', 'test', 'tips', 'studytips']


    def __str__(self):
        return f"{self.__faqs}"

    @property
    def answers(self):
        return self.__faqs['answer']

    def find_answer(self, user_text):
      user_embedding = self.__model.encode(user_text, convert_to_tensor=True)
      similarities = util.pytorch_cos_sim(user_embedding, self.__faq_embeddings)[0]
      best_score = similarities.max().item()
      best_idx = similarities.argmax().item()
      if best_score < 0.4:
        return "Sorry, I couldn't find an answer to that question."
      return self.__faqs['answer'][best_idx]

    
    
