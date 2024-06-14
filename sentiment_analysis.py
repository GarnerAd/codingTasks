# sentiment_analysis.py

import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Add the TextBlob sentiment analyzer to the pipeline
nlp.add_pipe('spacytextblob')

# Load the dataset
data = pd.read_csv('amazon_product_reviews.csv')

# Select the review text column
reviews_data = data['reviews.text']

# Remove missing values
clean_data = reviews_data.dropna()

# Function to preprocess text
def preprocess_text(text):
    """Preprocess text data by removing stopwords and non-alphabetic characters."""
    doc = nlp(text.lower())  # Convert to lowercase
    tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(tokens)

# Apply preprocessing to each review
clean_data = clean_data.apply(preprocess_text)

# Sentiment analysis function
def analyze_sentiment(review):
    """Analyze sentiment of a given review using spaCy with TextBlob."""
    doc = nlp(review)
    polarity = doc._.blob.polarity  # Sentiment polarity
    if polarity > 0:
        return 'positive', polarity
    elif polarity < 0:
        return 'negative', polarity
    else:
        return 'neutral', polarity

# Test the model on sample reviews
sample_reviews = clean_data.sample(5)

# Write a report summarizing the analysis
report_content = """
## Sentiment Analysis Report

### 5.1. Dataset Description
The dataset used is the Consumer Reviews of Amazon Products, containing product reviews.

### 5.2. Details of Preprocessing Steps
- Converted text to lowercase.
- Removed stopwords and non-alphabetic characters using spaCy.

### 5.3. Evaluation of Results
Sample reviews were analyzed using spaCy with TextBlob for sentiment analysis.

"""

for review in sample_reviews:
    sentiment, polarity = analyze_sentiment(review)
    report_content += f"Review: {review}\nSentiment: {sentiment}, Polarity: {polarity}\n\n"

# Additional insights into model's strengths and limitations
report_content += """
### 5.4. Insights into the Model's Strengths and Limitations
- Strengths: Integration of spaCy with TextBlob provides a straightforward way to analyze sentiment.
- Limitations: Accuracy can be influenced by the quality of text preprocessing and the underlying sentiment lexicon.

"""

# Save the report
with open('sentiment_analysis_report.txt', 'w') as f:
    f.write(report_content)

print("Sentiment analysis report generated successfully.")