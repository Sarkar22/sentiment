def strip_punctuation(stringword):
    new_words=""
    #print("Word is: ",word)
    for w in stringword:
        if w not in punctuation_chars:
            new_words=new_words+w
    return  new_words
def get_pos(stringsentence):
    pos_count=0
    strippedstringsentence=strip_punctuation(stringsentence)
    lowerstringsentence=strippedstringsentence.lower()
    splittedstringsentence=lowerstringsentence.split()
    for w in splittedstringsentence:
        if w in positive_words:
            pos_count+=1
    return pos_count
def get_neg(stringsentence):
    neg_count=0
    strippedstringsentence=strip_punctuation(stringsentence)
    lowerstringsentence=strippedstringsentence.lower()
    splittedstringsentence=lowerstringsentence.split()
    for w in splittedstringsentence:
        if w in negative_words:
            neg_count+=1
    return neg_count




punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
fh1=open('project_twitter_data.csv','r')
lines=fh1.readlines()
outfile=open('resulting_data.csv','w')
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write("\n")
for line in lines[1:]:
    newline=''
    line1=line.strip().split(',')
    y=get_pos(line1[0])
    x=get_neg(line1[0])
    z=y-x
    newline=','.join([line1[1],line1[2],str(y),str(x),str(z)])
    print(newline)
    outfile.write(newline)
    outfile.write('\n')


fh1.close()
outfile.close()
