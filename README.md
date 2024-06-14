# Sentiment Analysis Task

## Table of Contents
1. [Task Description](#task-description)
2. [Dataset](#dataset)
3. [Preprocessing](#preprocessing)
4. [Sentiment Analysis](#sentiment-analysis)
5. [Report](#report)

## Task Description
This coding task involves performing sentiment analysis on Amazon product reviews. The task demonstrates the integration of spaCy with TextBlob to analyze the sentiment of text data. Learning this aspect of coding is important because sentiment analysis is a common natural language processing (NLP) task used to gauge public opinion, monitor social media, and improve customer service.

## Dataset
The dataset used is the Consumer Reviews of Amazon Products, containing product reviews.

## Preprocessing
- Converted text to lowercase.
- Removed stopwords and non-alphabetic characters using spaCy.

## Sentiment Analysis
The sentiment of each review is analyzed using spaCy with TextBlob. The analysis yields the polarity of each review, classifying them as positive, negative, or neutral.

## Report
A report summarizing the sentiment analysis is generated, including insights into the model's strengths and limitations.

### Sentiment Analysis Report

#### 5.1. Dataset Description
The dataset used is the Consumer Reviews of Amazon Products, containing product reviews.

#### 5.2. Details of Preprocessing Steps
- Converted text to lowercase.
- Removed stopwords and non-alphabetic characters using spaCy.

#### 5.3. Evaluation of Results
Sample reviews were analyzed using spaCy with TextBlob for sentiment analysis.

#### 5.4. Insights into the Model's Strengths and Limitations
- Strengths: Integration of spaCy with TextBlob provides a straightforward way to analyze sentiment.
- Limitations: Accuracy can be influenced by the quality of text preprocessing and the underlying sentiment lexicon.

#### Installation Instructions
To run the provided script, you need to install several Python packages. Here's a list of the required packages and instructions on how to install them:

- pandas: For data manipulation and analysis.
- spacy: For natural language processing.
- spacytextblob: For sentiment analysis using TextBlob with spaCy.
- Additionally, you need to download the English language model for spaCy.

install pandas, spacy, and spacytextblob:
Open your terminal or command prompt and run the following command:

#### pip install pandas spacy spacytextblob

Download the spaCy English language model:
After installing spaCy, download the en_core_web_sm language model by running:

#### python -m spacy download en_core_web_sm

#### Summary of Commands
To summarize, here are the commands you need to run to install all the required packages and download the language model:

pip install pandas spacy spacytextblob
python -m spacy download en_core_web_sm

#### Package Descriptions
pandas: Used for data manipulation and analysis, providing data structures and operations for manipulating numerical tables and time series.
spacy: A library for advanced natural language processing in Python and Cython.
spacytextblob: An extension for spaCy that integrates TextBlob's sentiment analysis capabilities.
