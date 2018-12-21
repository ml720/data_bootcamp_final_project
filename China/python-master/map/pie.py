import matplotlib.pyplot as plt
import fileloader
import colorgenerator

repository = []

def find(_color) :
    for i in range(len(repository)):
        color, lable, count = repository[i]
        if color == _color:
            return i
    return None
            
def add(color, start, end, province):
    i = find(color)
    if i != None:
        color, lable, count = repository[i]
        count += 1
        if count%2 == 0:
            lable += "\n"+province            
        else:
            lable += ","+province
        repository[i] = (color, lable, count)
    else:    
        val = (color, str(start)+"-"+str(end)+": \n"+province,1)
        repository.append(val)
        
def get():
    colors = []
    labels = []
    counts = []
    for color, lable, count in repository:
        colors.append(color)
        labels.append(lable)
        counts.append(count)  
    return (colors, labels, counts)

def draw():
    figTitle = 'China Map Pie'
    # Change figHeight and figWidth to change figure size
    figHeight = 8
    figWidth = 8
    fig     = plt.figure(figsize=(figHeight,figWidth))
    fig.suptitle(figTitle, fontsize=16)
    fileName = 'ChinaData.csv'
    
    provinces, values = fileloader.read(fileName);
    for i in range(len(provinces)):
        # determine color index for each province
        val = values[i]
        color, rangeStart, rangeEnd = colorgenerator.getColor(val)
        add(color,rangeStart,rangeEnd,provinces[i])
    
    colors, labels, sizes = get() 
    # Plot
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
     
    plt.axis('equal')
    plt.draw()
    plt.savefig('pie.png')

draw()