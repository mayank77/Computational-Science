import math as mt
result = []
result.append(0.57735)


def eval_fx(x):
    return mt.pow(x,3) - x - 5


def eval_fx_diff(x):
    return (3*mt.pow(x,2)) - 1


def eval_f(x,count):
    return result.append(result[count-1] - (eval_fx(x)/eval_fx_diff(x)))


print('i'+'\t\t'+'x'+'\t\t'+'f(x)')

for i in range(1,50):
    eval_f(result[i-1],i)
    if (eval_fx(result[i-1]) * eval_fx(result[i])) < 0:
        a = result[i-1]
        b = result[i]
for i in range(1,50):
    c=(a+b)/2
    if (eval_fx(a) * eval_fx(c)>0):
        a=c
    if (eval_fx(b) * eval_fx(c)>0):
        b=c
    if (eval_fx(c)==0):
        print("Exact Root",c)
print(c)