# def strong_enough( earthquake, age ):
#     answer = 1
#     building_str = 1000

#     for i in range (0,age):
#         building_str = building_str - (building_str *.01)

#     print building_str
#     for i in earthquake:
#         answer *= sum(i)
#     return "Needs Reinforcement!" if answer > building_str else "Safe!"



#lambda <input>: <expression>
def strong_enough( earthquake, age ):
    #welp...wouldn't have known to decay at that rate...
    strength = 1000 * 0.99 ** age
    #
    shockwave = reduce(lambda x, y : x*y, [4,4,3])
    print shockwave
    if strength <= shockwave: print "Needs Reinforcement!"
    print "Safe!"

strong_enough([[5,8,7],[3,3,1],[4,1,2]], 3)