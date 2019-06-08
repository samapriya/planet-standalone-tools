import subprocess
import json
import os
import sys
import geopandas as gpd



def shp2gj(infile, outfile):
    inD = gpd.read_file(infile)
    #Reproject to EPSG 4326
    try:
        data_proj = inD.copy()
        data_proj['geometry'] = data_proj['geometry'].to_crs(epsg=4326)
        data_proj.to_file((outfile), driver="GeoJSON")
        print('Clean GeoJSON written to ' + str(outfile))
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


def convert(infolder, outfolder):
    for file in os.listdir(infolder):
        if file.endswith('.geojson'):
            infile = os.path.join(infolder, file)
            print('Processing: ' + str(infile))
            outfile = os.path.join(outfolder, file)
            cleanz(infile, outfile)
        elif file.endswith('.kml'):
            infile=os.path.join(infolder,file.replace('.kml','.shp'))
            outfile=os.path.join(outfolder,file.replace('.kml','.geojson'))
            print('Processing: ' + str(infile))
            try:
                subprocess.call('ogr2ogr -lco SHPT=POLYGON -f "ESRI Shapefile" '+'"'+os.path.join(infolder,file.replace('.kml','.shp'))+'" "'+ os.path.join(infolder,file)+'"',shell=False)
                shp2gj(infile, outfile)
            except Exception as e:
                print('Issues with:' + str(file) + str(e))


if len(sys.argv) == 3:
    convert(infolder=os.path.normpath(sys.argv[1]), outfolder=os.path.normpath(sys.argv[2]))
else:
    print('Pass inputfolder, output folder')

#convert(infolder=r'C:\Users\samapriya\Downloads\geotest',outfolder=r'C:\planet_demo')
# convert(infolder=r'C:\Users\samapriya\Box Sync\IUB\Pycodes\Applications and Tools\Planet Tools\Standalone Tools\gdal_convert\input',outfolder=r'C:\Users\samapriya\Box Sync\IUB\Pycodes\Applications and Tools\Planet Tools\Standalone Tools\gdal_convert\output')
