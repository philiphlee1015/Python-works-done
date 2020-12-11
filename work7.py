##  This assignment requires data from four files: 
##
##      'movies.txt':  A file of over 3900 movies
##      'users.dat':   A file of over 6000 reviewers who provided ratings
##      'ratings.dat': A file of over 1,000,000 movie ratings
##      'zips.txt':    A file of zip codes and location information
##
##  The file 'readme.txt' has more information about the first three files.
##  You will need to consult the readme file to answer some of the questions.

##  Note: You will need to convert the zip code information in 'users.dat' into
##  state (or territory) information for one or more of the questions below.
##  You must use the information in 'zips.txt' for this purpose, you cannot
##  use other conversion methods. 
import pandas as pd
import numpy as np


## 1.  Determine the percentage of users that are female.  Do the same for the
##     percentage of users in the 35-44 age group.  In the 18-24 age group,
##     determine the percentage of male users.

users = pd.Series(open('users.dat').read().splitlines())     ##reads in the users.dat
100*np.sum(users.str.split('::').str[1] == 'F')/len(users)     ##gets the percentage of users that are female
100*np.sum(users.str.split('::').str[2] == '35')/len(users) ##gets the percentage of users in 35-44age group
teen=users.loc[users.str.split('::').str[2] == '18']       ##gets the 18-24 age group
100*np.sum(teen.str.split('::').str[1] == 'M')/len(teen)      ##finds the percentage of male users in 18-24group

"""
1

28.294701986754966     ##percentage of users that are female
19.751655629139073      ##percentage of 35-44 age grouped users
72.98277425203989          ##percentage of male users in 18-24 age group
"""

## 2.  Give a year-by-year table of counts for the number of ratings, sorted by
##     year in ascending order.

rating = pd.Series(open('ratings.dat').read().splitlines())  ##reads in the ratings.dat
times=rating.str.split('::').str[-1]        ##gets the times from the ratings.dat
timess=pd.to_datetime(times,unit='s')       ##converts the times into readable format 
timess.dt.year.value_counts(ascending=False)     ##gets the counts for the number of ratings for each year

"""
2

2000    904757
2001     68058
2002     24046
2003      3348
"""

## 3.  Determine the average rating for females and the average rating for 
##     males.

user=users.str.split('::')      ##splits the users by :: 
userss=pd.DataFrame({'id':user.str[0], 'gender':user.str[1],'age':user.str[2],'occupation':user.str[3],'zip':user.str[4]}) ##makes a dataframe based on the split users created above that contains user id,gender, age, and occupation and zip code
ratingss=rating.str.split('::')     ##splits the rating by ::
ratings=pd.DataFrame({'id':ratingss.str[0],'movieid':ratingss.str[1],'rating':ratingss.str[2]})  ##makes a dataframe based on the split data created above that contains user id,movie id and rating
ratings['rating']=ratings['rating'].astype(int)   ##converts the column rating into integer
df1=pd.merge(userss,ratings, on='id')      ##merges the users dataframe and ratings dataframe on user id
df1.rating[df1.gender=='F'].mean()      ##gets the avg rating for females
df1.rating[df1.gender=='M'].mean()      ##gets the avg rating for males

"""
3

3.6203660120110372      ##avg rating for females
3.5688785290984373      ##avg rating for males
"""

## 4.  Find the top-10 movies based on average rating.  (Movies and remakes 
##     should be considered different.)  Give a table with the movie title
##     (including the year) and the average rating, sorted by rating from
##     highest to lowest.  (Include ties as needed.)

movie = pd.Series(open('movies.txt', encoding = "utf8").read().splitlines())    ##reads in the movies.txt file
mov=movie.str.split('::')    ##splits movie by ::
movies=pd.DataFrame({'movieid':mov.str[0],'title':mov.str[1],'genre':mov.str[-1]}) ##makes a dataframe that contains movieid, movie title, and genre
df2=pd.merge(df1,movies,on='movieid')     ##merges the first dataframe with the movies by the movie id column
df2.groupby([(df2.title)]).mean().sort_values(by='rating',ascending=False)[0:10]   ##gets the avg rating for each movie titles and sorts them from highest to lowest

"""
4

                                           rating
title                                            
Ulysses (Ulisse) (1954)                       5.0
Lured (1947)                                  5.0
Follow the Bitch (1998)                       5.0
Bittersweet Motel (2000)                      5.0
Song of Freedom (1936)                        5.0
One Little Indian (1973)                      5.0
Smashing Time (1967)                          5.0
Schlafes Bruder (Brother of Sleep) (1995)     5.0
Gate of Heavenly Peace, The (1995)            5.0
Baby, The (1973)                              5.0
"""

## 5.  Determine the number of movies listed in 'movies.txt' for which there
##     is no rating.  Determine the percentage of these unrated movies for
##     which there is a more recent remake.

np.sum(movies['title'].isin(df2['title'])==False)    ##finds the number of movies that are not in the dataframe
norating=movies['title'].loc[movies['title'].isin(df2['title'])==False]   ##gets the movie titles that have no rating
100*np.sum(norating.str.split().str[:-1].value_counts()>1)/len(norating) ##finds the percentage that has recent remake

"""
5

177        ##number of movies without rating
0.0             ##percentage of these unrated movies for which there is a more recent remake (none)
"""


## 6.  Determine the average rating for each occupation classification 
##     (including 'other or not specified'), and give the results in a
##     table sorted from highest to lowest average and including the
##     occupation title.

jobratings=df2.groupby([df2.occupation]).mean().sort_values(by='rating',ascending=False) ##gets the avg rating for each occupation
jobratings['occupation']=jobratings.index    ##makes a new column called occupation based on the index number
readme=pd.Series(open('readme.txt', encoding = "utf8").read().splitlines())   ##reads in readme.txt
jb=readme[70:91]        ##gets the occupation names from the readme
names=jb.str.split(':').str[-1]       ##gets the actual occupation names
actualjobs=pd.DataFrame(names).reset_index()       ##makes a dataframe based on job names and resets the index
actualjobs['index']=actualjobs.index.astype(str) ##makes a column called 'index' that has the index values that ranges from 0-20 and converts that into string
actualjobs.columns=['occupation','job title']    ##changes column name as occupation and job title
pd.merge(jobratings,actualjobs,on='occupation')     ##merges jobratings and actualjobs based on occupation number

"""
6

      rating occupation                   job title
0   3.781736         13                   "retired"
1   3.689774         15                 "scientist"
2   3.661578          6        "doctor/health care"
3   3.656589          9                 "homemaker"
4   3.656516          3            "clerical/admin"
5   3.654001         12                "programmer"
6   3.618481         14           "sales/marketing"
7   3.617371         11                    "lawyer"
8   3.613574         17       "technician/engineer"
9   3.599772          7      "executive/managerial"
10  3.596575         16             "self-employed"
11  3.576642          1         "academic/educator"
12  3.573081          2                    "artist"
13  3.537544          0    "other" or not specified
14  3.537529          5          "customer service"
15  3.536793          4      "college/grad student"
16  3.532675         10              "K-12 student"
17  3.530117         18       "tradesman/craftsman"
18  3.497392         20                    "writer"
19  3.466741          8                    "farmer"
20  3.414050         19                "unemployed"
"""

## 7.  Determine the average rating for each genre, and give the results in
##     a table listing genre and average rating in descending order.

df2['genre2']=df2['genre'].str.split('::').str[-1].str.split('|')  ##makes a new column in df2 called genre2 that contains the genres that are split based on :: and |
df2['genre2']=df2['genre2'].astype(str).str.split('[').str[1].str.split(']').str[0] ##gets the genre names without the square brackets
split=df2.drop('genre2', axis=1).join(df2.genre2.str.split(expand=True).stack().reset_index(drop=True, level=1).rename('genre2'))     ##splits the genres into multiple rows while having the index number the same for those split rows
split['genre2']=split['genre2'].str.strip(',')    ##removes commas from the genres
split['rating'].groupby(split['genre2']).mean().sort_values(ascending=False)   ##finds the avg rating for each genre

"""
7

genre2
'Film-Noir'      4.075188
'Documentary'    3.933123
'War'            3.893327
'Drama'          3.766332
'Crime'          3.708679
'Animation'      3.684868
'Mystery'        3.668102
'Musical'        3.665519
'Western'        3.637770
'Romance'        3.607465
'Thriller'       3.570466
'Comedy'         3.522099
'Action'         3.491185
'Adventure'      3.477257
'Sci-Fi'         3.466521
'Fantasy'        3.447371
"Children's"     3.422035
'Horror'         3.215013
"""

## 8.  For the user age category, assume that the user has age at the midpoint
##     of the given range.  (For instance '35-44' has age (35+44)/2 = 39.5)
##     For 'under 18' assume an age of 16, and for '56+' assume an age of 60.
##     For each possible rating (1-5) determine the average age of the raters.

df2['age2']=df2.age.astype(int)     ##creates a new column called age2 that has the values from age column as integer
df2['age2']=df2['age2'].replace(1,16).replace(18,21).replace(25,29.5).replace(35,39.5).replace(45,47).replace(50,52.5).replace(56,60) ##replaces the age group by the midpoint
df2['age2'].groupby(df2.rating).mean()   ##gets the avg age for each possible rating

"""
8

rating
1    31.710783
2    32.769485
3    33.840672
4    34.270909
5    34.368274
"""

## 9.  Find all combinations (if there are any) of occupation and genre for 
##     which there are no ratings.  

exist=pd.Series((split['occupation']+split['genre2']).unique())  ##combines the exisiting occupation data to the existing genres in the dataframe and gets the .unique() function to get the unique combinations and converts them to series
jobs=pd.Series(list(range(0,21))).astype(str)    ##makes a seires that ranges from 0 to 20 for numerical representation of each occupation
allcombinations=jobs+split['genre2'].unique()       ##combines all possible job numbers with all possible genres
newall=pd.Series(np.concatenate(allcombinations).astype(str))     ##combines all arrays of all possible combination into an array that contains all of possible combinations and converts that into string and then to seires
newall.loc[newall.isin(exist)==False]    ##checks if all possible combination is in the pre-existing combinations and locates where the possible combination is not in the existing combinations

"""
9

None       ###indicates that there are no combination of occupation and genre that has no rating
"""

## 10. For each age group, determine the occupation that gave the lowest 
##     average rating.  Give a table that includes the age group, occupation,
##     and average rating.  (Sort by age group from youngest to oldest) 

df3=pd.DataFrame(df2['rating'].groupby([df2.age,df2.occupation]).mean().sort_values())  ##makes a dataframe that has the avg rating for each age group and the corresponding occupation for that age group
df3['index']=df3.index    ##creates a column that contains the multiindex
df3['index']=df3['index'].astype(str).str.split('(').str[1].str.split(')').str[0] ##gets the index column to contain only the age and the occupation
df3['age']=df3['index'].str.split(',').str[0].str.split("'").str[1].astype(int) ##maeks a new column called age that has the age from the index column as integer
df3['occupation']=df3['index'].str.split(',').str[-1].str.split("'").str[1] ##makes a new column called occupation that has the occupation from the index column
df3.index=range(len(df3))  ##resets the index
df3=df3.drop(['index'],axis=1)        ##removes the column index
location=df3['age'].drop_duplicates().index      ##finds the rows where the first occurence of an age group shows up and gets the index values
results=pd.DataFrame(df3.iloc[location].sort_values('age'))   ##makes a dataframe that displays the avg rating for each age group and corresponding occupation
pd.merge(results,actualjobs,on='occupation')      ##merges job titles and the results

"""
10

     rating  age occupation                 job title
0  3.066667    1         11                  "lawyer"
1  3.235525   18          6      "doctor/health care"
2  3.366426   25         19              "unemployed"
3  2.642045   35          8                  "farmer"
4  3.437610   50          8                  "farmer"
5  3.280000   45          4    "college/grad student"
6  3.291755   56         14         "sales/marketing"
"""

## 11. Find the top-5 states in terms of average rating.  Give in table form
##     including the state and average rating, sorted from highest to lowest.
##     Note: If any of the zip codes in 'users.dat' includes letters, then we
##     classify that user as being from Canada, which we treat as a state for
##     this and the next question.

zips = pd.read_csv('zipcodes.txt',                ##reads in the zipcodes.txt file only the useful columns
                  usecols = [1,4],
                  converters={'Zipcode':str})
zips = zips.drop_duplicates()
zips.columns=['zip','State']           
df2['zip']=df2['zip'].str.split('-').str[0]        ##gets the zipcodes before the hyphen if present
df5=df2.merge(zips,how='left',on='zip')        ##merges df2 with zipcodes into a new dataframe while keeping the zipcodes without the states as NaN in the state column
df5.zip=df5.zip.astype(str)       ##converts the zipcodes as string
df5['State'].loc[df5.zip.str.lower().str.islower()==True] = 'Canada'     ##converts the State column in the rows that contains a character from NaN to Canada to account for Canadians
df5['State'].loc[df5.zip.str.len()>5] = 'Unknown'    ##converts the State column in the rows that contain zipcodes with more than 5 numbers from NaN to Unknown to account for weird zipcodes
df5['rating'].groupby([df5.State]).mean().sort_values(ascending=False)[0:5]  ##gets the mean rating for each state

"""
11

State
GU    4.236842
MS    3.996409
AK    3.985730
AP    3.938967
SC    3.807748
"""

## 12. For each genre, determine which state produced the most reviews.  
##     (Include any ties.)

split['zip']=split['zip'].str.split('-').str[0]   ##gets the zipcodes before the hyphen from the split dataframe
newdf6=split.merge(zips,how='left',on='zip')    ##merges split dataframe with zipcodes file
newdf6['State'].loc[newdf6.zip.str.len()>5] = 'Unknown'      ##converts the State column in the rows that contain zipcodes with more than 5 numbers from NaN to Unknown to account for weird zipcodes
newdf6['State'].loc[newdf6.zip.str.lower().str.islower()==True] = 'Canada' ##converts the State column in the rows that contains a character from NaN to Canada to account for Canadians
newdf7=pd.DataFrame(newdf6['genre2'].groupby(newdf6.State).value_counts().sort_values(ascending=False))     ##gets the counts of genres from each state and makes into a dataframe
newdf7['index']=newdf7.index       ##makes a new column called index based on the multindex
newdf7['index']=newdf7['index'].astype(str).str.split('(').str[1].str.split(')').str[0] ##gets the index column as string and removes the parenthesis
newdf7['state']=newdf7['index'].str.split(',').str[0].str.split("'").str[1]     ##makes a new column called state based on the index column that has the state name
newdf7['genre']=newdf7['index'].str.split(',').str[1].str.split('"').str[1]     ##names a new column called genre from the index column that has the genre name
newdf7.index=range(len(newdf7))     ##resets the index
newdf7=newdf7.drop(['index'],axis=1)     ##removes the column index
newlocation=newdf7['genre'].drop_duplicates().index       ##gets the first instance of a genre
newdf7.columns=['review counts','state','genre']       ##renames the columns
newdf7.iloc[newlocation].sort_values('genre')       ##finds the rows for that state that produced most reviews and sorts the result by alphabetical order of genre (except for children's since it does not have '' around it)

"""
12

     review counts state          genre
2            46914    CA       'Action'
8            24135    CA    'Adventure'
57            7922    CA    'Animation'
1            63035    CA       'Comedy'
19           14632    CA        'Crime'
276           1676    CA  'Documentary'
0            66176    CA        'Drama'
77            6384    CA      'Fantasy'
144           3658    CA    'Film-Noir'
26           12938    CA       'Horror'
62            7572    CA      'Musical'
64            7562    CA      'Mystery'
6            27252    CA      'Romance'
4            28915    CA       'Sci-Fi'
3            34570    CA     'Thriller'
29           12498    CA          'War'
141           3774    CA      'Western'
28           12587    CA    Children\'s       ##should be Children's instead of Children\'s
"""
