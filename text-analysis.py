# Import the TextBlob library to perform sentiment analysis
from textblob import TextBlob

# Open a text file ('sample-text.txt') in read mode and assign it to the 'f' variable
with open('sample-text.txt', 'r') as f:
    # Read the contents of the file and store them in the 'text' variable
    text = f.read()

# Create a TextBlob object 'blob' using the text from the file
blob = TextBlob(text)

# Analyze the sentiment of the text using the sentiment attribute, which calculates polarity (-1 to 1)
sentiment = blob.sentiment.polarity

# Print the calculated sentiment polarity to the console
print(sentiment)
