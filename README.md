#  ACM Research Coding Challenge (Fall 2021)

###### Language: Python 
###### Libraries/API/Packages: NLTK, Vader, 
###### Source of Information: NLTK Official Documentation at https://www.nltk.org/  

**Before You Use:** Download the nltk package using your CMD. You must issue the following commands in the Python Terminal:

        >>import nltk
        >>nltk.download('vader_lexicon')

**How To Use:**
    To test the program, simply run it on a chosen text editor. To change the body of text parsed and tested, make changes to the "input.txt" file. Once the program is run the output will appear in the terminal and show the results of Sentiment Analysis. 

**Why I Chose NLTK:**
    When set to complete this challenge, I was stuck between choosing the SpaCy Library and the NLTK Library. Both are excellent for any form of Natural Language Processing but having experience with SpaCy in the past I know that it is incredibly inefficient if one just wants to complete one specific task (in this case Sentiment Analysis) as the tokenizer completes a gamut of different tasks in one go. Technically the pipeline component TextBlob could be make things more efficient. Nevertheless, I wanted practice with NLTK so ultimately chose it. 

**How I Created The Program:**
    As explained by the official documentation, VADER ( Valence Aware Dictionary for Sentiment Reasoning) is the recommended model for Sentiment Analysis so I used the SentimentIntensityAnalyzer class from there. After importing both NLTK and the SentimentIntensityAnalyzer class from Vader, I opened the "input.txt" file and stored all the text into a string named text. I loaded in the "punkt" model for tokenization (splitting apart text into individual words or sentences) and stored the tokenized text into a list called sentences. From there I proceeded to find the sentiment score of each individual sentence using the polarity_scores(sentence) function. This runs through a provided sentence and finds its overall score on a range from (-1) to (1). According to the documentation the greater the number in either direction, the more sure Vader is that a provided sentence is negative or positive. Anything between the polarity values of (-1 to -.5) is considered negative, between (-.5 to .5) neutral, and between (.5 to 1) positive. From there once I found the individual scores of each sentence, I acknowledged there's no sure way to confirm if the text as a whole is positive, negative, or neutral so I set to providing as much information on the text as possible. I list:

        -   the sentiment score of each individual sentence 
        -   the summation of all listed scores
        -   the average score of the entire text
        -   what percent of the text is positive, negative, and neutral respectively 
        -   the final conclusion based off the previous point

**Score of "input.txt":**
    After running the program the score comes up as neutral, based off the number of sentences being neutral being greater than either those negative or positive. You'll notice that the first paragraph/excerpt is of a more negative tone (characters arguing) while the second is a bit more of a positive tone (character praising another) levelling out to a neutral tone between the two. Even with the more strikingly negative/positive sentences throughout the text, one can find that the number where it is neither positive nor negative dwarfs either of the two. For example, look at the sentence "Do you know, I had a dream an hour ago." Neither a program nor an individual reading can come to a conclusion on if such a sentence is positive or negative, so it makes most sense it is neutral. The text is littered with such sentences and because of it it confirms my beliefs that the text is neutral. 
