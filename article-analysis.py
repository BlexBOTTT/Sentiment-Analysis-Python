# https://www.youtube.com/watch?v=tXuvh5_Xyrw

# ntlk
# textblob
# newspaper3k

# Import necessary libraries for text analysis
from textblob import TextBlob
from newspaper import Article

# Define the URL of the web page you want to analyze
# https://en.wikipedia.org/wiki/Sadness
# https://en.wikipedia.org/wiki/Happiness
url = "https://www.gmanetwork.com/news/pinoyabroad/content/886198/israel-issues-missile-attack-warning-over-tel-aviv/story/?just_in"

# Create an Article object to download and analyze the web page's content
article = Article(url)

# Download the web page content
article.download()
# Parse the downloaded content to extract relevant information
article.parse()
# Perform natural language processing (NLP) on the article's content
article.nlp()

# Extract the summary of the article
text = article.summary

# Print the extracted summary
print(text)

# Create a TextBlob object using the extracted summary text
blob = TextBlob(text)

# Calculate the sentiment polarity of the text using the sentiment attribute, which gives a value between -1 and 1
sentiment = blob.sentiment.polarity

# Print the calculated sentiment polarity to the console
print(sentiment)
