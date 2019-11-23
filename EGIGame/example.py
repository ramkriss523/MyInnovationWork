def fact_fun(data):
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[i]<data[j]:
                temp = data[i]
                data[i]= data[j]
                data[j]=temp
    return data

a=5
b=6

a,b =b,a

print(a)

a = [20,10,50,33,90,45]
print(fact_fun(a))
