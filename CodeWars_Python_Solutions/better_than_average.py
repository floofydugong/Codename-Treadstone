def better_than_average(class_points, your_points):
    class_points.append(your_points)
    print (your_points > sum(class_points)/len(class_points))

better_than_average([2,3,6,7,10],5)
