l = [0,1,2,3,4,5,6,7,8]
fh= []
sh=[]
final=[]
c = len(l)
if c%2==0:
  for i in range(0,c//2):
    fh.append(l[i])
  for j in range(c//2,c):
    sh.append(l[j])
  final.extend(sh)
  final.extend(fh)
  print(final)
else:
  for i in range(0,c//2):
    fh.append(l[i])
  for j in range(c//2+1,c):
    sh.append(l[j])
  final.extend(sh)
  final.append(l[c//2])
  final.extend(fh)
  print(final)
  

