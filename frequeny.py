data =[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
freq_map ={} # dictionary to store frequency of each element
for i in data :
    if i in freq_map:
        freq_map[i]+1
    else:
        freq_map[i]=1
print(freq_map)    