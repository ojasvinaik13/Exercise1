def odd_magic_square():
    # for odd order magic squares
    i = n // 2
    j = n - 1
    mat[i][j] = 1

    for a in range(2, n ** 2 + 1):
        i = i - 1
        j = j + 1
        if (i == -1 and j != n):
            i = n - 1
        elif (j == n and i != -1):
            j = 0
        elif (i == -1 and j == n):
            i = 0
            j = n - 2

        # condition for position which is already occupied
        if mat[i][j] != 0:
            i = i + 1
            j = j - 2

        mat[i][j] = a

    print("The magic square is: ")
    for i in range(n):
        print(mat[i])

def doublyeven_magic_square():
    # for even order magic squares divisible by 4


    # Filling the matrix with numbers from 1 to n**2 in order
    for i in range(n):
        for j in range(n):
            mat[i][j]= n*i+j+1

    """The values of elements in matrices of order n/4 by n/4 at all four corners of the square and in middle matrix of order n/2 by n/2 are altered
    """

    for i in range(n//4):
        for j in range(n//4):
            mat[i][j] = (n * n + 1) - mat[i][j]

    for i in range(n//4):
        for j in range(3*n//4,n):
            mat[i][j] = (n * n + 1) - mat[i][j]

    for i in range(3*n//4,n):
        for j in range(n//4):
            mat[i][j] = (n * n + 1) - mat[i][j]

    for i in range(3*n//4,n):
        for j in range(3*n//4,n):
            mat[i][j] = (n * n + 1) - mat[i][j]

    for i in range(n//4,3*n//4):
        for j in range(n//4,3*n//4):
            mat[i][j] = (n * n + 1) - mat[i][j]

    print("The magic square is:")
    for i in range(n):
        print(mat[i])




n=int(input("Enter a number "))
print("The magic sum is %d " %(n*(n**2+1)//2))
mat=[]
for p in range(n):
    mat.append([])
for p in range(n):
    for q in range(n):
        mat[p].append(q)
        # initialise all elements to zero
        mat[p][q]=0

if(n%2!=0):
    odd_magic_square()
elif(n%4==0):
    doublyeven_magic_square()





