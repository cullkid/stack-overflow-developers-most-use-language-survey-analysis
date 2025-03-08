import csv
from collections import Counter
from matplotlib import pyplot as plt

with open('data.csv') as csv_file:  # use open function to get the csv file
    csv_reader = csv.DictReader(csv_file)  # read or access the csv file using python DictReader

    count_language = Counter()  #  count the numbers of the each programming result from the survey

    # loop over the csv_reader and use the data to updat the count_language
    for row in csv_reader:  
        count_language.update(row['LanguagesWorkedWith'].split(';'))  # split or remove the ; to be ,

# empty list
languages = []
popularity = []

for item in count_language.most_common(15):  # loop over tuple
    languages.append(item[0])  # asign the loop into the empty langauge 
    popularity.append(item[1]) # asign the loop into the empty langauge

# print(languages)
# print(popularity)

#  reverse the data to ascesnding order
languages.reverse()
popularity.reverse()

# plot the data in bar chart, switch it horinzontally and reverse the X & Y axis
plt.barh(languages, popularity)
plt.title('Most Popula Languages Used By The Programmers According Stack-Over-Flow Survey')
plt.xlabel('Programming Languages')
plt.ylabel('Number of poeple that use them')
plt.grid(axis='x')
plt.show()