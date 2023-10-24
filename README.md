# Sentiment Analysis with TextBlob, Newspaper3k, and NLTK

This repository demonstrates how to perform sentiment analysis using the TextBlob library for both web articles and text files. Sentiment analysis is a technique that quantifies the sentiment or emotional tone in a piece of text, allowing you to determine whether the text expresses positive, negative, or neutral sentiment.

## Prerequisites

Before using this code, make sure you have the following Python packages installed:

- `textblob`
- `newspaper3k`
- `nltk`

You can install them using `pip`:

```bash
pip install textblob newspaper3k nltk
```

## Analyzing the Sentiment of a Web Article

To analyze the sentiment of a web article, follow these steps:

1. Clone this repository or download the `article-analysis.py` script.

2. Edit the `url` variable in the script to specify the URL of the web article you want to analyze. For example:

   ```python
   url = "https://www.example.com/article"
   ```

3. Run the `article-analysis.py` script using Python. It will download and parse the article, perform natural language processing (NLP), extract a summary, and calculate the sentiment polarity. The sentiment polarity value will be printed to the console on a scale from -1 (negative) to 1 (positive).

## Analyzing the Sentiment of a Text File

To analyze the sentiment of a text file, follow these steps:

1. Clone this repository or download the `text-analysis.py` script.

2. Create a text file (e.g., `sample-text.txt`) containing the text you want to analyze. Make sure the file is in the same directory as the script.

3. Run the `text-analysis.py` script using Python. It will read the text from the file, create a TextBlob object, and calculate the sentiment polarity. The sentiment polarity value will be printed to the console on a scale from -1 (negative) to 1 (positive).

## Example Results

- For the article analysis, you will see a sentiment polarity value printed to the console, indicating the overall sentiment expressed in the article.
- For the text file analysis, you will see a sentiment polarity value printed to the console, indicating the sentiment of the text in the file.

Feel free to use these scripts and adapt them to analyze sentiment in your own text data.

For more information on the TextBlob, Newspaper3k, and NLTK libraries, please refer to their official documentation and resources.

## CREDITS

- [Simple Sentiment Text Analysis in Python](https://www.youtube.com/watch?v=tXuvh5_Xyrw)
  - Basis for the tutorial
- [ChatGPT](https://openai.com/chatgpt)
  - For advanced AI-assisted troubleshooting/debugging if out of my knowledge range
- [Natural Language ToolKit (NLTK)](https://www.nltk.org/index.html)
  - NLTK is a Python library for text analysis and processing.
- [TextBlob](https://textblob.readthedocs.io/en/dev/)
  - TextBlob is a simple Python library for text analysis, including sentiment analysis.
- [Newspaper/Newspaper3k](https://newspaper.readthedocs.io/en/latest/)
  - Newspaper is a Python library for web article extraction and analysis.
