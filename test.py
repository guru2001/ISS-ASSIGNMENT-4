ans1=[[0,0,0,0,0,1,1],[0.5,0.5,1,0,0,0,0],[0.5,0.5,0,1,0,0,0],[0,0,0,0,1,0,0]]
ans2=[[0,0.33,0,0.5,0],[0,0,1,0,0],[1,0,0,0.5,0],[0,0.33,0,0,1],[0,0.33,0,0,0]]
ques1 = []
ques2 = []
print("input the first list by space separated numbers and new lines for Emission Matrix")
for i in range(0,4):
    ques1.append([float(j) for j in input().split()])
print("input the second list by space separated numbers and new lines for Transition Matrix")
for i in range(0,5):
    ques2.append([float(j) for j in input().split()])
out1 = []
out2 = []
flag1=0
flag2=0
for i in range(0,4):
    for j in range(0,7):
        if ans1[i][j] == ques1[i][j]:
            out1.append('c')
        else:
            out1.append('x') #and flag1=1
            flag1=1 	
    out1.append('][')
for i in range(0,5):
    for j in range(0,5):
        if(ans2[i][j] == ques2[i][j]):
            out2.append('c')
        else:
            out2.append('x') 
            flag2=1
    out2.append('][')
print(out1)
print(out2)
if flag1==1:
    print("The Emission Matrix is incorrect.The correct matrix is")
    print(ans1)
if flag2==1:
    print("The Transition Matrix is incorrect.The correct matrix is")
    print(ans2)
if flag1==0 and flag2==0:
    print("Kudos! Correct Answer")

