import nltk
# imports package used for tokenization & sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# this class will do the sentiment analysis magic
filename = "input.txt"
file = open(filename, "r", encoding="utf-8")
text = file.read()
# lines 5 - 7 open the input file, make the unicode utf-8, and store contents into string variable
# called text
text = text.replace("\n", " ")
# text files have newlines stored between each line; this can lead to issues with tokenization
# so good convention is to replace them
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
sentences = tokenizer.tokenize(text)
# 13-14 create the tokenizer and the tokenizer will turn the contents of text into a list
# composed of elements that have been "tokenized" (or divided into individual sentences)
sid = SentimentIntensityAnalyzer()
# object that gives sentiment score of inputted words or sentences
sentiment_score = 0
# stores the sentiment value of each sentence into a single sum
length = len(sentences)
# total number of sentences in the input file
pos_neg_neu = [0, 0, 0]
# list that keeps tally of [positive, negative, neutral] sentences
sentiment_list = []
# stores the polarity scores of each sentence


def get_nltk_sentiment(sentence):
    # function that finds and returns sentiment value of each individual sentence
    ss = sid.polarity_scores(sentence)
    # polarity_scores returns a float for sentiment strength based on the input text.
    # Positive values are positive valence, negative value are negative valence.
    sentiment_list.append(ss['compound'])
    return ss['compound']


def sentence_rating(num):
    # sentiment scores are values between (-1) & (1)
    # if a sentiment score is > (.5) it is likely to be a positive sentence
    # if a sentiment score is < (-.5) it is likely to be a negative sentence
    # if a sentiment score is between (.5) & (-.5) it is likely to be neutral
    if num > .5:
        pos_neg_neu[0] = pos_neg_neu[0] + 1
    elif num <= -.5:
        pos_neg_neu[1] = pos_neg_neu[1] + 1
    else:
        pos_neg_neu[2] = pos_neg_neu[2] + 1


def mostly():
    # finds if there are mostly positive, negative, or neutral scores
    max_value = max(pos_neg_neu)
    max_index = pos_neg_neu.index(max_value)
    if max_index == 0:
        return "Positive"
    elif max_index == 1:
        return "Negaitve"
    if max_index == 2:
        return "Neutral"


for sentence in sentences:
    num = get_nltk_sentiment(sentence)
    # stores sentiment score of a given sentence
    sentence_rating(num)
    # tallies if score is pos, neg, or neu into the list
    sentiment_score = sentiment_score + num
    # adds sentiment score into a sum

print("Sentiment Scores Are On A Range Between (-1) & (1) Where: \
     \n(-1)  - (-.5)\t Is Negative \
     \n(-.5) - (.5)\t Is Neutral \
     \n(.5)  - (1)\t Is Positive")
print("-----------------------------")
print("Individual Sentence Scores:\n", '\n'.join('{}: {}'.format(*k)
      for k in enumerate(sentiment_list)))
print("-----------------------------")
print("Sum of Scores:\t\t", str(sentiment_score))
# this takes the aggregate of all sentence scores
print("Average Score:\t\t", str(sentiment_score/length))
# this takes the average of all sentence scores
print("Text Is:\t\t", ((pos_neg_neu[0]/length)*100), "% Positive")
print("Text Is:\t\t", ((pos_neg_neu[1]/length)*100), "% Negative")
print("Text Is:\t\t", ((pos_neg_neu[2]/length)*100), "% Neutral")
print("Overall Sentiment:\t", mostly())
# this finds which sentiment (pos, neg, neu) is most present
