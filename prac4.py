n=int(input())
List=list(input())
maxim=max(List)
for i in List:
    if i==maxim:
        List.remove(maxim)
print(max(List))