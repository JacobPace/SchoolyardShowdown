def G(n):
    if n == 1:
        return 0
    else:
        return (n-1)+G(n-1)

numOfStudents = int(input("How many students?: "))
print(G(numOfStudents))