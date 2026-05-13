from collections import deque
dq=deque()

# Inserting Elements
dq.append(10)
dq.append(20)
dq.appendleft(5)
print(" Deque After inserting : ",dq)

# delete Elements
dq.pop()
print(" After pop : ",dq)
dq.popleft()
print("After popleft :",dq)

#Add more Elements

dq.append(30)
dq.append(40)

print("Final deque :",dq)

#Accessing the Elements in the deque

print("Front Element : ", dq[0])
print("Rear element : ",dq[-1])

#Size

print("Size of the Deque : ",len(dq))

