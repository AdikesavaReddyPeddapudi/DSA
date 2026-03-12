print('   STAR PATTERN  \n ')

def star_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end='')
        print()
star_pattern(6)

def star_pattern_rev(n):
    for i in range(1,n+1):
        for j in range(i,n):
            print('*',end='')
        print()
star_pattern_rev(6)

print()

def number_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
number_pattern(5)

print()

def number_pattern1(n):
    for i in range(1,n+1):
        for j in range(i,):
            print(i,end=' ')
        print()
number_pattern1(5)
