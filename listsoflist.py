#studentsList= [['fred','12','13','14'],['joe','4','2','3'],['jane','4','7','8']]

f = open('students.txt','r')
fileContents=f.readlines()
print(fileContents)
f.close()

for item in studentsList:
        print(item)
        ave = (int(item[1])+ int(item[2])+int(item[3]) )/3
        ave=round(ave,2)
        item.append(ave)
        m=max(int(item[1]),int(item[2]),int(item[3]))
        item.append(m)
print(studentsList)

