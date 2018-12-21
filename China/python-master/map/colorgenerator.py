# Add more collors if need
colors = ['#2F2F2F','#FF0000','#00FF00','#0000FF','#00FFFF',
         '#FFFF00','#FF00FF','#A0A0A0']

# interval size equals to colors size + 1
# two items define one interval
# so the total number of intervers is the same as colors size
#  
# Change the values to get different interval
#
# remove the middle value will reduce the number of intervals
#
# add more values to increase the number of interval
# but colors size must increase at the same time         
interval = [0,500,1000,4000,5000,9000,12000,20000]

def getColor(val):
    start = 0
    end = 0
    for i in range(len(interval)-1):
        start = interval[i]
        end = interval[i+1]
        if start <= val and val < end:
            return (colors[i],start,end)
    return (colors[len(interval)-1],start,end)
