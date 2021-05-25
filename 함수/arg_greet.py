
# def greet(*names):
#     print(names)
#     for i in names :
#         print(i)

# greet('a','b','c')




# def foo(*args):
#     print('인쟈의 개수:',len(args))
#     print('인자들 :',args)

# foo(10,20,30)




def sum_nums(*args):
    sum=0
    mean=0
    print(len(args),'개의 인자',args)
    for i in args :
        sum=sum+i
    mean=sum/len(args)
    print('합계 :',sum)
    print('평균 :',mean)

sum_nums(10,20,30)
sum_nums(10,20,30,40)