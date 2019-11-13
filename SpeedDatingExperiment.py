#importing packages
import pandas as pd
pd.options.display.max_rows = 1000 
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


#importing data
dataset = pd.read_csv('SpeedDatingData.csv', encoding="ISO-8859-1")
dataset.head(5)
dataset.isnull().sum()

#age distribution - izbrisi
#age = dataset[np.isfinite(dataset['age'])]['age']
#plt.hist(age.values)
#plt.xlabel('Age')
#plt.ylabel('Frequency')

#number of people who matched -treba li ovo?
pd.crosstab(index=dataset['match'],columns='count')

#narrowing dataset
dataset1 = dataset.iloc[:, 12:28] #ovako je ocijenjen od partnera + match
dataset2 = dataset.iloc[:, 30:33] #da li bi ga partner ponovo vidio
dataset3 = dataset.iloc[:, 48:67] #zajednicki interesi
dataset4 = dataset.iloc[:, 69:74] #sta je bitno kod partnera
dataset5 = dataset.iloc[:, 87:91] #misljenje ispitanika o samom sebi
dataset6 = dataset.iloc[:, 97:104] #kako je ocijenio partnera
dataset7 = dataset.iloc[:, 104:107] #da li mu se svidio partner, da li bi se sreli

#correlation svih
date11 = pd.concat([dataset.iloc[:, 2],dataset1,dataset2,dataset3,dataset4,
                 dataset5,dataset6,dataset7], axis=1)

#removing null values
date12=date11.dropna()

plt.subplots(figsize=(30,20))
ax=plt.axes()
ax.set_title("Mapa korelacije")
corr=date12.corr()
sns.heatmap(corr, xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,vmin=-1,vmax=1,annot=True) #annot=True za prikazivanje brojeva

#correlation ocjena od partnera, match + zajednicki interesi
date21=pd.concat([dataset.iloc[:,2],dataset1,dataset2,dataset3,dataset4],axis=1)
date22=date21.dropna()

plt.subplots(figsize=(20,20))
ax2=plt.axes()
ax2.set_title("Mapa korelacije 3")
corr2=date22.corr()
sns.heatmap(corr2, xticklabels=corr2.columns.values,
            yticklabels=corr2.columns.values,vmin=-1,vmax=1,annot=True) 


#correlation match+ zajednicki intersi 
date31=pd.concat([dataset.iloc[:,12],dataset3],axis=1)
date32=date31.dropna()

plt.subplots(figsize=(10,10))
ax3=plt.axes()
ax3.set_title("Mapa korelacije 3")
corr3=date32.corr()
sns.heatmap(corr3, xticklabels=corr3.columns.values,
            yticklabels=corr3.columns.values,vmin=-1,vmax=1,annot=True) 


#korelacija match sa pozicijom i dec 23 97
plt.subplots()
ax1=plt.axes()
ax1.set_title("Mapa korelacije 2")
#DODAJ JOS DEC
orderdata=pd.concat([dataset.iloc[:,9],dataset.iloc[:,12], 
                     dataset.iloc[:,30],dataset.iloc[:,104], 
                     dataset.iloc[:,97], dataset.iloc[:,23]],axis=1)
order=orderdata.dropna()
korel=order.corr()
sns.heatmap(korel,xticklabels=korel.columns.values,
            yticklabels=korel.columns.values,vmin=-1,vmax=1,annot=True)

#scatter plotovi - polovi i osobine
sns.set(style="ticks", color_codes=True)
dateplot = pd.concat([dataset6.iloc[:, 1:7],dataset.iloc[:,2]],axis = 1)
p = sns.pairplot(dateplot, hue="gender")

#OLS
dataset100=pd.concat([orderdata,dateplot], axis=1) #osobine+order+dec,match..
dataset101=dataset100.dropna()

#OLS u vezi reda - provjeri
#x = dataset100.order
#y = dataset100.dec
#o = sm.OLS(y, x)
#res = o.fit()
#res.summary()


#OLS u vezi osobina i odluke - provjeri
x = dataset101[['attr','sinc','intel','fun', 'amb', 'shar', 'order']]
y = dataset101.dec
o = sm.OLS(y, x)
res = o.fit()
res.summary()


#isto, samo match
x = dataset101[['attr','sinc','intel','fun', 'amb', 'shar','like', 
               'like_o', 'order']]
y = dataset101.match
o = sm.OLS(y, x)
res = o.fit()
res.summary()
