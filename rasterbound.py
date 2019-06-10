import rasterio
import sys
import os
import json
import rasterio.features
import rasterio.warp
from shapely.geometry import Polygon
from shapely.geometry import shape
from shapely.geometry import box
from geodaisy import GeoObject


temp = {"coordinates": [], "type": "Polygon"}


# Function to get raster bounding box as a GeoJSON
def rasterbound(rasterfile):
    with rasterio.open(rasterfile) as dataset:
        mask = dataset.dataset_mask()
        for geom, val in rasterio.features.shapes(
                mask, transform=dataset.transform):
            geom = rasterio.warp.transform_geom(
                dataset.crs, 'EPSG:4326', geom, precision=6)
            gmain = shape(geom)
            glist = list(gmain.bounds) #Create the bounding box
            mosgeom = shape(Polygon(box(glist[0], glist[1], glist[2], glist[3]).exterior.coords))
            geo_obj = GeoObject(mosgeom)
            print('\n' + 'Using geodaisy')
            print(geo_obj.geojson()) #geojson using geodaisy

            # direct method not as short
            gmainbound = (','.join(str(v) for v in list(gmain.bounds)))
            first = [float(i) for i in [gmainbound.split(',')[0], gmainbound.split(',')[3]]]
            second = [float(i) for i in [gmainbound.split(',')[0], gmainbound.split(',')[1]]]
            third = [float(i) for i in [gmainbound.split(',')[2], gmainbound.split(',')[1]]]
            fourth = [float(i) for i in [gmainbound.split(',')[2], gmainbound.split(',')[3]]]
            last = first
            temp['coordinates'] = [[first, second, third, fourth, last]]
            print('\n' + 'Using boundary list')
            print(json.dumps(temp))
            break

if len(sys.argv) == 2:
    rasterbound(rasterfile=os.path.normpath(sys.argv[1]))
else:
    print('Pass raster file')

#rasterbounds(rasterfile=r'C:\Users\samapriya\20190428_083053_1035_3B_AnalyticMS.tif')
