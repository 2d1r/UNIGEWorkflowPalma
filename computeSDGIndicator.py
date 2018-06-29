from osgeo import ogr

# have to make sure have access to gdal data files
import os

#if 'GDAL_DATA' not in os.environ:
#    os.environ["GDAL_DATA"] = '/opt/anaconda/share/gdal'

g = ogr.Open( "area_out.shp" )
layer = g.GetLayer( 0 )

g1 = ogr.Open( "intersection_out.shp" )
layer1 = g1.GetLayer( 0 )

a = {}
b = {}
resultat = {}

for feat in layer:
    a[feat.GetField('SitRecID')] = feat.GetField('area')

for feat in layer1:
    b[feat.GetField('SitRecID')] = feat.GetField('area')

resultat = {key: (100*b.get(key, 0)/a[key]) for key in a.keys()}

count = 0
mysum = 0

for i in resultat:
    count += 1
    mysum += resultat[i]
    #print i, resultat[i]
print ("The mean purcentage is ", mysum/count)
  

