# Planet-Standalone-Tools
These are standalone tools created based on user requestes and long/short discussions with a few users from time to time. I hope to keep adding to this as on a need basis or requests.

### Planet-IDlist-Footprint
This tool allows you to convert a csv file with idlist to a geojson metadata file. The csv has the header ```id``` followed by the list of ids in the same column. The order of input is
```
inputfile =input csv file with id as csv file header
item= Item types for the idlist PSOrthoTile, PSScene4Band, PSScene3Band
asset = analytic, analytic_dn, visual
export= Full path along with name of geojson file **C:\johndoe\footprint.geojson**
```

Structure of the input CSV file with list of file ID(s)
<center>
|               id             |
|------------------------------|
| 0171121_141041_101e          |
| 20171121_141040_101e         |
| 20171121_141039_101e         |
</center>

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-baqh{text-align:center;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-baqh">id</th>
  </tr>
  <tr>
    <td class="tg-baqh">20171121_141041_101e</td>
  </tr>
  <tr>
    <td class="tg-baqh">20171121_141040_101e</td>
  </tr>
  <tr>
    <td class="tg-baqh">20171121_141039_101e</td>
  </tr>
</table>

```python idlist_footprint.py inputfile item asset export```

#### Example

```python idlist_footprint.py "C:\planet\images\idlist.csv" "PSScene4Band" "analytic" "C:\planet\footprint.geojson"```

![CLI](https://i.imgur.com/C2WXwwz.gif)

### Planet-SR-Tools
Currently the surface reflectance images have additional metadata json written into the GeoTIFF TIFFTAG. You can read the specifications and white [paper here](https://assets.planet.com/marketing/PDF/Planet_Surface_Reflectance_Technical_White_Paper.pdf). Though this is useful in some sense, not every platform can read from the header tags. This tool was written so as to extract both the PSScene4Band image metadata from which the Surface reflectance is created and then geotiff tifftags to a combined csv which can then be parsed. This tool requires that gdal is installed and can be called natively in command prompt or terminal.

The example metadata json written into the GeoTIFF TIFFTAG is the following

```
{
 “atmospheric_correction”: {
 “aerosol_model”: “continental”,
 “aot_coverage”: 0.53125,
 “aot_mean_quality”: 1.5294117647058822,
 “aot_method”: “fixed”,
 “aot_source”: “mod09cma_nrt”,
 “aot_status”: “Data Found”,
 “aot_std”: 0.038710440990655584,
 “aot_used”: 0.08517646789550781,
 “atmospheric_correction_algorithm”: “6Sv2.1”,
 “atmospheric_model”: “water_vapor_and_ozone”,
 “luts_version”: 3,
 “ozone_coverage”: 0.53125,
 “ozone_mean_quality”: 255.0,
 “ozone_method”: “fixed”,
 “ozone_source”: “mod09cmg_nrt”,
 “ozone_status”: “Data Found”,
 “ozone_std”: 0.0,
 “ozone_used”: 0.2550000022439396,
 “satellite_azimuth_angle”: 0.0,
 “satellite_zenith_angle”: 0.0,
 “solar_azimuth_angle”: 146.5250019999137,
 “solar_zenith_angle”: 53.64893752015384,
 “sr_version”: “1.0”,
 “water_vapor_coverage”: 0.53125,
 “water_vapor_mean_quality”: 1.5294117647058822,
 “water_vapor_method”: “fixed”,
 “water_vapor_source”: “mod09cma_nrt”,
 “water_vapor_status”: “Data Found”,
 “water_vapor_std”: 0.058699880113139036,
 “water_vapor_used”: 4.051176183363971
 }
}
```
To use simply type

```python sr_metadata_cli.py "full path to folder with surface reflectance images" "full path where metadata csv is to be exported"```

#### Example

```python sr_metadata_cli.py "C:\planet\sr" "C:\planet\srmetadata.csv"```

![CLI](https://i.imgur.com/ZgCDijB.gif)


### Split MultiBand Images in Folder to Single Images

This tool will allow you to split all multiband images in a folder into their component bands as single images. Note for now this only works with ".tif" files but you can change the extension within the program to whatever you need. This tool requires that gdal is installed and can be called natively in command prompt or terminal.

You can use the tool in 3 ways

![MultiBand Tool](https://i.imgur.com/viimtTg.gif)

* The first method will create a subfolder in that path called split and will split the multiband images into individual band images.
```python multiband2singleImages "source directory full path where your images exist"```


* Incase you want to specify a destination where you want your split images to be saved
```python multiband2singleImages "source directory full path where your images exist" "destination directory where you want your images to be saved```

* The third method will only work on Windows OS if you have python installed in your system path , meaning you can actually type ```python```
in your command prompt and start the python shell. In that case you can just drag and drop this tool in the folder with your images and double click on the python files and it will create a new folder called split and extract the images.
