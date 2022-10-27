import datetime
b1=10
b2=20
a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
a=a%1
new=round(b1+(b2-b1)*a)
print(new)

