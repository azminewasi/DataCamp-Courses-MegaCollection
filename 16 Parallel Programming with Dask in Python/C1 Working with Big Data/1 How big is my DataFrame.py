"""How big is my DataFrame?
A DataFrame of daily weather data from The Weather Underground is provided for you as df. Your job is to determine the exact amount of memory used (in kilobytes) to store the DataFrame in entirety.

You can use either df.info() or df.memory_usage() to determine this value. Remember that df.memory_usage() will return memory usage in bytes and the value must be divided by 1024 to convert to kilobytes (KB). This DataFrame has at least one column of text.

Instructions
50 XP
Possible Answers

2.9 KB

100.9 KB

65.8 KB

23.6 KB"""

print(df.memory_usage())