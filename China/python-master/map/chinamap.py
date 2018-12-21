import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np
import datetime
import fileloader
import colorgenerator

# init parameters
# Change figTitle to set different title on printed figure
figTitle = 'China Map'
# Change figHeight and figWidth to change figure size
figHeight = 16
figWidth = 16
fileName = 'ChinaData.csv'

start = datetime.datetime.utcnow()

# load data from ChinaData.csv

# provinces[] contains province names 
# and are loaded from the first column of ChinaData.csv 
# it is used to match NAME_1 property in states_info in CHN_adm1 file.
# they should be
#'Guangdong', 'Shandong', 'Gansu', 'Tianjin', 
#             'Shaanxi', 'Heilongjiang', 'Zhejiang', 
#             'Xinjiang Uygur', 'Anhui', 'Beijing', 'Qinghai', 
#             'Henan', 'Liaoning', 'Hubei', 'Hainan', 'Jiangsu', 
#             'Yunnan', 'Fujian', 'Guizhou', 'Chongqing', 'Shanghai', 
#             'Xizang', 'Shanxi', 'Sichuan', 'Hebei', 'Ningxia Hui', 
#             'Nei Mongol', 'Guangxi', 'Jiangxi', 'Hunan', 'Jilin']

# values loaded from the second column of ChinaData.csv

provinces, values = fileloader.read(fileName);

patchCollections = []

# function to patches array index for a given province
def getIndex(name):
    for i in range(len(provinces)):
        if(provinces[i] == name):
            return i
    return -1

# patches is a 31*1 array to hold shape data for each province. 
patches = []
for i in range(len(provinces)):
    patches.append([])

fig     = plt.figure(figsize=(figHeight,figWidth))
ax      = fig.add_subplot(111)
fig.suptitle(figTitle, fontsize=64)

m = Basemap(llcrnrlon=77, llcrnrlat=14,
            urcrnrlon=140, urcrnrlat=51,
            projection='lcc', lat_1=33, lat_2=45, lon_0=100)
m.drawcoastlines(),[]
m.drawcountries(linewidth=1.5)

# all 6 of CHN_adm1 files must be in the same directory as this python file
m.readshapefile('./CHN_adm1','states', drawbounds=True)

# create data for each province
for info, shape in zip(m.states_info, m.states):
    # NAME_1 is the property name of info that has 
    # province name defined in provinces array.
    index = getIndex(info['NAME_1'])
    assert (index >= 0),"index must be greater than or equal to 0!"
    patches[index].append( Polygon(np.array(shape), True) )

# plot each province map
for i in range(len(provinces)):
    # determine color index for each province
    val = values[i]
    color, rangeStart, rangeEnd = colorgenerator.getColor(val)
    p = PatchCollection(patches[i], 
                    facecolor= color, edgecolor='k', 
                    linewidths=1., zorder=2)
    patchCollections.append(p)
    ax.add_collection(p)

end = datetime.datetime.utcnow()
print('{} seconds to prepare. start save and draw ......'.format((end-start).total_seconds()))
plt.draw()
plt.savefig('chinamap.png')


