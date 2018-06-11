#Quiz 1: Multiplying a Matrix by a Vector

# matVec takes in a matrix and a vector and returns the Matrix-Vector Multiply
def matVec(matrix,vector):
  '''
  Python starts by taking the first value of the matrix (value:x) and multiplying it by the first value of the vector (value:y). It continues this until the first row of the matrix has been used at least once, it then adds the products ("+=") and uses the sum as a answer ("answer.append(product)"). Python repeats ("return") this until the code is satisfied.
  '''
  #Line 9-18 tells python how to find the product:
  answer = []
  for x in range(len(matrix)):
    product = 0
    for y in range(len(vector)):
      #This is where python executes the product:
      product += matrix[x][y] * vector[y]
    #Puts most recent answer at the end of the solution with "append": 
    answer.append(product)
  #Repeat until the product is complete (by using "return"):
  return answer

# Values of the matrix and vector:
matrix1 = [[1, 2, 3], [4, 5, 6]]
vector1 = [7, 8, 9]

matrix2 = [1, 3, 4]
vector2 = [[1,1,1],[2,2,2],[3,3,3]]

matrix3 = 'test'
vector3 = 3

#print means compute the value
print(matVec(matrix1,vector1))    
#print(matVec(matrix2,vector2))
#print(matVec(matrix3,vector3))