import subprocess
import json
import os
import sys
import geopandas as gpd



def shp2gj(folder, export):
    for items in os.listdir(folder):
        if items.endswith('.shp'):
            inD = gpd.read_file(os.path.join(folder, items))
            #Reproject to EPSG 4326
            try:
                data_proj = inD.copy()
                data_proj['geometry'] = data_proj['geometry'].to_crs(epsg=4326)
                data_proj.to_file(os.path.join(export, str(items).replace('.shp', '.geojson')), driver="GeoJSON")
                print('Export completed to ' + str(os.path.join(export, str(items).replace('.shp', '.geojson'))))
            except Exception as e:
                print(e)


def cleanz(infile, outfile):
    with open(infile) as rfile:
        d = json.load(rfile)
        for items in d['features']:
            for things in items['geometry']['coordinates']:
                for item in things:
                    item.remove(item[2])
        with open(outfile, 'w') as f:  # writing JSON object
            json.dump(d, f)
        print('Clean GeoJSON written to: ' + str(outfile))


def convert(infolder, outfolder, typ):
    for file in os.listdir(infolder):
        if typ == 'geojson' and file.endswith('.geojson'):
            infile = os.path.join(infolder, file)
            print('Processing: ' + str(infile))
            outfile = os.path.join(outfolder, file)
            cleanz(infile, outfile)
        elif typ == 'kml' and file.endswith('.kml'):
            try:
                print('Processing: ' + str(file))
                subprocess.call('ogr2ogr -lco SHPT=POLYGON -f "ESRI Shapefile" '+'"'+os.path.join(infolder,file.replace('.kml','.shp'))+'" "'+ os.path.join(infolder,file)+'"',shell=False)
            except Exception as e:
                print('Issues with:' + str(file) + str(e))
    if typ == 'kml':
        print('Now exporting to GeoJSON...')
        shp2gj(infolder, outfolder)


if len(sys.argv) == 4:
    convert(infolder=os.path.normpath(sys.argv[1]), outfolder=os.path.normpath(sys.argv[2]),typ=sys.argv[3])
else:
    print('Pass inputfolder, output folder and typ as either geojson or kml')

#convert(infolder=r'C:\Users\samapriya\Downloads\geotest',outfolder=r'C:\planet_demo',typ='geojson')
#convert(infolder=r'C:\Users\samapriya\Box Sync\IUB\Pycodes\Applications and Tools\Planet Tools\Standalone Tools\gdal_convert\input',outfolder=r'C:\Users\samapriya\Box Sync\IUB\Pycodes\Applications and Tools\Planet Tools\Standalone Tools\gdal_convert\output',typ='kml')
