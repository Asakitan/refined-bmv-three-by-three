"""Exact coefficient certificate over Z[b,c], using only Python integers."""
from math import comb


class Poly(dict):
    """Key 256*i+j denotes b^i c^j. No carry: total degrees are <= 144."""
    def plus(self, other, factor=1):
        res = Poly(self)
        for k,v in other.items():
            res[k] = res.get(k,0)+factor*v
            if not res[k]:
                del res[k]
        return res

    def __mul__(self, other):
        res=Poly()
        for i,x in self.items():
            for j,y in other.items():
                res[i+j]=res.get(i+j,0)+x*y
        return Poly((k,v) for k,v in res.items() if v)

    def __pow__(self, power):
        out=one
        for _ in range(power):
            out=out*self
        return out


one=Poly({0:1})
hom_y=Poly({0:1,256:1})
hom_z=Poly({0:1,256:1,1:1})
EXPECTED={5:3701,6:515,7:7400,8:9722,9:1262}


def verify(n):
    k=1 if n%3==0 else 3
    assert 6*n*k<256
    xyz=(one,hom_y,hom_z)
    powers=[[p**i for i in range(k*n+1)] for p in xyz]
    def gap(i,j,l):
        out=Poly()
        for r in range(n+1):
            for s in range(n-r+1):
                out=out.plus(powers[i][k*r]*powers[j][k*s]*powers[l][k*(n-r-s)])
        e=k*n//3
        return out.plus(powers[i][e]*powers[j][e]*powers[l][e],-comb(n+2,2))
    A=gap(0,0,2); B=gap(1,1,2); H=gap(0,1,2)
    Q=(gap(1,1,0)*gap(2,2,0)).plus(gap(0,0,1)*gap(2,2,1))
    D=(H**2).plus(A*B,-1)
    T=(H*A.plus(B)).plus(A*B,2)
    poly=(Q*T**2).plus((D**2)*(A.plus(B)**2),-1)
    if len(poly)!=EXPECTED[n] or min(poly.values())<=0:
        raise ArithmeticError(f"Certificate failed for n={n}")
    print(f"n={n}: {len(poly)} positive integer coefficients, no negatives.")


if __name__=='__main__':
    for n in EXPECTED:
        verify(n)
