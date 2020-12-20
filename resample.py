# Data Formatting
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df=df.set_index('Formatted Date')
df.head(10)
#Resampling
df1 = df[['Apparent Temperature (C)', 'Humidity']] .resample('MS').mean()
df1.head(10)
import seaborn as sns
import warnings
warnings.filterwarnings ("ignore") 
plt.figure (figsize=(14,6))
plt.title ("Variation in Apparent Temperature and Humidity with time")
sns.lineplot (data=df1)

