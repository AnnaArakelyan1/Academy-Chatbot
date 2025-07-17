from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import spacy

class TextPreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.nlp = spacy.load('en_core_web_sm')  

    def preprocess(self, text):
        if not isinstance(text, str):
            return []
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token not in self.stop_words]
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return tokens

    def extract_entities(self, text):
        doc = self.nlp(text)
        return [ent.text for ent in doc.ents]

if __name__ == '__main__':
    tp = TextPreprocessor()
    user_input = "Where are the libraries located?"
    tokens = tp.preprocess(user_input)
    print(tokens)
