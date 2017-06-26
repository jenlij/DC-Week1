my_list = [6,2,5,1,3,4,8,2,3]

#sum numbers
# my_list_sum = 0
# for i in my_list:
#     my_list_sum += i
# print "sum:", my_list_sum

#largest number
# current_max = my_list[0]
# for i in my_list:
#     if i > current_max:
#         current_max = i
# print current_max        
         
#smallest number
# current_min = my_list[0]
# for i in my_list:
#     if i < current_min:
#         current_min = i
# print current_min   

#even numbers
# for i in my_list:
#     if i % 2 == 0:
#         print i

#positive numbers
# list2 = [-1, -6, 0, 2, 9, 3]
# for i in list2:
#     if i > 0:
#         print i

# #positive numbers II
# list3 = []
# for i in list2:
#     if i > 0:
#         list3.append(i)
# print list3        

# #multiply a list
# factor = 3
# newlist = []
# for i in my_list:
#     newlist.append(factor * i)
# print newlist

#multiply vectors
# vec1 = [2,4,5]
# vec2 = [2,3,6]
# newvec = []
# j = 0
# for i in vec1:
#     newvec.append(i * vec2[j])
#     j += 1
# print newvec    

#matrix addition
# twoD1 = [[1, 3],
#          [2, 4]]
# twoD2 = [[5, 2],[1, 0]]

# new_matrix = []
# i=0
# for row in twoD1:
#     new_row = []
#     j = 0
#     for value in row:
#         new_row.append(value + twoD2[i][j])
#         j += 1
#     new_matrix.append(new_row)
#     i += 1    
# print new_matrix  

#matrix addition II
# matrix1 = [[1,2,3],[3,4,3],[5,6,3]]
# matrix2 = [[7,8,3],[9,10,3],[11,12,3]]
# #[[8,10,6],[12,14,6],[16,18,6]]
# new_matrix = []
# i=0
# for row in matrix1:
#     new_row = []
#     j = 0
#     for value in row:
#         new_row.append(value + matrix2[i][j])
#         j += 1
#     new_matrix.append(new_row)
#     i += 1    
# print new_matrix  


#de-dup
# dups = [5,1,2,3,3,5,4,3,6]
# newlist = list(set(dups))
# print newlist

#matrix mult (2x2)
a = [[2, -2],
     [5, 3]]
b = [[-1, 4],
     [4, -6]]
c = [["na","na"],["na","na"]] #[[-10, 20],[7, 2]]

# (n * m)(m * p) = (n * p)
# c[0][0] = summation (a[0][m] * b[m][0]) from 0 to m 
# c[0][1] = summation (a[0][m] * b[m][1]) from 0 to m
# c[0][p] = summation(a[0][m] * b[m][p]) from 0 to m, and 0 to p
# c[n][p] = summation( a[n][m] * b[m][p])

# c[0][0] = a[0][0]*b[0][0] + a[0][1]*b[1][0]
# c[0][1] = a[0][0]*b[0][1] + a[0][1]*b[1][1]
# c[1][0] = a[1][0]*b[0][0] + a[1][1]*b[1][0]
# c[1][1] = a[1][0]*b[0][1] + a[1][1]*b[1][1]

n = 0
while n < 2:
    p = 0
    while p < 2:
        c[n][p] = (a[n][0]*b[0][p]) + (a[n][1]*b[1][p])
        p += 1    
    n += 1
print c