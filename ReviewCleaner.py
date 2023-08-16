import csv

def save_reviews_to_file(reviews, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for review in reviews:
            file.write(review + '\n')

def main(csv_file_path):
    positive_reviews = []
    negative_reviews = []

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        for row in csvreader:
            row_elements = row[0].split(',')
            if 'Positive' in row_elements[2]:
                positive_reviews.append(row_elements[3])
            elif 'Negative' in row_elements[2]:
                negative_reviews.append(row_elements[3])

    save_reviews_to_file(positive_reviews, 'pos.txt')
    save_reviews_to_file(negative_reviews, 'neg.txt')

if __name__ == "__main__":
    csv_file_path = "twitter_training.csv"
    main(csv_file_path)
