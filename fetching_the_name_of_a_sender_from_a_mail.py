name_of_file = input ('input the name of file to fetch the mail text from\n')
Mname = open(name_of_file)
count = 0
for check in Mname:
    check = check.rstrip()
    if check.startswith('From:'):
       print(check.strip('From:'))
       count+=1
print ('there were',count,'lines with from as first word')
