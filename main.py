import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# for sentiment analysis
nltk.download('punkt')

url = 'https://viterbischool.usc.edu/news/2019/05/robotics-and-american-sign-language/'
# url = 'https://www.proquest.com/docview/216442336/fulltext/421B54203E9344D4PQ/1?accountid=25364'
article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Author: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

# analysis
# analysis = TextBlob(article.text) # whole article text
# print(analysis.polarity)
# print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
#





