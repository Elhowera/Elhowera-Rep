
import nltk

from nltk.corpus import stopwords
nltk.download('stopwords')

with open('paragraphs.txt', 'r') as file:
    text = file.read()
words = nltk.word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
filtered_text = ' '.join(filtered_words)

from collections import Counter

word_freq = Counter(filtered_words)

for word, freq in word_freq.items():

    print(f"{word}: {freq}")