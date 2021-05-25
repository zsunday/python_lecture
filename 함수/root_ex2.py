# def root_ex(a,b,c):
#     x_1=(-b+(b**2-4*a*c)**0.5)/2*a
#     x_2=(-b-(b**2-4*a*c)**0.5)/2*a

#     return x_1,x_2

# a=int(input('이차항의 계수'))
# b=int(input('일차항의 계수'))
# c=int(input('상수항'))

# x1, x2 =root_ex(a,b,c)
# print(f'해는 {x1} 또는 {x2}')


# def print_sum():
#     global a,b
#     a=100
#     b=200
#     result=a+b
#     print('print_sum() 내부 :',a'과', b, '의 합은', result, '입니다.')

# a=10
# b=20
# print_sum()
# result=a+b
# print('print_sum() 외부:',a'과',b,'의 합은',result,'입니다.')


# def print_star(n=1):
#     for _ in range(n):
#         print('**************************')

# print_star()

def greet(*names):
    for i in names :
        print(i)

greet('a','b','c')