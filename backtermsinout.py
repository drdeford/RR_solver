import math

import numpy as np 

def backterms(initial,coeffs):
    ans=[]
    
    order = len(coeffs)
    element = initial[-1]
    
    for k in range(order-1):
        element = element - coeffs[k]*initial[-(k+2)]
    
    element = element / coeffs[-1]
    

    return element

def backrr(num,initial,coeffs):
    ans = []
    for i in range(num):
        ans.append(backterms(initial,coeffs))
        initial.pop()
        initial.insert(0,ans[-1])

    return ans

def forterms(initial,coeffs):
    ans=[]
    #coeffs.reverse()
    order = len(coeffs)
    element = 0
    for k in range(order):
        element = element + coeffs[k]*initial[-(k+1)]
        

    return element

def forrr(num,initial,coeffs):
    ans = []
    #coe=coeffs[:]
    for i in range(num):
        ans.append(forterms(initial,coeffs))
        initial.reverse()
        initial.pop()
        initial.reverse()
        initial.append(ans[-1])
        #coeffs=coe
    return ans

def bothways(num,initial,coeffs):
    init=initial[:]
    initr=initial[:]
    eigs=[]
    disp=[]
    disp2=[]
    eigs=roots(coeffs)
    gps=findcoeffs(initial,eigs)
    c=init[:]
    coe=coeffs[:]
    a=forrr(num,initial,coeffs)
    b=backrr(num,init,coe)
    b.reverse()
    b=[b]
    b.append(c)
    b.append(a)
    charmat=[]
    for i in range(len(coeffs)-1):
        charmat.append([])
        for j in range(i+1):
            charmat[-1].append(0)
        charmat[-1].append(1)
        for k in range(len(coeffs)-2-i):
            charmat[-1].append(0)
    coeffs.reverse()
    charmat.append(coeffs)
    print('\nThe sequence is: \n')
    print(b)
    print('\nThe companion matrix is:\n')
    for i in range (len(charmat)):
        print(charmat[i])
    print('\nThe eigenvalues are:\n')
    for i in range(len(eigs)):
        print(eigs[i])
    print('\nThe G.P.S. is:\n')
   # for i in range(len(gps)):
      #  disp.append(gps[i],eigs[i])
    print(gps[0],'*(',eigs[0],')^n')
    for i in range(len(gps)-1):
        print('+',gps[i+1],'*(',eigs[i+1],')^n')
    print('\n')
    return b,charmat,initr, coeffs,eigs,gps
##def findbasisn(order, rangea,coeffs):
##    a=[]
##    b=[]
##    for i in range(order):
##        a.append([])
##        for j in range(rangea):
##            a[-1].append(j)
##    t=bothways(5,[a],coeffs)
##    if t[0][1][1]==t[0][0][-1] and t[0][1][2] == t[0][0][-2] and t[0][1][3] == t[0][0][-3]:
##        
##    
##            
##

def forrrr(num,initial,coeffs):
    ans = []
    init=initial[:]
    #coe=coeffs[:]
    for i in range(num):
        ans.append(forterms(initial,coeffs))
        initial.reverse()
        initial.pop()
        initial.reverse()
        initial.append(ans[-1])
        #coeffs=coe
    ans.reverse()
    ans.append(init)
    ans.reverse()
        
        
    return ans

def roots(init):
    vec=[1]
    
    for i in range(len(init)):
        vec.append(-init[i])
    alpha=np.roots(vec)
    return alpha

def findcoeffs(init, eigs):
    mat=[]
    gps=[]
    for i in range(len(init)):
        mat.append([])
    for i in range(len(init)):    
        for j in range(len(init)):
            mat[i].append(eigs[j]**i)

    newmat=np.array(mat)
    newinit=np.array(init)
    x=np.linalg.solve(newmat,newinit)
    for k in range(len(x)):
        gps.append(x[k])

    return gps

def botheigs(num, eigs,init):
    charpoly=np.poly(eigs)
    temp=[]
    for i in range(len(charpoly)-1):
        temp.append(-charpoly[i+1])
    print('\nThe coefficients are:\n')
    print(temp)
    a=bothways(num,init,temp)
    

    return a
        
def bothgps(num,eigs,coeff):
    init=[]
    var=0
    for i in range(len(eigs)):
        var=0
        for j in range(len(eigs)):
            var=var+(coeff[j]*(eigs[j]**i))
        init.append(var)
    print('The initial conditions are:\n')
    print(init)
    a=botheigs(num,eigs,init)

    return a
