import os
import csv

csv_path=os.path.join('..','..','Pybank','Resources','budget_data.csv')
month_counter=0
total_change=0.0    
all_change=[]
all_month=[]
last_line=0.0

with open(csv_path, newline='') as csv_handler:
    csv_reader=csv.reader(csv_handler, delimiter=',')
    csv_header=next(csv_reader)
    change=0

    for row in csv_reader:
        month_counter+=1
        total_change+=int(row[1])        
        monthly_change=int(row[1])-last_line
        change+=monthly_change
        average_change=change/(month_counter*2)
        all_change.append(monthly_change)
        all_month.append(row[0])
        last_line=int(row[1])
        
        
    month_counter=month_counter
    max_change=max(all_change)
    min_change=min(all_change)
    print(all_change)
    #print(all_month)
    max_index=all_change.index(max_change)
    min_index=all_change.index(min_change)
    max_month=all_month[max_index]
    min_month=all_month[min_index]
    #print(['try this ' +str(month_counter))
    #-2196someting for min_change
    #print(len(all_change))

print(f'Total Month: {month_counter}')
print(f'Total Change: {total_change}')
print(f'Average Change: {round(average_change)}')
print(f'Max Change: {max_change} on {max_month}')
print(f'Min Change: {min_change} on {min_month}')
text_string= (
f"Total Months : {month_counter} \n"
f"Total Change: {total_change}\n"
f"Average Change: {round(average_change)}\n"
f"Max Change: {max_change} on {max_month}\n"
f"Min Change: {min_change} on {min_month}\n "
)
#text_string=f'Total Month: {month_counter}\n Total Change: {total_change}\n Average Change: {round(average_change)}\nMax Change: {max_change} on {max_month}\nMin Change: {min_change} on {min_month}'
print(text_string)
text_file=open("output.txt","w")
text_file.writelines(text_string)