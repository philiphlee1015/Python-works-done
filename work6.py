##  This assignment requires the data file 'movies.txt'.  This file
##  contains records for nearly 4000 movies, including a movie ID number, 
##  the title (with year of release, which is not part of the title), and a 
##  list of movie genre classifications (such as Romance, Comedy, etc). 

##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit.  

import numpy as np # load numpy as np
import pandas as pd # load pandas as pd
movie = open('movies.txt', encoding = "utf8").read().splitlines() 


## 1.  Are there any repeated movies in the data set?  A movie is repeated 
##     if the title is exactly repeated and the year is the same.  List any 
##     movies that are repeated, along with the number of times repeated.

movies=pd.Series(movie)      ##converts movie into series
names=movies.str.split('::').str[1]       ##splits the string into just the movie names and the year
np.sum(names.value_counts() >1)         ##checks if there is any movie that are repeated

"""
1

0           ## no movies are repeated
"""

## 2.  Determine the number of movies included in genre "Action", the number
##     in genre "Comedy", and the number in both "Children's" and "Animation".
genre=movies.str.split('::').str[-1]        ##isolates the strings by the genres
counts=genre.value_counts()          ##counts the genres
Action=np.sum(counts.filter(like= 'Action'))       ##finds the genre names that contain Action and the sum of all counts of the specified genre
Comedy=np.sum(counts.filter(like= 'Comedy'))       ##finds genre names that contain Comedy and the sum of all counts of the specified genre
Anime=np.sum(counts.filter(like= "Animation|Children's"))     ##finds genre names that contain both Children's and Animation  and the sum of all counts of the specified genre
print(Action,Comedy,Anime)       ##prints the number of movies for each of the genres


"""
2

503 1200 84          ##number of movies included in the genres specified. First is for Action, second is for Comedy, and last one is for Children's and Animation
"""


## 3.  Among the movies in the genre "Horror", what percentage have the word
##     "massacre" in the title?  What percentage have 'Texas'? (Upper or lower
##     cases are allowed here.) 
horror=names.loc[genre.str.contains('Horror')]  ##prints the movie titles that have the genre of horror
aa=pd.DataFrame(horror)        ##converts the titles into dataframe
bb=aa[0].str.lower()        ##makes all titles lowercased
mass=np.sum(bb.str.contains('massacre'))     ##finds the number of titles that contain massacre
tex=np.sum(bb.str.contains('texas'))       ##finds the number of titles that contain texas

mass/len(horror)*100      ##gets the percentages
tex/len(horror)*100

"""
3

2.623906705539359        ##% of titles that contain 'massacre'
1.1661807580174928      ##% of titles that contain 'texas'
"""

## 4.  How many titles are exactly one word?

justnames=names.str.split().str[0:-1] ##gets the movie names without the year
np.sum(justnames.str.len() == 1)      ##finds the number of titles that are exactly 1 word

"""
4

690       ##number of titles that are exactly one word
"""

## 5.  Among the movies with exactly one genre, determine the top-3 genres in
##     terms of number of movies with that genre.
genre2=movies.str.split('::').str[-1].str.split('|')  ##gets the genre names and splits it by | 
(genre2.loc[genre2.str.len() == 1]).value_counts()[0:3]   ##finds movies with exactly one genre and finds the top 3 genres in terms of movies with that genre

"""
5

[Drama]     843
[Comedy]    521
[Horror]    178
"""

## 6.  Determine the number of movies with 0 genres, with 1 genre, with 2 genres,
##     and so on.  List your results in a table, with the first column the number
##     of genres and the second column the number of movies with that many genres.
gen0=np.sum(genre2.str.len() == 0)            ##finds the number of movies with indicated number of genres
gen1=np.sum(genre2.str.len() == 1)
gen2=np.sum(genre2.str.len() == 2)
gen3=np.sum(genre2.str.len() == 3)
gen4=np.sum(genre2.str.len() == 4)
gen5=np.sum(genre2.str.len() == 5)
gen6=np.sum(genre2.str.len() == 6)

data = {'number of genres': [0,1,2,3,4,5,6],
        'number of movies':[gen0,gen1,gen2,gen3,gen4,gen5,gen6]}
df= pd.DataFrame(data,columns=['number of genres','number of movies'])     ##makes the table
df

"""
6

   number of genres  number of movies
0                 0                 0
1                 1              2025
2                 2              1322
3                 3               421
4                 4               100
5                 5                14
6                 6                 1
"""

## 7.  How many remakes are in the data?  A movie is a remake if the title is
##     exactly the same but the year is different. (Count one per remake.  For
##     instance, 'Hamlet' appears 5 times in the data set -- count this as one
##     remake.)
np.sum(names.str.split('(').str[:-1].value_counts()>1)
##splits the movie titles by just their names, excluding the years
##finds the number of movies that are remakes and gets the number of remakes in the data

"""
7

38          ##number of remaeks in the data
"""

## 8.  List the top-5 most common genres in terms of percentage of movies in
##     the data set.  Give the genre and percentage, from highest to lowest.

numgen=genre2.apply(pd.Series).stack().value_counts() ##finds the number of movies that contains the genre
(100*numgen/len(movies))[0:5]       ##gives top 5 most common genres in terms of percentage of movies

"""
8

Drama       41.282514
Comedy      30.903940
Action      12.953902
Thriller    12.670616
Romance     12.129797
"""

## 9.  Besides 'and', 'the', 'of', and 'a', what are the 5 most common words  
##     in the titles of movies classified as 'Romance'? (Upper and lower cases
##     should be considered the same.)  Give the number of titles that include
##     each of the words.
ro=names.loc[genre.str.contains('Romance')]  ##prints the movie titles that have the genre of Romance
aa=pd.DataFrame(ro)        ##converts the titles into dataframe
bb=aa[0].str.lower()        ##makes all titles lowercased
titles=pd.DataFrame(bb.str.split().str[0:-1])       ##just gives the title of the movie without the year
wordct=titles[0].apply(pd.Series).stack().value_counts()       ##count the occurences of each word
df=pd.DataFrame(wordct)      ##coverts the word count into a dataframe
forbidden= pd.Series(['and','the','of','a'])    ##makes a series of words that are excluded
words=(df[~df.index.isin(forbidden)])[0:5]     ##prints the top 5 most common words without the excluded words
print(words)

"""
9

in    27         ##top 5 most common words in movie titles and the number of occurences
love  21
to    14
you   10
on    10
"""

## 10. It is thought that musicals have become less popular over time.  We 
##     judge that assertion here as follows: Compute the mean release years 
##     for all movies that have genre "Musical", and then do the same for all
##     the other movies.  Then repeat using the median in place of mean.
mu=names.loc[genre.str.contains('Musical')]          ##finds the movie names where the genre contains 'Musical'
muyrs=mu.str.split().str[-1].str.split("(").str[-1].str.split(")").str[0]       ##gets the years of the movies
munumb=muyrs.astype(float)     ##converts the years into float
np.mean(munumb)         ##finds the mean yrs for Musicals
np.median(munumb)         ##finds the median yrs for Musicals

years=names.str.split().str[-1].str.split("(").str[-1].str.split(")").str[0]    ##gets all the years for all movies
data = pd.DataFrame({'years': years,'genre2':genre2})     ##makes a dataframe with movie years and the associated movie genres
newdat=data.convert_objects(convert_numeric=True)      ##converts the years column to numeric
newdat['genre2']=newdat['genre2'].astype(str)       ##converts the genre column to string
newdat['genre2']=newdat['genre2'].str.strip('[').str.strip(']')    ##removes the brackets in the genres
split=newdat.drop('genre2', axis=1).join(newdat.genre2.str.split(expand=True).stack().reset_index(drop=True, level=1).rename('genre2'))
##splits the genres into multiple rows
split['genre2']=split['genre2'].str.strip(',')       ##removes commas from the genre names   
split['years'].groupby(split['genre2']).mean().drop(["'Musical'"])         ##finds the mean release yrs for each genre excluding musical
split['years'].groupby(split['genre2']).median().drop(["'Musical'"])          ##finds the median release yrs for each genre excluding musical

nomu=names.loc[genre.str.contains('Musical') == False]       ##finds movie titles without musical genre
nomuyrs=nomu.str.split().str[-1].str.split("(").str[-1].str.split(")").str[0]  ##gets the years for the titles
nomunumb=nomuyrs.astype(float)   ##converts the years into numbers
np.mean(nomunumb)     ##finds the mean for all movie genres excluding musical
np.median(nomunumb)      ##finds the mean for all movie genres excluding musical

"""
10

1968.7456140350878        ##mean yrs released  for Musical
1967.0           ##median yrs released for Musical
-----------
"Children's"     1984.597610             ##mean years released for each genres
'Action'         1988.898608
'Adventure'      1984.388693
'Animation'      1982.961905
'Comedy'         1988.309167
'Crime'          1987.483412
'Documentary'    1994.196850
'Drama'          1987.379289
'Fantasy'        1987.029412
'Film-Noir'      1963.409091
'Horror'         1981.548105
'Mystery'        1981.924528
'Romance'        1988.394904
'Sci-Fi'         1984.061594
'Thriller'       1987.855691
'War'            1977.993007
'Western'        1972.367647
-------------------------
"Children's"     1993.0            ##median years released for each genres
'Action'         1993.0
'Adventure'      1989.0
'Animation'      1993.0
'Comedy'         1994.0
'Crime'          1995.0
'Documentary'    1996.0
'Drama'          1994.0
'Fantasy'        1989.5
'Film-Noir'      1954.0
'Horror'         1986.0
'Mystery'        1993.0
'Romance'        1995.0
'Sci-Fi'         1988.5
'Thriller'       1995.0
'War'            1985.0
'Western'        1971.5
===========================
1986.5908729105863           ##mean yrs released for all non-musical genres
1994.0                         ##median yrs released for all non-musical genres
                            ##apparently this is what you guys were looking for?
"""
