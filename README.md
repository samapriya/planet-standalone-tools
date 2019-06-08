# Planet-Standalone-Tools
These are standalone tools created based on user requestes and long/short discussions with a few users from time to time. I hope to keep adding to this as on a need basis or requests.

## Tool List
* [Saved Search Download](#saved-search-download)
* [Planet-IDlist-Footprint](#planet-idlist-footprint)
* [Planet-SR-Custom-Metadata](#planet-sr-custom-metadata)
* [Split MultiBand Images in Folder to Single Images](#split-multiband-images-in-folder-to-single-images)
* [Enable and Disable Email alert on Saved Search](#enable-and-disable-email-alert-on-saved-search)
* [Remove z value and convert to GeoJSON](#remove-z-value-and-convert-to-geojson)

### Saved Search Download
This tool is a quick addon to existing application of ```planet saved searches``` to download images. This prints all the saved searches that you might have saved using the CLI or using the explorer. In which case you are able to set the filters, choose item types and date ranges and aoi within the Planet Explorer GUI and then be able to use the saved search name to execute a batch download command. This combines activation and download and works only for a single item type that was set in the search. You can choose to provide a limit which limits the number of item-asset combinations to download or use without limit and all items and asset combinations in the aoi will be downloaded.

Using with limits

```python saved_search_download.py "search_name" "analytic" "C:\planet_demo" "10"```

Without limits the setup becomes

```python saved_search_download.py "search_name" "analytic" "C:\planet_demo"```

<img src="/images/saved_searches.gif">

<p align="center">
  <b>Steps to create and use saved searches</b>
</p>

### Planet-IDlist-Footprint
This tool allows you to convert a csv file with idlist to image footprints. Each footprint has the related metadata associated with the imagery so you can do further analysis by converting it into kml or shape file for checking coverage or any other statistical analysis. The csv has the header ```id``` followed by the list of ids in the same column. The order of input is
```
inputfile =input csv file with id as csv file header
item= Item types for the idlist PSOrthoTile, PSScene4Band, PSScene3Band
asset = analytic, analytic_dn, visual
export= Full path along with name of geojson file **C:\johndoe\footprint.geojson**
```

Structure of the input CSV file with list of file ID(s)

|                <center>id</center>            |
|-----------------------------------------------|
| <center>20171121_141041_101e</center>         |
| <center>20171121_141040_101e</center>         |
| <center>20171121_141039_101e</center>         |


```python idlist_footprint.py inputfile item asset export```

#### Example

```python idlist_footprint.py "C:\planet\images\idlist.csv" "PSScene4Band" "analytic" "C:\planet\footprint.geojson"```

![CLI](https://i.imgur.com/C2WXwwz.gif)

### Planet-SR-Custom-Metadata
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


### Enable and Disable Email alert on Saved Search
This tool is a quick addon to enable and disable email notification when new imagery is available for your saved search based on your filters. This can access all your saved searched including those built in Planet Explorer as well as those built using the Plane Client. You can create a search using client command ```planet data create-search --help``` to look at filters to setup these notifications. Currently the CLI does not allow for enabling email notification, and this tool augments to the existing saved searches. This can enable and disable all email notifications for all saved search or you can enable or disable a specific saved search based on saved-search name.

<img src="/images/add_email.gif">

<p align="center">
  <b>Steps to enable and disable email notification on saved searches</b>
</p>

Enable email notification when new images are available for all saved searched

```python add_email_notification.py all enable```

Disable email notification when new images are available for all saved searched

```python add_email_notification.py all disable```

Enable email notification when new images are available for specific saved search name

```python add_email_notification.py searchname enable```

Disable email notification when new images are available for specific saved search name

```python add_email_notification.py searchname disable```

### Remove z value and convert to GeoJSON
This tool serves a very specific function, the planet API does not accept z value along with the lat long coordinates for a GeoJSON geometry file. Often times you can get this from a kml file or from a generated geojson file. This application can take a folder filled with kml files with z axis or geojson file with a z and remove them and write the files to a new folder. The program does require for you to install geopandas before running this tool.

The setup is simple

```
python remove_z.py "path to input folder" "path to output folder" "kml"
```

if files are geojsons

```
python remove_z.py "path to input folder" "path to output folder" "geojson"
```
