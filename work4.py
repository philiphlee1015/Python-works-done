##  This assignment requires the data file 'airline_tweets.csv'.  This file
##  contains records of over 14000 tweets and associated information related
##  to a number of airlines.  You should be able to read this file in using
##  the usual pandas methods.

##  Note: Questions 1-9 should be done without the use of loops.  
##        Questions 10-13 can be done with loops.

## 1.  Determine the number of tweets for each airline, indicated by the
##     name in the 'airline' column of the data set.  Give the airline 
##     name and number of tweets in table form.
import pandas as pd         ##loads pandas
tweet = pd.read_csv('airline_tweets.csv') ##saves csv data as tweet   
twit=tweet.groupby(['airline'])     ##uses groupby function to aggregate the data by column 'airline'
counts=twit.count()         ##uses .count() to count the number of data that corresponds to each airline
counts.loc[:,'Unnamed: 0']      ##makes the table
"""
1

airline
American          2759                     ##number in the right column indicates the number of tweets for each airline
JetBlue           2222
Southwest         2420
US Airways        2913
United            3822
Virgin America     504
"""


## 2.  For each airlines tweets, determine the percentage that are positive,
##     based on the classification in 'airline_sentiment'.  Give a table of
##     airline name and percentage, sorted from largest percentage to smallest.
positive = tweet[tweet['airline_sentiment']=='positive']     ##isolates the data by positive reviews
tweetpositive= positive['airline_sentiment'].groupby(tweet['airline'])       ##aggregate the isolated data based on the airline
tweetrating=tweet['airline_sentiment'].groupby(tweet['airline'])   ##aggregate the whole data based on airline
asdf=tweetpositive.count()           ##counts how many positive reviews are there for each airline
assdf=tweetrating.count()        ##counts how many reviews are there for each airline
percent=100*asdf/assdf            ##divides the number of positive reviews by the total number and multiply it by 100 to get the percentage of reviews that are positive
percent.sort_values(ascending=False)    ##sorts the percent from largest to smallest

"""
2

airline
Virgin America    30.158730          ##number in the right is the percent of positive tweets for each airline
JetBlue           24.482448
Southwest         23.553719
United            12.872841
American          12.178325
US Airways         9.234466
"""



## 3.  List all user names (in the 'name' column) with at least 20 tweets
##     along with the number of tweets for each.  Give the results in table
##     form sorted from most to least.
toomany = tweet.groupby(['name'])        ##aggregates the data by name
yikes=toomany.count()        ##counts the number of rows that are associated with each name
why=yikes.loc[yikes['Unnamed: 0']>=20].sort_values('Unnamed: 0',ascending=False)    ##finds the name with count at least 20 and sorts the table by largest to smallest
why.loc[:,'Unnamed: 0'] ##makes the table
"""
3

name
JetBlueNews        63             ##number in the right is number of tweets for each name
kbosspotter        32
_mhertz            29
otisday            28
throthra           27
rossj987           23
weezerandburnie    23
GREATNESSEOA       22
MeeestarCoke       22
scoobydoo9749      21
jasemccarty        20
"""

## 4.  Determine the percentage of tweets from users who have more than one
##     tweet in this data set.
more=yikes.loc[yikes['Unnamed: 0']>1]   ##uses same code from #3, just chaging the inequality to >1 to find users with more than 1 tweet
import numpy as np     ##import numpy
users=np.unique(tweet['name']) ## finds unique user names
len(more)/len(users)*100     ##divides the number of tweets from users with more than 1 tweet by total number of tweets and multiplies by 100 to get percentage

"""
4

38.955979742890534
"""
## 5.  Among the negative tweets, which five reasons are the most common?
##     Give the percentage of negative tweets with each of the five most 
##     common reasons.  Sort from most to least common.
negative = tweet[tweet['airline_sentiment']=='negative']      ##aggregates the data by negative tweets
reasons=negative.groupby(['negativereason'])['Unnamed: 0']       ##aggregates the negative tweets by the reasons
morereasons=reasons.count().sort_values(ascending=False)[0:5]      ##counts the number of occurnces for each reason and displays the top 5 reasons why
morereasons/len(negative)*100       ##finds the percentage of negative tweets for the five most common reasons by dividing the above values by the number of negative tweets

"""
5

negativereason                               ##percentage of negative tweets for top 5 reasons
Customer Service Issue    31.706254
Late Flight               18.141207
Can't Tell                12.965788
Cancelled Flight           9.228590
Lost Luggage               7.888429
"""


## 6.  How many of the tweets for each airline include the phrase "on fleek"?
fleek=tweet[tweet['text'].str.contains('on fleek')]      ##aggregates the data that contains the phrase "on fleek"
fleek.groupby([('airline')]).count()['Unnamed: 0']         ##aggregates the above data frame by the airline and counts how many are there for the airline

"""
6                    ##right column indicates the # of tweets for the airline that contains the phrase

airline
JetBlue    146
"""

## 7.  What percentage of tweets included a hashtag?
hashtag=tweet[tweet['text'].str.contains('#')]  ##finds tweets that included a hashtag
len(hashtag)/len(tweet)*100         ##divides the number of tweets that had a hashtag by total number of tweets

"""
7

17.001366120218577        ##% of tweets that included a hashtag
"""

## 8.  How many tweets include a link to a web site?
http=tweet[tweet['text'].str.contains('http')]       ##finds tweets that had a link
len(http)   ##finds number of tweets that had a link

"""
8

1173
"""

## 9.  How many of the tweets include an '@' for another user besides the
##     intended airline?
tags=tweet['text'].str.count('@') > 1    ##finds tweets that have more than 1 @ in text
np.sum(tags)       ##adds up the amount of tweets that has more than 1 @

"""
9

1645
"""

## 10. Suppose that a score of 1 is assigned to each positive tweet, 0 to
##     each neutral tweet, and -1 to each negative tweet.  Determine the
##     mean score for each airline, and give the results in table form with
##     airlines and mean scores, sorted from highest to lowest.

def mysgn(x): # Returns the "sign" of x
    if x =='positive':
        return(1) # 1 when x positive
    elif x =='negative':
        return(-1) # -1 when x negative
    else:
        return(0) # 0 when x is neutral

scores=tweet['airline_sentiment'].apply(mysgn)      ##creates a new column called scores that converted the strings in the airline_sentiment to nuemrical values
tweet['scores']=scores                                   ##adds the scores column above to the original data
tweet['scores'].groupby(tweet['airline']).mean().sort_values(ascending=False)      ##finds the mean score for each airline

"""
10

airline
Virgin America   -0.057540
JetBlue          -0.184968
Southwest        -0.254545
United           -0.560178
American         -0.588619
US Airways       -0.684518
"""

## 11. Among the tweets that "@" a user besides the indicated airline, 
##     what percentage include an "@" directed at the other airlines 
##     in this file? (Note: Twitterusernames are not case sensitive, 
##     so '@MyName' is the same as '@MYNAME' which is the same as '@myname'.)
tags=tweet.loc[tweet['text'].str.count('@') > 1]         ## aggregates the data by tweets with more than 1 @
mentions=pd.Series(['@virginamerica','@jetblue','@southwestair','@americanair','@usairways','@united']) ##makes series of airline names
ct=0       ##starts the counter
txt=tags['text']      ##isolates the tags data by tweeter texts
for i in txt:                  ##looks through all ranges of the txt
    strings=pd.Series(i.lower().split())       ##makes the tweeter texts lower case and splits them into individual words
    if mentions.isin(strings).sum() >1:        ##checks if the airline name is in the tweeter texts and adds to the counter if there's more than 1 airline mentioned, the same airline mentioned in the tweet would only count once.
        ct+=1
ct/len(txt)*100            ##gets the percentage


"""
11

18.72340425531915
"""
    
## 12. Suppose the same user has two or more tweets in a row, based on how they 
##     appear in the file. For such tweet sequences, determine the percentage
##     for which the most recent tweet (which comes nearest the top of the
##     file) is a positive tweet.
sequences=0     ##counter for the total number of tweet seqeunces
positive=0        ##counter for the most recent tweet in the sequence being positive
savedname= ' '      ##used to account for cases where the consecutive tweets are more than 2, makes consecutive tweets not counted twice or more if tweet sequence is > 2
for i in range(len(tweet)-1):                 ##goes upto max-1 as we'll have to check i+1 tweet
    currentname=tweet['name'][i]                  ##gets the current name
    nextname=tweet['name'][i+1]               ##gets the next name
    if (currentname == savedname):              ##first check to see if the current name is not a subsequence name in a sequence
        continue                               ##continues if it's not
    elif (currentname==nextname):            ##checks if the names are same in a row
        sequences += 1                   ##adds to the count of sequences found
        if tweet['airline_sentiment'][i] == 'positive':         ##checks if the first tweet is positive
            positive += 1                          ##adds to the positive counter if it is true
        savedname = currentname          ##saves the current name in case there are more than 2 tweets in the sequence
    else:                           ##if the current name and next name are not in sequence, makes savedname blank again
        savedname= ' '

100*positive/sequences       ##finds percentage of positive tweets in tweets that appear in sequences

"""
12

11.189634864546525
"""
## 13. Give a count for the top-10 hashtags (and ties) in terms of the number 
##     of times each appears.  Give the hashtags and counts in a table
##     sorted from most frequent to least frequent.  (Note: Twitter hashtags
##     are not case sensitive, so '#HashTag', '#HASHtag' and '#hashtag' are
##     all regarded as the same. Also ignore instances of hashtags that are
##     alone with no other characters.)
text=tweet['text']              ##isolates the tweet data by text column
hashes=[]        ##creates an empty vector that will contain the hashtags
for i in range(len(text)):
    strings = text[i].lower().split()         ##splits the text strings and make the lower case
    for ee in strings:
        if ee.startswith("#") == True:              ##makes the condition that will find words that start with a hashtag
                        hashes.append(ee)          ##adds the found hashtag to the empty vector created above
                        
hashtags=pd.Series(hashes)                        ##makes the found hashtags into series
counts=hashtags.value_counts()      ##counts the hashtags
counts[1:13]  ##displays top 10 hashtags (and ties)
why= pd.Series(['!','?'])
trew=hashtags.replace(why,' ')
zxcv=trew.str.split(' ')
qwer=pd.Series(zxcv)
count=qwer.value_counts()
count[1:13]
"""
13

#destinationdragons    76
#fail                  64
#jetblue               44
#unitedairlines        43
#customerservice       34
#usairways             30
#neveragain            26
#usairwaysfail         26
#united                25
#americanairlines      25
#disappointed          23
#avgeek                22
"""
