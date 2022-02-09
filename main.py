import csv
import sys
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

maxInt = sys.maxsize

while True:

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
            #print(row['message']) This line is to print out all the messages.
            list_sentiments.append(sia.polarity_scores(row['message']))

    df = pd.read_csv('GitterCom.csv')
    df['sentiments'] = list_sentiments
    print(df)

    df.to_csv("GitterCom.csv")






