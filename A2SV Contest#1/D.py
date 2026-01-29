a,b = map(int,input().split())
#This answer exceeds time limit, so I want to try another approach using binary search or somthing 
#arr = []
#[arr.append(i+1) for i in range(a) if (i+1)%2 ==1]
#[arr.append(c+1) for c in range(a) if (c+1)%2 ==0]
#print(arr[b-1])
mid = (a+1)//2
if b <= mid:
    print(2*b -1)
else:
    EvenPositition = b-mid
    print(2*(EvenPositition)) 