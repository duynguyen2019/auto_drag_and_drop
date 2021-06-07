def my_sum(test,test2,*args, **kwargs):
    result = ""
    for x in args:
        result += str(x)
    return result

print(my_sum('test1','test2','test3',22,12,1,3,"test4"))