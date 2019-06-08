import os
import csv
import json
import time
import sys
pathway=os.path.dirname(os.path.realpath(__file__))
def id2footprint(inputfile,item,asset,export):
    with open(inputfile) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        numline = len(csvfile.readlines())
    with open(inputfile,'r') as f:
        reader = csv.DictReader(f)
        l=[]
        for i,line in enumerate(reader):
            print("Processing "+str(i+1)+" of "+str(numline-1))
            l.append(line['id'])
        pjson={"type": "AndFilter","config": [{"type": "StringInFilter","field_name": "id","config": []}]}
        pjson['config'][0]['config']=l
        json_data = json.dumps(pjson)
        with open('pjson.json', 'w') as outfile:
            json.dump(pjson, outfile)
        time.sleep(2)
        try:
            print("")
            os.system("planet data search --item-type "+str(item)+" --asset-type "+str(asset)+' --filter-json "'+os.path.join(pathway,"pjson.json")+'" --limit 10000 >"'+export+'"')
            print("Footprints Exported")
        except Exception as e:
            print(e)
id2footprint(inputfile=os.path.normpath(sys.argv[1]),item=os.path.normpath(sys.argv[2]),asset=os.path.normpath(sys.argv[3]),
             export=os.path.normpath(sys.argv[4]))
