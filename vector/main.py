from vector import Vector

if __name__ == '__main__':
    

    a = Vector(1, 2, 3)
    b = Vector(3, 4, 5)

    print(a*0.5)
    print(2*a)

    print(a*a)
    print(a.inner(b))


    print(a.abs())

    print(a.normalize())

    print(a-b)

    print(b-a)

    e1=Vector(1,0,0)
    e2=Vector(0,1,0)

    print(e1 @ e1)

    print(e1 @ e2)

    print(e2 @ e1)

    c = Vector(1)

    d = Vector(1, 0)

    print(len(c))
    
    print(len(d))


    print(a, c)

    k = Vector()
    k += a
    print(k)
    print(-a)
    k += a
    print(k, a)
    a = a + a
    print(a)
    print(repr(a))
    print(repr(c))
    p = Vector(1, 3, -4)
    p = -p
    print(p)
    print(repr(p))
    p += p
    print(p)
    p -= Vector(-1,-3,4)
    print(p)
    p @=p
    print(p)
    p = Vector(1, 3, -4)
    p *= 3
    print(p)
