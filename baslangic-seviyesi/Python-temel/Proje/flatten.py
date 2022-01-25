# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# output: [1,'a','cat',2,3,'dog',4,5]

input = eval(input("Add a input :"))
output = []

def isSingle(t):
    if type(t) ==  str  or type(t) == float or type(t) == int:
        return True
    else:
        return False

def flatten(x):
    if isSingle(x):
        output.append(x)
    else:
        for i in x:
            flatten(i)

flatten(input)
print("Output:",output)