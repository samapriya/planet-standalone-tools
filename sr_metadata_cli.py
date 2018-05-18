from osgeo import gdal
import json,os,time,csv,sys

def srmeta(indir,mfile):
    with open(mfile,'wb') as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=["id_no", "satID","system:time_start", "AtmModel", "SolarAzAngle","AOT_Model", "AOT_Used", "AOT_Std", "AOT_Used","AOT_MeanQual"
        ,"LUTS_Version","SolarZenAngle","AOT_Coverage","Aerosol_Model","AOT_Source","AtmCorr_Alg","SatAzAngle","SatZenAngle"], delimiter=',')
        writer.writeheader()
    for filename in os.listdir(indir):
        print("Processing "+str(filename))
        print("Sat ID : "+str(filename).split("_")[2])
        try:
            gtif = gdal.Open(os.path.join(indir,filename))
            date_time = gtif.GetMetadata()['TIFFTAG_DATETIME'].split(" ")[0]
            pattern = '%Y:%m:%d'
            epoch = int(time.mktime(time.strptime(date_time, pattern)))*1000
            conv=json.loads(gtif.GetMetadata()['TIFFTAG_IMAGEDESCRIPTION'])
            sid=str(filename).split("_")[2]
            atmmodel=(conv['atmospheric_correction']['atmospheric_model'])
            sraz=(conv['atmospheric_correction']['solar_azimuth_angle'])
            aotmethod=(conv['atmospheric_correction']['aot_method'])
            aotused=(conv['atmospheric_correction']['aot_used'])
            aotstat=(conv['atmospheric_correction']['aot_status'])
            aotstd=(conv['atmospheric_correction']['aot_std'])
            aotmq=(conv['atmospheric_correction']['aot_mean_quality'])
            luts=(conv['atmospheric_correction']['luts_version'])
            szen=(conv['atmospheric_correction']['solar_zenith_angle'])
            aotcov=(conv['atmospheric_correction']['aot_coverage'])
            arsm=(conv['atmospheric_correction']['aerosol_model'])
            aotsor=(conv['atmospheric_correction']['aot_source'])
            atcoralgo=(conv['atmospheric_correction']['atmospheric_correction_algorithm'])
            sataz=(conv['atmospheric_correction']['satellite_azimuth_angle'])
            satzen=(conv['atmospheric_correction']['satellite_zenith_angle'])
            print("Atmospheric Model : "+str(atmmodel))
            print("Solar Azimuth Angle : "+format(float(sraz),'.2f'))
            print("Aerosol Optical Thickness(AOT) Method : "+str(aotmethod))
            print("Aerosol Optical Thickness(AOT) Used : "+format(float(aotused),'.4f'))
            print("Aerosol Optical Thickness(AOT) Status : "+str(aotstat))
            print("Aerosol Optical Thickness(AOT) Std : "+format(float(aotstd),'.4f'))
            print("Aerosol Optical Thickness(AOT) mean quality : "+str(aotmq))
            print("LUTS Version : "+str(luts))
            print("Solar Zenith Angle : "+format(float(szen),'.2f'))
            print("Aerosol Optical Thickness(AOT) Coverage : "+format(float(aotcov),'.4f'))
            print("Aerosol Model : "+str(arsm))
            print("Aerosol Optical Thickness(AOT) Source : "+str(aotsor))
            print("ATCOR Correction Algorithm : "+str(atcoralgo))
            print("Satellite Azimuth Angle : "+str(sataz))
            print("Satellite Zenith Angle : "+str(satzen))
            print("Date Time : "+str(date_time))
            print("Epoch Time : "+str(epoch))
            print(" ")
            with open(mfile,'a') as csvfile:
                writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
                writer.writerow([os.path.splitext(filename)[0],sid,epoch,str(atmmodel),format(float(sraz),'.2f'),str(aotmethod),format(float(aotused),'.4f'),str(aotstat),
                format(float(aotstd),'.4f'),aotmq,luts,format(float(szen),'.2f'),format(float(aotcov),'.4f'),str(arsm),str(aotsor),str(atcoralgo),str(sataz),str(satzen)])
        except Exception:
            print("Issues with : "+str(os.path.splitext(filename)[0]))
srmeta(indir=os.path.normpath(sys.argv[1]),mfile=os.path.normpath(sys.argv[2]))
