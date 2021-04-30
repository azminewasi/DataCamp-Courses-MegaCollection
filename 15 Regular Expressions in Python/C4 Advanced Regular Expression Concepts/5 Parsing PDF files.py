"""Parsing PDF files
You now need to work on another small project you have been delaying. Your company gave you some PDF files of signed contracts. The goal of the project is to create a database with the information you parse from them. Three of these columns should correspond to the day, month, and year when the contract was signed.
The dates appear as Signed on 05/24/2016 (05 indicating the month, 24 the day). You decide to use capturing groups to extract this information. Also, you would like to retrieve that information so you can store it separately in different variables.

You decide to do a proof of concept.

The variable contract containing the text of one contract and the re module are already loaded in your session. You can use print() to view the data in the IPython Shell.

Instructions 1/3
35 XP
1
2
3
Instructions 1/3
35 XP
1
2
3
Write a regex that captures the month, day, and year in which the contract was signed. Scan contract for matches."""

# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}
# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))