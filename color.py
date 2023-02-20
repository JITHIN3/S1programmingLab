dic = {'unni': 5, 'manu': 20, 'kiran': 17}
l = list(dic.items())
l.sort()
d = dict(l)
print("Ascending is: ", d)
l = list(dic.items())
l.sort(reverse=True)
d = dict(l)
print("Descending is: ", d)
