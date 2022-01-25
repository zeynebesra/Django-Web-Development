# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

# input: [[1, 2], [3, 4], [5, 6, 7]]

# output: [[[7, 6, 5], [4, 3], [2, 1]]

input = eval(input("Add a input :"))

def isList(t):
    if type(t) ==  list:
        return True
    else:
        return False

def reverse(x):
    if isList(x):
        for i,e in enumerate(x):
            if isList(e):
                x[i] = e[::-1]
        x = x[::-1]
    return x
    
print("Output: ",reverse(input))