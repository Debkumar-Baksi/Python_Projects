def dot_product(x,y):
    sum_dot_product=0
    for i in range(len(x)):
        sum_dot_product+=x[i]*y[i]
    return sum_dot_product

def absolute_value(x):
    sum_absolute_value=0
    for i in range(len(x)):
        sum_absolute_value+=x[i]**2
    return (sum_absolute_value)**0.5

def similarity(x,y):
    similarity_value=dot_product(x,y)/(absolute_value(x)*absolute_value(y))
    return similarity_value

def similarity_matrix(matrix):
    new_matrix=[]
    for i in range(len(matrix)):
        row=[]
        for j in range(len(matrix)):
            row.append(similarity(matrix[i],matrix[j]))
        new_matrix.append(row)
    return new_matrix


def predict(user_index,item_index,rating_matrix,similarity_matrix):
    numerator=0
    denominator=0
    for i in range(len(rating_matrix)):
        if i!=user_index and rating_matrix[i][item_index]!=0:
            numerator+=similarity_matrix[user_index][i] * rating_matrix[i][item_index]
            denominator+=similarity_matrix[user_index][i]
    result=numerator/denominator
    return result

u1=[4,0,2,5,0]
u2=[0,3,0,4,2]
u3=[5,0,4,0,3]
u4=[2,5,0,3,0]

rating=[u1,u2,u3,u4]

user_index=3
item_index=4
rating_matrix=rating
new_similarity_matrix=similarity_matrix(rating)
print(predict(user_index,item_index,rating_matrix,new_similarity_matrix))
