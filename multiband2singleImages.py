from osgeo import gdal
import sys,os,subprocess
currentfolder=os.path.dirname(os.path.realpath(__file__))
def bandsplit(folder,destination=None):
    if destination is not None:
        for files in os.listdir(folder):
            if files.endswith(".tif"):
                src_ds = gdal.Open(os.path.join(folder,files))
                if src_ds is None:
                    print 'Unable to open INPUT.tif'
                else:
                    print files,"has ",src_ds.RasterCount," bands"
                if int(src_ds.RasterCount)>1:
                    for band in range(src_ds.RasterCount):
                        band += 1
                        output=os.path.join(destination,os.path.splitext(files)[0]+"_b"+str(band)+".tif")
                        if not os.path.exists(output):
                            subprocess.call("gdal_translate -b "+str(band)+' "'+os.path.join(folder,files)+'" "'+output+'"')
                        else:
                            print("Raster Split already: Skipping "+str(files))
                else:
                    print("Single Band Image: "+str(files))
    else:
        if not os.path.exists(os.path.join(folder,"split")):
            os.makedirs(os.path.join(folder,"split"))
        for files in os.listdir(folder):
            if files.endswith(".tif"):
                src_ds = gdal.Open(os.path.join(folder,files))
                if src_ds is None:
                    print 'Unable to open INPUT.tif'
                else:
                    print files,"has ",src_ds.RasterCount," bands"
                if src_ds.RasterCount>1:
                    for band in range(src_ds.RasterCount):
                        band += 1
                        output=os.path.join(os.path.join(folder,"split"),os.path.splitext(files)[0]+"_b"+str(band)+".tif")
                        if not os.path.exists(output):
                            print("Processing Band "+str(band))
                            subprocess.call("gdal_translate -b "+str(band)+' "'+os.path.join(folder,files)+'" "'+output+'"')
                        else:
                            print("Raster Split already: Skipping "+os.path.splitext(files)[0]+"_b"+str(band)+".tif")
                else:
                    print("Single Band Image: "+str(src_ds))

#bandsplit(folder=r"C:\planet_demo\SurfaceReflectance\sr",destination=r"C:\planet_demo\SurfaceReflectance\nw")           
if len(sys.argv)==3:
    bandsplit(folder=os.path.normpath(sys.argv[1]),destination=os.path.normpath(sys.argv[2]))
elif len(sys.argv)==2:
    bandsplit(folder=os.path.normpath(sys.argv[1]))
else:
    bandsplit(folder=os.path.dirname(os.path.realpath(__file__)))
