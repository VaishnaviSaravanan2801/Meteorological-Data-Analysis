# Data Analysis
Jan = df1[df1.index.month==1] #retrieving jan
print(Jan)
Jan.dtypes
Feb = df1[df1.index.month==2]
print(Feb)
Feb.dtypes
March = df1[df1.index.month==3]
print(March)
March.dtypes
.
.
.
.
Dec= df1[df1.index.month==12]
print(Dec)
Dec.dtypes
# Data Visualization 
Jan.plot(kind='line',marker='o') #Jan
plt.xlabel("Year")
plt.title("January")
Feb.plot(kind='line',marker='o') #Feb
plt.xlabel("Year")
plt.title("February")
Dec.plot(kind='line',marker='o') #Dec
plt.xlabel("Year")
plt.title("December")
