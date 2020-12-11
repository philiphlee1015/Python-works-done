##  This assignment requires data from the file 
##
##      'ncaa.csv':  NCAA Men's Tournament Scores, 1985-2019
##
##  The organization of the file is fairly clear.  Each record has information
##  about one game, including the year, the teams, the final score, and each 
##  team's tournament seed.  All questions refer only to the data in this
##  file, not to earlier tournaments.

##  Note: The data set is from Data.World, with the addition of the 2019
##  tournament provided by your dedicated instructor.

import pandas as pd
ncaa = pd.read_csv('ncaa.csv')

## 1.  Find all schools that have won the championship, and make a table that
##     incluldes the school and number of championships, sorted from most to
##     least.
champs=ncaa[ncaa['Region Name'].str.contains('Championship')]       ##gets the championship data
champs1=pd.DataFrame(champs['Team'].loc[(champs['Score']>champs['Score.1'])==True])      ##gets the champion team names
champs2=pd.DataFrame(champs['Team.1'].loc[(champs['Score']<champs['Score.1'])==True])
champs2.columns=['Team']     ##changes column of champs2 into Team so it can be concatenated with champs1
allchamps=pd.concat([champs1,champs2])   ##concats both dfs
allchamps['Team'].value_counts()      ##counts the number of championships for each team

"""
1

Duke              5
North Carolina    4
Connecticut       4
Villanova         3
Kentucky          3
Kansas            2
Florida           2
Louisville        2
Virginia          1
Arizona           1
Syracuse          1
UNLV              1
UCLA              1
Indiana           1
Arkansas          1
Michigan St       1
Maryland          1
Michigan          1
"""

## 2.  Find the top-10 schools based on number of tournament appearances.
##     Make a table that incldes the school name and number of appearances,
##     sorted from most to least.  Include all that tie for 10th position
##     if necessary.
round1=ncaa[ncaa['Round']==1]       ##isolates teh df by first round
school=pd.concat([round1['Team'],round1['Team.1']])     ##concatenates teams 
school.value_counts().nlargest(11)     ##gets the top-10 schools based on number of tourmanment appearances

"""
2

Duke              34
Kansas            34
Arizona           32
North Carolina    32
Kentucky          30
Michigan St       29
Syracuse          28
Louisville        26
Oklahoma          26
Purdue            26            ##4-way ties for 10th place
Texas             26
"""

## 3.  Determine the average tournament seed for each school, then make a
##     table with the 10 schools that have the lowest average (hence the
##     best teams). Sort the table from smallest to largest, and include
##     all that tie for 10th position if necessary.
seed0=round1[['Seed','Team']]     ##gets the seeds and teams for round 1
seed1=round1[['Seed.1','Team.1']]
seed1.columns=['Seed','Team']
seeds=pd.concat([seed0,seed1])       ##concatenates the dataframes
seeds['Seed'].groupby(seeds.Team).mean().nsmallest(10)     ##gets the avg seed for each school

"""
3

Team
Duke               2.176471
Kansas             2.500000
North Carolina     2.718750
Kentucky           3.566667
Connecticut        3.950000
Loyola Illinois    4.000000
Massachusetts      4.375000
Syracuse           4.428571
Arizona            4.437500
Ohio St            4.450000
"""

## 4.  Give a table of the average margin of victory by round, sorted by
##     round in order 1, 2, ....
ncaa['margin']=abs(ncaa['Score']-ncaa['Score.1'])     ##makes a new column called margin that gets the margin of victory by round
ncaa['margin'].groupby(ncaa.Round).mean()      ##gets the avg margin of victory by round

"""
4

Round
1    12.956250
2    11.275000
3     9.917857
4     9.707143
5     9.485714
6     8.257143
"""

## 5.  Give a table of the percentage of wins by the higher seed by round,
##     sorted by round in order 1, 2, 3, ...

highseed1=ncaa[ncaa['Seed']<ncaa['Seed.1']]       ##gets the rows with higher seed
highseed2=ncaa[ncaa['Seed']>ncaa['Seed.1']]
win1=(highseed1[highseed1['Score']>highseed1['Score.1']])['Round'].value_counts()      ##gets the winning teams by the higher seed by round
win2=(highseed2[highseed2['Score']<highseed2['Score.1']])['Round'].value_counts()
100*win1.add(win2,fill_value=0)/ncaa['Round'].value_counts()       ##gets the percentage

"""
5

1    74.285714
2    71.250000
3    71.428571
4    55.000000
5    48.571429
6    57.142857
"""

## 6.  Determine the average seed for all teams in the Final Four for each
##     year.  Give a table of the top-5 in terms of the lowest average seed
##     (hence teams thought to be better) that includes the year and the
##     average, sorted from smallest to largest.
ff=ncaa[ncaa['Region Name']=='Final Four']     ##gets the dta with final four
seed00=ff[['Year','Seed']]        ##gets the year and the seed for the final four
seed11=ff[['Year','Seed.1']]
seed11.columns=['Year','Seed']
seedss=pd.concat([seed00,seed11])     ##concatenates the dataframes
seedss['Seed'].groupby([seedss['Year']]).mean().sort_values()[0:8]      ##gets the avg seeds for all teams for each year

"""
6

2008    1.00
1993    1.25
2007    1.50
2001    1.75
1999    1.75
1997    1.75
1991    1.75
2009    1.75
"""

## 7.  For the first round, determine the percentage of wins by the higher
##     seed for the 1-16 games, for the 2-15 games, ..., for the 8-9 games.
##     Give a table of the above groupings and the percentage, sorted
##     in the order given.
firstround=ncaa[ncaa['Round']==1]            ##gets the data pertaining to first round
firstround['combinedseed']=firstround['Seed'].astype(str)+'-'+firstround['Seed.1'].astype(str)    ##combines the seed so it'll be like 1-16 and 2-15 and so on
win11=(firstround[firstround['Score']>firstround['Score.1']])       ##gets the record of wins by the higher seeds
100*win11['combinedseed'].value_counts()/firstround['combinedseed'].value_counts() ##gets the percentage of wins by the higher seeds

"""
7

1-16    99.285714
2-15    94.285714
3-14    85.000000
4-13    79.285714
5-12    64.285714
6-11    62.857143
7-10    60.714286
8-9     48.571429
"""

## 8.  For each champion, determine the average margin of victory in all
##     games played by that team.  Make a table to the top-10 in terms of
##     average margin, sorted from highest to lowest.  Include all that tie
##     for 10th position if necessary.
winner=[]          ##makes an empty list called winner
loser=[]         ##makes an empty list called loser
for i,j in ncaa.iterrows():          ##makes a loop that goes over the df rows
    if j['Score']>j['Score.1']:       ##makes a condition if score is bigger, then it'll append the team name to winner, else it'll append to loser
        winner.append(j['Team'])
        loser.append(j['Team.1'])
    else:
        winner.append(j['Team.1'])
        loser.append(j['Team'])
ncaa['winner']=winner    ##makes new columns called winner and loser that contains winning and losing team names
ncaa['loser']=loser


years=ncaa[ncaa['Region Name']==('Championship')]['Year']   ##gets the years for the championships
winners=ncaa[ncaa['Region Name']==('Championship')]['winner']   ##gets the winners from championships
combined=years.astype(str)+'-'+winners.astype(str)    ##combines years and the winners
ncaa['combined']=ncaa['Year'].astype(str)+'-'+ncaa['winner'].astype(str)     ##makes a new column called combined that has the year and the winner name for each rows
df=ncaa[ncaa['combined'].isin(combined)]    ##checks if championship winner is in the combined column and gets the rows pertaining to that data
df['margin'].groupby([df['winner'],df['Year']]).mean().nlargest(10)  ##gets the margin of vicotry in all games played by the champion in each year


"""
8

winner          Year
Kentucky        1996    21.500000
Villanova       2016    20.666667
North Carolina  2009    20.166667
UNLV            1990    18.666667
Villanova       2018    17.666667
Duke            2001    16.666667
Louisville      2013    16.166667
Florida         2006    16.000000
North Carolina  1993    15.666667
Duke            2015    15.500000
"""



## 9.  For each champion, determine the average seed of all opponents of that
##     team.  Make a table of top-10 in terms of average seed, sorted from 
##     highest to lowest.  Include all that tie for 10th position if necessary.
##     Then make a table of the bottom-10, sorted from lowest to highest.
##     Again include all that tie for 10th position if necessary. 
winseed=[]                      ##pretty much the same thing as #8 but for winning seeds and losing seeds
loseseed=[]
for i,j in ncaa.iterrows():
    if j['Score']>j['Score.1']:
        winseed.append(j['Seed'])
        loseseed.append(j['Seed.1'])
    else:
        winseed.append(j['Seed.1'])
        loseseed.append(j['Seed'])
ncaa['winseed']=winseed
ncaa['loseseed']=loseseed

years=ncaa[ncaa['Region Name']==('Championship')]['Year']              ##same thing as #8 but for seeds
winners=ncaa[ncaa['Region Name']==('Championship')]['winner']
combined=years.astype(str)+'-'+winners.astype(str)
ncaa['combined']=ncaa['Year'].astype(str)+'-'+ncaa['winner'].astype(str)
df=ncaa[ncaa['combined'].isin(combined)]
df['loseseed'].groupby([df['winner'],df['Year']]).mean().nlargest(11)     ##gets the avg seeds of the opponent teams
df['loseseed'].groupby([df['winner'],df['Year']]).mean().nsmallest(11)

"""
9

winner          Year
UNLV            1990    9.000000
Louisville      2013    8.500000
Kansas          2008    8.000000
Virginia        2019    8.000000
Florida         2006    7.666667
Connecticut     1999    7.500000
Louisville      1986    7.500000
Arkansas        1994    7.333333
Michigan St     2000    7.166667
Indiana         1987    7.000000
North Carolina  2005    7.000000
--------------
winner          Year
Villanova       1985    3.333333
Connecticut     2014    4.666667
Villanova       2016    4.833333
North Carolina  1993    5.500000
                2017    5.666667
Syracuse        2003    5.666667
North Carolina  2009    5.833333
Florida         2007    6.000000
Kentucky        1996    6.000000
Maryland        2002    6.000000
Michigan        1989    6.000000
"""


## 10. Determine the 2019 champion.

yr=ncaa[ncaa['Year'].astype(str).str.contains('2019')]       ##gets the data from 2019
champ2019=yr[yr['Region Name'] == 'Championship']        ##gets the row with the championship in 2019
if (champ2019['Score'] > champ2019['Score.1']).bool() == True:        ##makes a condition that prints the winning team
    print(champ2019['Team'])
else:
    print(champ2019['Team.1'])

"""
10

2204    Virginia        ##2019 is Virginia
"""
