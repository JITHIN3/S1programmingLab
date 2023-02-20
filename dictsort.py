dic = {"sona":8,"zinu":5,"trisha":9,"roshan":7,"nandhu":4}
i=list(dic.items())
i.sort()
d=dict(i)
print("Ascending order is : ",d)
i.sort(reverse=True)
d=dict(i)
print("Decending is : ",d)