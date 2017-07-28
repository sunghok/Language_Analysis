from collections import Counter

def count_words(text):
	text = text.lower()
	skips = [".",",",";",":","'",'"']
	for ch in skips:
		text = text.replace(ch, "")

	word_counts = Counter(text.split(" "))
	return word_counts


def read_book(title_path):
	"""
	Read a book and return it as a string
	"""
	with open(title_path, "r", encoding="utf8") as current_file:
		text = current_file.read()
		text.replace("\n","").replace("\r","")
	return text


def word_stats(word_counts):
	"""Return # of unique words and word frequencies"""
	num_unique = len(word_counts)
	counts = word_counts.values()
	return(num_unique,counts)


import os
book_dir = "./Books"


import pandas as pd
stats = pd.DataFrame(columns = ("language","author","title","length","unique"))
title_num = 1


for language in os.listdir(book_dir)[1:]:
	for author in os.listdir(book_dir + "/" + language)[1:]:
		for title in os.listdir(book_dir + "/" + language + "/" + author)[1:]:
			inputfile = book_dir + "/" + language + "/" + author + "/" + title
			# print(inputfile)
			text = read_book(inputfile)
			(num_unique, counts) = word_stats(count_words(text))
			
			stats.loc[title_num] = language, author.capitalize(), title.replace(".txt",""), sum(counts), num_unique  
			title_num +=1

stats
stats.head()
stats.tail()

#select the column
stats.length     
stats.unique

print(stats.length)










import matplotlib.pyplot as plt
plt.plot(stats.length, stats.unique, "bo")     # (x,y, marker)
plt.loglog(stats.length, stats.unique, "bo")     
# print(plt.show())


plt.figure(figsize = (10,10))

subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label="English", color ="crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label="French", color ="forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label="German", color ="orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label="Portuguese", color ="blueviolet")

plt.legend()      							#add legend
plt.xlabel("Book length")
plt.ylabel("Number of unique words")

plt.savefig("lang_plot.pdf")				#save as a pdf file






