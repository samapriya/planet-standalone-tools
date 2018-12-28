#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
from requests.auth import HTTPBasicAuth

headers = {'Content-Type': 'application/json'}


def enable_email(name, action):
    if action == 'enable':
        action = True
    if action == 'disable':
        action = False
    try:
        fname = os.path.join(os.path.expanduser('~'), '.planet.json')
        contents = {}
        if os.path.exists(fname):
            with open(fname, 'r') as fp:
                contents = json.loads(fp.read())
        else:
            raise IOError('Escape to End and Initialize')
        if not len(contents) != 0:
            raise IOError('Escape to End and Initialize')
        else:
            k = contents['key']
        main = \
            requests.get('https://api.planet.com/data/v1/searches/?search_type=saved'
                         , auth=HTTPBasicAuth(k, ''))
        if main.status_code == 200:
            content = main.json()
            for items in content['searches']:
                if items['name'] == name:
                    try:
                        source = \
                            'https://api.planet.com/data/v1/searches/' \
                            + items['id']
                        if items['__daily_email_enabled'] \
                            == (not action):
                            items['__daily_email_enabled'] = action
                            main = requests.put(source,
                                    data=json.dumps(items),
                                    headers=headers,
                                    auth=HTTPBasicAuth(k, ''))
                            if main.status_code == 200:
                                print 'Updating email notification for saved search ' \
                                    + str(items['name']) + ' with id ' \
                                    + str(items['id']) + ' to ' \
                                    + str(action)
                        else:
                            print 'Email notification for saved search ' \
                                + str(items['name']) + ' with id ' \
                                + str(items['id']) + ' already set to ' \
                                + str(action)
                    except Exception, e:
                        print e
                elif name == 'all':
                    for items in content['searches']:
                        try:
                            source = \
                                'https://api.planet.com/data/v1/searches/' \
                                + items['id']
                            if items['__daily_email_enabled'] \
                                == (not action):
                                items['__daily_email_enabled'] = action
                                main = requests.put(source,
                                        data=json.dumps(items),
                                        headers=headers,
                                        auth=HTTPBasicAuth(k, ''))
                                if main.status_code == 200:
                                    print 'Updating email notification for saved search ' \
    + str(items['name']) + ' with id ' + str(items['id']) + ' to ' \
    + str(action)
                        except Exception, e:
                            pass
        else:
            print 'Failed with exception code: ' + str(main.status_code)
    except IOError:

        print 'Initialize client or provide API Key'


if len(sys.argv) == 3:
    enable_email(name=sys.argv[1], action=sys.argv[2])
else:
    print 'Pass saved search followed by enable or disable to run tool '
