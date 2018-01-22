import datetime
l = '2011-12-02'
t = datetime.datetime.strptime(l, '%Y-%m-%d')
print t
print t.strftime('%Y-%m-%d')