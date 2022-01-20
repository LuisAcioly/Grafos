num = int(input())
peças = {}
vetor = []
print(peças)
for i in range(num):
    p1, p2 = input().split()
    if(p1 in peças):
        peças[p1].append(p2)
    else:
        vetor = [p2]
        peças.update({p1 : vetor})

print(peças)

for j in peças.keys():
    print(j)
