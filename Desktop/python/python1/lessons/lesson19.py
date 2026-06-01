def abubakr(*param):
    if len(param)==1:
        start=0
        stop=param[0]
        step=1
    elif len(param)==2:
        start=param[0]
        stop=param[1]
        step=1
    elif len(param)==3:
        start=param[0]
        stop=param[1]
        step=2
    else:
        raise TypeError('Error params max param 3 start stop step')
    
    if step==0:
        raise ValueError('Error step')
    
    if start<stop:
        i=start
        while i<stop:
            yield i
            i+=step
    else:
        if step>0:
            step=step*-1
        i=stop
        while i<start:
            yield i
            i-=step

for i in abubakr(20,1,-5):
    print(i)
#yield ба мисли генератор аст ки якто якто бар мегардонад.