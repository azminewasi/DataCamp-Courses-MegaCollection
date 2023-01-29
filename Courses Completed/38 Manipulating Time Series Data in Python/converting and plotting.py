data = pd.read_csv('nyc.csv')

# Inspect data
print(data.info())

# Convert the date column to datetime64
data.date=pd.to_datetime(data.date)

# Set date column as index
data.set_index('date',inplace=True)

# Inspect data 
print(data.info())

# Plot data
data.plot(subplots=True) 
plt.show()
