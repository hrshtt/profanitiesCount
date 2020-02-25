# list of dummy profanities in lower case
profanities = ['a', 'psychology', 'how', 'are', 'the']

#dictionary to hold profanity count for each line
profanitiesCount = {}

#dummy text file holds a wikipedia article
comments_file = 'textfile.txt'

#ASSUMPTION: we have been given a text file
#reading the comments file in lowercase
with open(comments_file, 'r') as f:
  comments_txt = f.read().lower()
f.close()

#ASSUMPTION: the seperator for each comment is '\n'
#for each line in the comments text file count profanities
for i, comment in enumerate(comments_txt.strip().splitlines()):
  
  #ASSUMPTION: the total count of profanities in a sentence is
  # enough to signify sentence's profanity
  #The dictionary gets the total profanity count for each line
  profanitiesCount[i] = sum([comment.count(word) for word in profanities])

print(profanitiesCount)
