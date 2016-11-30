def rekursion(x,y):
    if(x==1):
        return x
    else:
        if(y==1):
            return x
        else:
            x=x*x
            return rekursion(x,y-1)
    return x

zahlx = int(input())
zahly = int(input())

rekursion(zahlx,zahly)