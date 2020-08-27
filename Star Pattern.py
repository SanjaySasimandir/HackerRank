'''
* * * * *  * * * * *
* * * *      * * * *
* * *          * * *
* *              * *
*                  *
*                  *
* *              * *
* * *          * * *
* * * *      * * * *
* * * * *  * * * * *
'''
def pattern(n): 
    list = [] 
    for i in range(n,0,-1): 
        list.append("*"*i+' '*(n-i)) 
    for i in range(len(list)):
        line=" ".join(list[i])
        print(line,'',line[::-1])
    for i in range(len(list)-1,0,-1):
        line=" ".join(list[i])
        print(line,'',line[::-1])
    print(" ".join(list[0]),''," ".join(list[0]))

pattern(int(input())) 