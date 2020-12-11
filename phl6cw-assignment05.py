## File: phl6cw-assignment01.py 
## Topic:  Assignment 05 Solutions
## Name: Philip Lee

##  This assignment requires the data file 'diabetic_data.csv'.  This file
##  contains records for over 100,000 hospitalizations for people who have
##  diabetes.  The file 'diabetic_info.csv' contains information on the
##  codes used for a few of the entries.  Missing values are indicated by
##  a '?'.  You should be able to read in this file using the usual 
##  pandas methods.

##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit.  
import numpy as np # load numpy as np
import pandas as pd # load pandas as pd
data = pd.read_csv('diabetic_data.csv')

## 1.  Determine the average number of medications ('num_medications') for 
##     males and for females.
data['num_medications'].groupby(data['gender']).mean()       ##groups the data by gender for number of medications and finds the mean

"""
1

gender
Female             16.187888
Male               15.828775
"""

## 2.  Determine the average length of hospital stay ('time_in_hospital')
##     for each race classification.  (Omit those unknown '?' but include 
##     those classified as 'Other'.)
data['time_in_hospital'].groupby(data['race']).mean()[1:]   ##groups the data by race for time in hospital and finds the avg time excluding '?'

"""
2

race
AfricanAmerican    4.507860
Asian              3.995320
Caucasian          4.385721
Hispanic           4.059892
Other              4.273572
"""

## 3.  Among males, find a 95% confidence interval for the proportion that 
##     had at 2 or more procedures ('num_procedures').  Then do the same 
##     for females.

male=data.loc[data['gender']=='Male']   ##groups data by males
female=data.loc[data['gender']=='Female']  ##groups data by females
maleproc=male.loc[male['num_procedures']>=2]    ##finds males with 2 ore more procedures
femaleproc=female.loc[female['num_procedures']>=2]  ##same as above but for females
nmale=len(male)   ##finds # of rows for males
nfemale=len(female)  ##same but for females
phatmale=len(maleproc)/nmale    ##finds proportion of males that had 2 or more procedures out of total males
phatfemale=len(femaleproc)/nfemale   ##same but for females
lclmale = phatmale - 1.96*np.sqrt(phatmale*(1-phatmale)/nmale)  ##calculates 95% confidence interval for males
uclmale = phatmale + 1.96*np.sqrt(phatmale*(1-phatmale)/nmale)
print(lclmale,uclmale)
lclfemale = phatfemale - 1.96*np.sqrt(phatfemale*(1-phatfemale)/nfemale)  ##calculates 95% confidence interval for females
uclfemale = phatfemale + 1.96*np.sqrt(phatfemale*(1-phatfemale)/nfemale)
print(lclfemale,uclfemale)

"""
3

0.3551161035669802 0.36378730733515563          ##95% confidence interval for males
0.31516986803938 0.32298177340245665           ## for females
"""

## 4.  Among the patients in this data set, what percentage had more than
##     one recorded hospital visit?  (Each distinct record can be assumed 
##     to be for a distinct hospital visit.)

patient=np.unique(data['patient_nbr'])    ##finds unique patients based on patient_nbr, assumes that patient_nbr stays the same for different visits
pat=data.groupby(data['patient_nbr'])     ##groups the data by patient nbr
100*np.sum(pat.count()['encounter_id']>1)/len(patient) ##uses .count function to count the number of records corresponding to the patient
                                                    ##the column encounter_id is used to get the number of records for hospital visits
    ##uses np.sum to get number of patients that had mroe than 1 visits and divide it by the number of unique patients to get the percentage                                                      

"""
4

23.452837048015883
"""

## 5.  List the top-10 most common diagnoses, based on the codes listed in
##     the columns 'diag_1', 'diag_2', and 'diag_3'.

(data['diag_1'].value_counts()+data['diag_2'].value_counts()+data['diag_3'].value_counts()).sort_values(ascending=False)[0:10]
##counts the number for each diagnoses and adds them up and displays the top 10 results

"""
5

                 ##left column is diagnoses, right colum is the number records that the diagnoses had been used for
428    18101.0
250    17861.0
276    13816.0
414    12895.0
401    12371.0
427    11757.0
599     6824.0
496     5990.0
403     5693.0
486     5455.0
"""
## 6.  The 'age' in each record is given as a 10-year range of ages.  Assume
##     that the age for a person is the middle of the range.  (For instance,
##     those with 'age' [40,50) are assumed to be 45.)  Determine the average
##     age for each classification in 'insulin'.

age=data['age']  ##groups the data by the age column
justnumbers=age.str.split('[').str[1].str.split(')').str[0].str.split('-').str[1] ##splits the column multiple times to get the number in the upper range
maxage=justnumbers.astype(int)  ##converts the string into integer
mean=maxage-5   ##gets the assumed age
mean.groupby(data['insulin']).mean()      ##finds the mean age based on the insulin classification

"""
6

insulin
Down      63.300049
No        67.460165
Steady    65.571169
Up        63.673560
"""

## 7.  Among those whose weight range is given, assume that the actual
##     weight is at the midpoint of the given interval.  If the weight is
##     listed as '>200' then assume the actual weight is 200.  Determine the
##     average weight for those whose 'num_lab_procedures' exceeds 50,
##     then do the same for those that are fewer than 30.

exceed50=data[data['num_lab_procedures']>50]       ##finds the rows that have num lab procedures exceeding 50
not200=exceed50[exceed50.weight != '>200']     ##isolates the data above by weight that does not exceeed 200
yes200=len(exceed50)-len(not200)        ##finds the number of rows that have weight exceeding 200
removeqmark=not200[not200.weight!= '?']     ##removes the rows that does not have any input for the weight
justnumbers=removeqmark['weight'].str.split('[').str[1].str.split(')').str[0].str.split('-').str[1]  ##gets the number from the upper range in the string
midpt=justnumbers.astype(float) - 12.5     ##gets the assumed weight
twohundred=pd.Series(yes200*[200])      ##makes a series that contains 200 by the number of rows that contain '
final=midpt.append(twohundred)        ##adds the series above to the assumed weight list
np.mean(final)         ##finds the mean weight for those whose num_lab_procedures exceed 50

below30=data[data['num_lab_procedures']<30]      ##same as the codes above but for fewer than 30
not200=below30[below30.weight != '>200']
yes200=len(below30)-len(not200)
removeqmark=not200[not200.weight!= '?']
justnumbers=removeqmark['weight'].str.split('[').str[1].str.split(')').str[0].str.split('-').str[1]
midpt=justnumbers.astype(float) - 12.5
twohundred=pd.Series(yes200*[200])
final=midpt.append(twohundred)
np.mean(final)

"""
7

85.05018489170628      ##avg weight for >50
88.73546511627907          ##avg weight for <30
"""

## 8.  Three medications for type 2 diabetes are 'glipizide', 'glimepiride',
##     and 'glyburide'.  There are columns in the data for each of these.
##     Determine the number of records for which at least two of these
##     are listed as 'Steady'.

glip = data['glipizide'] == 'Steady'      ##finds which rows have 'Steady' in glipizide column
glim = data['glimepiride'] == 'Steady'   ##same as above but for glimepiride
glyb = data['glyburide'] == 'Steady'  ##same as above but for glyburide
np.sum((glip & glim) | (glip & glyb) | (glim & glyb))      ##finds the sum of records that has at least two of these listed as steady

"""
8

284
"""

## 9.  What percentage of reasons for admission ('admission_source_id')
##     correspond to some form of transfer from another care source?

transferid= pd.Series([4,5,6,10,18,22,25,26])    ##makes a series that contains the IDs for 'Transfer from' from the info.csv
100*np.sum(data['admission_source_id'].isin(transferid))/len(data['admission_source_id'])
     ##finds the sum of records that contains the transferid and gets the percentage of reasons tha tcorrespond to some form of transfer from another care source
     
"""
9

6.218186820745633
"""

## 10. The column 'discharge_disposition_id' gives codes for discharges.
##     Determine which codes (and the corresponding outcomes from the ID
##     file) resulted in no readmissions ('NO' under 'readmitted').  Then
##     find the top-5 outcomes that resulted in readmissions, in terms of
##     the percentage of times readmission was required.

info = pd.read_csv('diabetic_info.csv') ##loads info.csv
discharge=info[10:40]     ##isolates the info by the rows that contain info on discharge disposition id
discharge.columns=['discharge id','description']  ##changes the column names of discharge info to index and description. Index is the ID (code) for the discharge
admitted = data['readmitted'].str.replace('>30','1').str.replace('<30','1').str.replace('NO','0').astype(int)
##replaces '>30' and '<30' to '1' and replaces 'NO' to '0' and converts them to integers
groups=admitted.groupby(data['discharge_disposition_id']) ##groups by the data by discharge id
noreadmit=groups.sum()[[11,19,20]]    ##adds the total instances of discharge ids and displays those that had 0
nop=pd.DataFrame(noreadmit.astype(str))  ##converts the result above into a string then to a data frame
nop['discharge id']=nop.index        ##adds another column on nop based on the index number
pd.merge(nop.astype(str),discharge)[['discharge id','description']]     ##merges the discharge description to the dataframe containing ids with no readmissions

nope=data.loc[data['readmitted']=='NO'] ##finds the data that had no readmissions
more=data.loc[data['readmitted'] == '>30']  ##isolates the data by readmissions >30
less=data.loc[data['readmitted'] == '<30'] ##isolates the data by readmissions <30
totalreasons=more['discharge_disposition_id'].value_counts()+less['discharge_disposition_id'].value_counts()+nope['discharge_disposition_id'].value_counts()
##^finds the total number of each discharge disposition id
percent=100*(((more['discharge_disposition_id'].value_counts()+less['discharge_disposition_id'].value_counts()).sort_values(ascending=False))/(totalreasons)).sort_values(ascending=False)[0:5]
##^gets the percent of times readmissions was required by getting the sum of counts for discharge IDs and dividing it by the totalreasons
new=pd.DataFrame(percent.astype(str))  ##converts percent into a string then to a data frame
new.columns=['percent']  ##labels the column of new as percent
new['discharge id']=new.index  ##adds a new column to new based on the index. The new column is the discharge id
afff=new.astype(str) ##converts the changed 'new' into string again
bb=afff.loc[afff['percent'] != 'nan']   ##gets rid of rows that contain 'nan'
cc=bb[['percent','discharge id']]    ##shows only percent column and discharge id column
cc.sort_values('percent',ascending=False)  ##sorts the dataframe by percent
"""
10
                 ##codes that resulted in no readmissions
   discharge id                                        description      ##the column discharge id is the discharge disposition id for both parts of the question
0           11                                            Expired
1           19           Expired at home. Medicaid only, hospice.
2           20  Expired in a medical facility. Medicaid only, ...
--------------------------
               percent discharge id
15   73.01587301587301           15
28   61.15107913669065           28
6    54.25515423965277            6
22  53.738083291520326           22
9    52.38095238095239            9
"""