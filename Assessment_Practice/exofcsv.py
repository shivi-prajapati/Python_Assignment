import csv
# with open(r'C:\Users\Shivi Prajapati\Code Practice\practice_file_handling\data.csv','r')as f:
#     d=csv.reader(f)
#     next(d) #remover header key
#     for i in d:
#         print(i[0],i[1])

# with open(r'C:\Users\Shivi Prajapati\Code Practice\practice_file_handling\data.csv','r')as f:
#     d=csv.reader(f)
#     with open('demo_copy.csv','w')as g:
#         w=csv.writer(g,delimiter='-')
#         for line in d:
#             w.writerow(line)


with open(r'C:\Users\Shivi Prajapati\Code Practice\practice_file_handling\data.csv','r')as f:
    read=csv.DictReader(f)
    with open('demo_copy.csv','w')as g:
        write=csv.DictWriter(g,fieldnames=['Name','Age','City'],lineterminator='\n')
        write.writeheader()
        for line in read:
            del line['Course'],line['Marks']
            write.writerow(line)
        

