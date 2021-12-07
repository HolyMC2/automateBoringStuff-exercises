#!/usr/bin/env python3

def displayPathtoPrincess(n,ip):
    for col,k in enumerate(ip):
        if 'm' or 'p' in k:
            for ind, d in enumerate (k):
                if d == 'm':
                    indm = [col,ind]
                elif d == 'p':
                    indp = [col,ind]
    UP = DOWN = RIGHT = LEFT = 0
    if indm[0] >= indp[0]:
        UP = indm[0]-indp[0]
    elif indm[0] = indp[1]:
        LEFT = indm[1]-indp[1]
    elif indm[0] < indp[1]:
        RIGHT = indp[1] - indm[1]

    while UP or DOWN:
        if UP:
            print 'UP'
            UP -=1
        else:
            print 'DOWN'
            DOWN -= 1
    while LEFT or RIGHT:
        if LEFT:
            print 'LEFT'
            LEFT -= 1
        else:
            print 'RIGHT'
            RIGHT -= 1

#print all the moves here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(list(raw_input().strip()))


displayPathtoPrincess(m,grid)
