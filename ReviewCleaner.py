import csv
import re
from spellchecker import SpellChecker

def save_reviews_to_file(reviews, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for review in reviews:
            file.write(review + '\n')


def clean_text(text):
    text = text.strip().lower()
    
    # Remove punctuation using regular expressions
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Batch process words
    batch_size = 100  # You can adjust this based on your data and performance
    corrected_words = []
    spell = SpellChecker()
    for i in range(0, len(words), batch_size):
        batch = words[i:i + batch_size]
        batch_corrected = spell.correction(batch)
        corrected_words.extend(batch_corrected)
    
    text = ' '.join(corrected_words)
    
    # ... other preprocessing steps
    
    return text

def main(csv_file_path):
    positive_reviews = []
    negative_reviews = []
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        for row in csvreader:
            row_elements = row[0].split(',')
            if 'Positive' in row_elements[2]:
                positive_reviews.append(clean_text(row_elements[3]))
            elif 'Negative' in row_elements[2]:
                negative_reviews.append(clean_text(row_elements[3]))

    save_reviews_to_file(positive_reviews, 'positive.txt')
    save_reviews_to_file(negative_reviews, 'negative.txt')

if __name__ == "__main__":
    csv_file_path = "twitter_training.csv"
    main(csv_file_path)
