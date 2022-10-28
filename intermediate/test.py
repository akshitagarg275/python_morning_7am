# 1:A:0, 2:B:1, 3:C:1, 4:D:2, 5:E:2, 6:F:3 - input string 
# Output: 
#A - B,C 
# B - D,E 
# C - F 
#D - 
# E - 
#F -

str1="1:A:0,2:B:1,3:C:1,4:D:2,5:E:2,6:F:3" 
n=str1.split(",") 
print(n) 
n1=[]
for i in range(len(n)):
     n1.append(n[i].split(":")) 
     print(n1) 
     t={} 
     while(1): 
        for i in range(len(n)): 
            n2=[] 
            for j in range(len(n)):
                if n1[i][0]==n1[j][2]:
                    n2.append(n1[j][1])
            t[n1[i][1]]=n2
            break 
        print(t)