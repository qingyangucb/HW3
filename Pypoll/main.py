import os
import csv

csv_path=os.path.join('..','..','Pypoll','Resources','election_data.csv')
with open(csv_path, newline='') as csv_handler:
    csv_reader=csv.reader(csv_handler, delimiter=',')
    csv_header=next(csv_reader)
    candidate=[]
    unique=[]
    
    for row in csv_reader:
        candidate.append(row[2])
        
    for name in candidate:
        if name not in unique:
            unique.append(name)

         
length_1=len(unique)
count=[0] *length_1  
length_2=len(candidate)

for i in range(length_1):
    for j in range(length_2):
        if unique[i]==candidate[j]:
            count[i]+=1
#print(unique)            
#print(count)   

#print(count)   
total_vote=sum(count)
#print(total_vote)
percent=[round(x/total_vote*100,4) for x in count]
# for x in percent:
#     print(str(x)+"%")

max_val=max(count)
max_index=count.index(max_val)
winner=unique[max_index]
length=len(count)
string=[]
for i in range(0, length):
    max_val=max(count)
    max_index=count.index(max_val)
    string.append(f'{unique.pop(max_index)}: {percent.pop(max_index)}% ({count.pop(max_index)})\n')
  
   
string.append(f'Winner: {winner}')
for x in string:
    print(x)

text_file=open("output.txt","w")
text_file.writelines(string)