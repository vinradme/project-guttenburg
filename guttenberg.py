# Reading and printing the lines of the file

myfile = open('ran.txt', 'r')
lines = myfile.readlines()
print lines
myfile.close()

# Reading the file in binary mode 


with open('ran.txt', 'rb') as f:
	byte = f.read(1)
	print byte
	while byte:
		byte = f.read(1)
		print byte

# Counting the number of occurences of
# great good adventure the while

great_count = 0
good_count = 0
adventure_count = 0
the_count = 0
while_count = 0


with open('ran.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line_list = line.split()
        for word in line_list:        
		if word.lower() == "great":
			great_count += 1
		elif word.lower() == "good":
			good_count += 1
                elif word.lower() == "adventure":
                        adventure_count += 1
                elif word.lower() == "the":
                        the_count += 1
                elif word.lower() == "while":
                        while_count += 1

print "the value for count of great: %d" % (great_count)
print "the value for count of good: %d" % (good_count)
print "the value for count of adventure: %d " % (adventure_count)
print "the value for count of the: %d" % (the_count)
print "the value for count of while: %d" % (while_count)



