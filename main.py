def merge(*lists):
    
    def insertion(data): # эта функция сортирует вставками массивы
    
        for i in range(len(data)):
            j = i - 1 
            key = data[i]
            while data[j] > key and j >= 0:
                data[j + 1] = data[j]
                j -= 1
                data[j + 1] = key
    
        return data
    arrays = [i for i in lists]
    temp = []
    for k in arrays:
        for j in k:
            temp.append(j)
    return insertion(temp)

b = [1, 2, 3]
a = [4, 5, 6]

print(merge(a,b))
