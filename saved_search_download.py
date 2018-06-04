import os
import sys
import json
import subprocess
import requests
from requests.auth import HTTPBasicAuth

def download(name,asset,path,limit):
    '''Print allocation and remaining quota in Sqkm.'''
    try:
        fname = os.path.join(os.path.expanduser('~'), '.planet.json')
        contents = {}
        if os.path.exists(fname):
            with open(fname, 'r') as fp:
                contents = json.loads(fp.read())
        else:
            raise IOError('Escape to End and Initialize')
        if not len(contents) !=0:
            raise IOError('Escape to End and Initialize')
        else:
            k = contents['key']
        main = requests.get(
            'https://api.planet.com/data/v1/searches/?search_type=saved',
            auth=HTTPBasicAuth(
                k, ''))
        if main.status_code == 200:
            content = main.json()
            for items in content['searches']:
                if (items['name']==name and limit !=None):
                    print("Processing limited assets of size "+str(limit)+" with name "+str(items['name'])+" with id "+str(items['id']))
                    subprocess.call('planet data download --search-id '+'"'+str(items['id'])+'"'+' --asset-type '+'"'+asset+'"'+' --limit '+'"'+str(limit)+'"'+' --dest '+'"'+str(path)+'"',shell=True)
                elif (items['name']==name and limit ==None):
                    print("Processing all assets for "+str(items['name'])+" with id "+str(items['id']))
                    subprocess.call('planet data download --search-id '+'"'+str(items['id'])+'"'+' --asset-type '+'"'+asset+'"'+' --limit '+'"'+str(limit)+'"'+' --dest '+'"'+str(path)+'"',shell=True)
                elif items['name'] !=name:
                    pass
        else:
            print('Failed with exception code: ' + str(
                main.status_code))

    except IOError:
        print('Initialize client or provide API Key')
#download(name="LA/AtchVerm",asset="analytic",limit=1,path='C:\\planet_demo')
if len(sys.argv)==5:
    download(name=(sys.argv[1]),asset=(sys.argv[2]),path=os.path.normpath(sys.argv[3]),limit=(sys.argv[4]))
elif len(sys.argv)==4:
    download(name=(sys.argv[1]),asset=(sys.argv[2]),path=os.path.normpath(sys.argv[3]))
else:
    print("Provide arguments in the following order: saved_order_name, asset_type,path_to_save,limit_which is optional and represents numeber of item-asset combinations")
