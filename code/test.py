from datetime import datetime
t1 = datetime.utcnow()
for i in range(100000):
    print(i)
t2 = datetime.utcnow()
print(t2-t1)