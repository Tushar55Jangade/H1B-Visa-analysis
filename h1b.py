# -*- coding: utf-8 -*-
"""
Created on Tue May 28 23:18:19 2019

@author: tusha
"""

import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal
import numpy as np
import seaborn as sb
h1b_data = pd.read_csv('C://Users//tusha//Desktop//Tushar School Documents//Masters Project//ian-h-1-b-disclosure-data-fy-17//h1b_kaggle_55.csv')

len(h1b_data)
h1b_data.EMPLOYER_NAME.value_counts().head(15)

h1b_data['EMPLOYER_NAME'].value_counts().head(15).plot(kind = "bar" , title ="Top 15 Hiring Company")


h1b_data.PREVAILING_WAGE.value_counts().sort_values(ascending = False).head(15)


h1b_data.PREVAILING_WAGE.mean()

denied = h1b_data[h1b_data.CASE_STATUS=='DENIED']

nooooo = h1b_data[h1b_data.YEAR == 'nan']
h1b_data.dropna()
DAta = h1b_data[h1b_data.JOB_TITLE == 'DATA ANALYST']

DAta['EMPLOYER_NAME'].value_counts().head(50)

#wages given by employee
wages_employee = h1b_data.groupby(['EMPLOYER_NAME']).mean()['PREVAILING_WAGE'].nlargest(15).plot(kind = 'bar')

h1b_data.WORKSITE.value_counts().head(20)

h1b_data.WORKSITE.value_counts().head(20).plot(kind = 'bar', title ="Cities with Highest Job opportunity ")

h1b_data.loc[:,'WORKSITE'] = h1b_data.loc[:,'WORKSITE'].apply(lambda rec:rec.split(',')[1][1:])

def change_NA(rec):
    if (rec=='NA'):
        return 'MARINA ISLANDS'
    return rec
h1b_data.loc[:,'WORKSITE'] = h1b_data.loc[:,'WORKSITE'].apply(lambda rec: change_NA(rec))
print(len(h1b_data['WORKSITE'].unique()))


h1b_data['CASE_STATUS'].unique()


status_freq = [0]*7

statues = ['CERTIFIED-WITHDRAWN', 'WITHDRAWN', 'CERTIFIED', 'DENIED',
       'REJECTED', 'INVALIDATED',
       'PENDING QUALITY AND COMPLIANCE REVIEW - UNASSIGNED']

for i in range(0,7):
    status_freq[i] = h1b_data[h1b_data.CASE_STATUS==statues[i]]['CASE_STATUS'].count()
status_freq
#status_freq.unique()
from matplotlib.pyplot import pie,axis,show
import matplotlib as mpl

plt.figure(figsize = (5,5))
plt.title('PETITIONS BY CASE STATUS')
axis('equal');
pie(status_freq[:4], labels = statues[:4]);
show()

#h1b_data.EMPLOYMENT_START_DATE  = pd.tslib.Timestamp.now()
h1b_data['YEAR'] = h1b_data['YEAR'].apply(lambda year:'%g' % (Decimal(str(year))))

h1b_data['PREVAILING_WAGE'] = h1b_data['PREVAILING_WAGE'].apply(lambda year:'%g' % (Decimal(str(year))))

year = ['2011','2012','2013','2014','2015','2016']
year_count = [0]*6
for i in range(0,6):
    year_count[i] = h1b_data[h1b_data.YEAR==year[i]]['YEAR'].count()
year_count

sb.set_context("notebook",font_scale=1.0)
plt.figure(figsize=(13,3))
plt.title('PETITIONS DISTRIBUTION BY YEAR')
sb.countplot(h1b_data['YEAR'])

denied = h1b_data[h1b_data.CASE_STATUS=='DENIED']
len(denied)


del denied['CASE_STATUS']
denied = denied.reset_index()
denied.head()

denied_year_count = [0]*6
for i in range(0,6):
    denied_year_count[i] = denied[denied.YEAR==year[i]]['YEAR'].count()
denied_year_count


sb.set_context("notebook",font_scale=1.0)
plt.figure(figsize=(13,3))
plt.title('DENIED PETITIONS BY YEAR')
sb.countplot(denied['YEAR'])

denied_rate  = [0]*6
for i in range(0,6):
    denied_rate[i] = float("%.2f" % ((denied_year_count[i] / year_count[i])*100))

ratio = pd.DataFrame()
ratio['year'] = year
ratio['denied rate %'] = denied_rate
ratio = ratio.set_index(['year'])
ratio.T

ratio = ratio.reset_index()
sb.set_context("notebook",font_scale=1.0)
plt.figure(figsize=(13,3))
plt.title('DENIED PETITIONS RATE BY YEAR')
g= sb.barplot(x='year' , y = 'denied rate %', data = ratio)

US_states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado ','Connecticut','Delaware',
             'District of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
             'Maine','Marina Islands','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska',
             'Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota',
             'Ohio','Oklahoma','Oregon','Pennsylvania','Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee',
             'Texas ','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

US_states = [x.upper() for x in US_states] 
  
# printing output 
print(US_states) 
len(US_states)
petition_by_state = [0]*53
for i in range(0,53):
    petition_by_state[i] = h1b_data[h1b_data.WORKSITE == US_states[i]]['WORKSITE'].count()
pet_state = pd.DataFrame()
pet_state['STATE'] = US_states
pet_state['FILED PETITIONS'] = petition_by_state
print(sum(petition_by_state))


sb.set_context("notebook",font_scale=1.0)
plt.figure(figsize=(13,5))
plt.title('FILED PETITIONS BY STATE')
v= sb.barplot(x='STATE' , y = 'FILED PETITIONS', data = pet_state)
rotg = v.set_xticklabels(v.get_xticklabels(), rotation = 90)

########
len(denied)
denied_by_state = [0]*53
for i in range(0,53):
    denied_by_state[i] = denied[denied.WORKSITE == US_states[i]]['WORKSITE'].count()
den_state = pd.DataFrame()
den_state['STATE'] = US_states
den_state['DENIED PETITIONS'] = denied_by_state
print(sum(denied_by_state))


sb.set_context("notebook",font_scale=1.0)
plt.figure(figsize=(13,5))
plt.title('DENIED PETITIONS BY STATE')
v= sb.barplot(x='STATE' , y = 'DENIED PETITIONS', data = den_state)
rotg = v.set_xticklabels(v.get_xticklabels(), rotation = 90)



#######

denied_state_rate = [0]*53
for i in range(0,53):
    denied_state_rate[i] = float("%.2f" % ((denied_by_state[i] / petition_by_state[i])*100))
ratios = pd.DataFrame()
ratios['STATE'] = US_states
ratios['DENIED PETITIONS %'] = denied_state_rate
print(sum(denied_state_rate))


sb.set_context("notebook",font_scale=1.0)
plt.figure(figsize=(13,5))
plt.title('DENIED PETITIONS BY STATE')
v= sb.barplot(x='STATE' , y = 'DENIED PETITIONS %', data = ratios)
rotg = v.set_xticklabels(v.get_xticklabels(), rotation = 90)


pet_state['DENIED PETITIONS'] = denied_by_state
pet_state['DENIED PETITIONS %'] = denied_state_rate
pet_state = pet_state.sort_values(by='DENIED PETITIONS %',ascending = False)
pet_state


h1b_data.JOB_TITLE.value_counts().head(15)

h1b_data['JOB_TITLE'].value_counts().head(15).plot(kind = "bar" , title ="Top 15 Jobs")