import pandas as pd

class Resources:

    def __init__(self, filepath='data/resource.csv'):
        self.__resources = pd.read_csv(filepath)
        self.__resource_keywords = ['resource', 'link', 'material', 'document', 'file', 'book', 'pdf','tutorial']
        self.topics = [topic.lower() for topic in self.__resources['topic']]

    def __str__(self):
        return f"{self.__resources}"


    def get_resource_type(self, user_tokens):
      topic_tokens = [t for t in user_tokens if t not in self.__resource_keywords]
      matches = []

      for token in topic_tokens:
          matching = self.__resources[self.__resources['topic'].str.lower().str.contains(token.lower())]
          if not matching.empty:
              matches.extend(matching.itertuples(index=False))

      if matches:
          links = '\n'.join([f"• {row.topic}: {row.link}" for row in matches])
          return True, f"Here are the resources I found:\n{links}"

      return False, "Sure! What topic are you interested in?"

