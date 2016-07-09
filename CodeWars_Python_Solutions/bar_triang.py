def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    xO = round(float(pointA[0] + pointB[0] + pointC[0])/float(3),4)
    yO = round(float(pointA[1] + pointB[1] + pointC[1])/float(3),4)
    return ([xO,yO]) # coordinates of the barycenter expressed up to four decimals
                    # (rounded result)