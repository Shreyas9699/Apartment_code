def input_process(): #process input
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    
    blocks_names = list()
    for i in contents:
        if 'Area_name' in i:
            blocks_names.append(i.split(':')[1][2])
            del contents[contents.index(i)]
    
    tmpLst = []
    for i in contents:
        if 'False' in i.split(':')[1]:
            tmpLst.append(False)
        else:
            tmpLst.append(True)
    
    amenities = ['Gym', 'Store', 'School'] #list of amenities required
    apart = list() #list of amenities for each block
    i = 0
    while i < len(tmpLst):
        apart.append({amenities[i%3]: tmpLst[i], amenities[(i+1)%3]: tmpLst[i+1], amenities[(i+2)%3]: tmpLst[i+2]})
        i = i+3
    return blocks_names, apart, amenities

#function to get best block to buy apart from given blocks
def findMyApart(apart, amenities):
    amenitiesAvail = {i: [] for i in amenities} #map available amenities to respective blocks
    for i in range(len(apart)):
        for j in amenitiesAvail:
            if apart[i][j]:
                amenitiesAvail[j].append(i)
    
    minDist = {i: [] for i in range(len(apart))}
    maxDist = []
    for i in minDist:
        for key, value in amenitiesAvail.items():
            minVal = 0
            if apart[i][key] == False: #if for ith block req amenity is not there
                minVal = min([abs(i-j) for j in value]) #then serch for the nearest block, using amenitiesAvail
                minDist[i].append(minVal)
            else:
                minDist[i].append(minVal) #since req amenity is present min distance is 0
        maxDist.append(max(minDist[i]))
    
    return maxDist.index(min(maxDist))


#main
blocks_names, apart, amenities = input_process()

print(blocks_names[findMyApart(apart, amenities)])


'''
blocks_names = ['A', 'B', 'C'] #block names
apart = [
    {'Gym': False, 'Store': False, 'School': True},
    {'Gym': False, 'Store': True, 'School': False},
    {'Gym': True ,'Store': True, 'School': False}] #each blocks with amenities
    
amenities = ['Gym', 'Store', 'School'] #list of amenities required

print(blocks_names[findMyApart(apart, amenities)])
'''