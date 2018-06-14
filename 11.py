import re
lines_count = 0
words_count = 0
words_dict = {}

with open('dict.txt') as f:
	
		for line in f:
			if line:
				line == line.startswith('a')
				lines_count = lines_count + 1
			
print("The numbers of words beginning with 'a' is", lines_count)
				
		