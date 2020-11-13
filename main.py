# data[0] is a column of a dataframe includes sorted values such as [9, 5, 2, 1]
p = data[0].to_numpy()
loss = 10**8
i1, i2 = 0, 0
for i in range(10000000):
    c1 = np.random.randint(0, len(data)-2, 1)[0]
    c2 = np.random.randint(c1+1, len(data), 1)[0]
    p1 = np.sum(p[:c1])
    p2 = np.sum(p[c1:c2])
    p3 = np.sum(p[c2:])
    loss_temp = abs(p3-p2)+abs(p2-p1)
    if loss_temp<=loss:
        print(loss)
        loss = loss_temp   
        i1, i2 = c1, c2
 print(i1, i2), #These are the points which you break your list at them.
