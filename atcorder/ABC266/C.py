Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

import math
import numpy as np

#角度計算開始
def kakudo(x0,y0,x1,y1,x2,y2):
    vec1=[x1-x0,y1-y0]
    vec2=[x2-x0,y2-y0]
    absvec1=np.linalg.norm(vec1)
    absvec2=np.linalg.norm(vec2)
    inner=np.inner(vec1,vec2)
    cos_theta=inner/(absvec1*absvec2)
    theta=math.degrees(math.acos(cos_theta))
    k = round(theta,2)
    # print(k)
    return k

# A
akakudo = kakudo(Ax,Ay,Dx,Dy,Bx,By)
if Cx < Ax and Ax < Bx and Ax < Dx:
    akakudo = 360 - akakudo
ans = akakudo < 180

# B
if ans:
    ans = kakudo(Bx,By,Ax,Ay,Cx,Cy) < 180

# C
if ans:
    ans = kakudo(Cx,Cy,Bx,By,Dx,Dy) < 180

# D
if ans:
    ans = kakudo(Dx,Dy,Ax,Ay,Cx,Cy) < 180

if ans:
    print("Yes")
else:
    print("No")
