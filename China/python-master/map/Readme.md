# Draw China map with province level administration information (adm1) using Basemap

The steps to download China's shapefile. 

1. Go to [http://www.diva-gis.org/gdata](http://www.diva-gis.org/gdata) web site.

2. Select **China** in Country.

3. Select **Administrative areas** in Subject. It should be the first choice in dropdown list. If not, select it.

4. Click **OK** to download.

5. Extract downloaded CHN_adm.zip file to working folder.

Use code below to load China shapefile. See chinamap.py for details
>m.readshapefile('\<working folder\>','states',drawbouns=True)