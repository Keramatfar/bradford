p = data[0].to_numpy()
loss = 10**8
i1, i2 = 0, 0
s1, s2, s3 = 0, 0, 0
for c1 in range(len(data)-1):
    for c2 in range(c1, len(data)):
        p1 = np.sum(p[:c1])
        p2 = np.sum(p[c1:c2])
        p3 = np.sum(p[c2:])
        loss_temp = abs(p3-p2)+abs(p2-p1)
        if loss_temp<=loss:
            loss = loss_temp   
            i1, i2 = c1, c2
            s1, s2, s3 = p1, p2, p3
print('Zone 1:', i1, 'Zone 2:', i2-i1, 'Zone 3:', len(data) - i2) #These are the points which you break your list at them.
