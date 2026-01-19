ms,cs,es=map(int,input().split())
p=(ms+cs+es)//3
print(p)
if p>80:
    print('学校1')
elif p>50:
    print('学校2')
elif p>30:
    print('学校3')
else:
    print('学校4')
