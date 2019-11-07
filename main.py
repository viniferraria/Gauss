def gauss(n,M):
  for i in range(0,n-1):
    p = i
    p = min(i, M[p][i])
    if p == 0:
      break
    if p != i:
      M[p], M[i] = M[i], M[p]
    for j in range(i+1,n):
      m = M[j][i]/M[i][i]
      M[j][i] -= m*M[j][j]
      print(M)
  return M

def resolver(n,M):
  if M[n-1][n] == 0:
    return "Solução Inexistente"
  x = [0]*n
  x[n-1] = M[n-1][n]/M[n-1][n-1]
  print("x = ", x[n-1])
  if x[n-1] ==  0:
    print("Solução inexistente")
  else:
    for i in range(n-1,1,-1):
      soma = 0
      for j in range(i+1,n):
        soma += M[i][j]*x[j]  
      x[i] = (M[i][n]-soma)/M[i][i]
    return x

M = [[2,0,0,0,3],[1,1.5,0,0,4.5],[0,-3,0.5,0,-6.6],[2,-2,1,1,0.8]]
n = len(M)
print(resolver(n,gauss(n,M)))
