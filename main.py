import csv
import sys
from nltk.sentiment import SentimentIntensityAnalyzer

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

if __name__ == '__main__':

    sia = SentimentIntensityAnalyzer()
    list_sentiments = []

    with open('GitterCom.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row['message'])
            list_sentiments.append(sia.polarity_scores(row['message']))

    #for sentiment in list_sentiments:
    #    print(sentiment)





