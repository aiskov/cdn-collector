from os import listdir, remove
from shutil import rmtree
from utils import load_json, call, check_skip, create_dir, extract, move
import json
import re

config = load_json('cdn-config.json')

print 'Rebuild CDN collection.'

for target in config['targets']:
    print 'Collect %s libraries.' % target

    create_dir(target)

    lib_info = call("bower info %s -j --allow-root" % target)
    if not lib_info:
        print 'Cannot collect information about library'
        break

    versions = [
        version for version in json.loads(lib_info)['versions']
        if not check_skip(version, config['skipWords'])
    ]

    for version in versions:
        print 'Version found %s - %s.' % (target, version)

        target_directory = "%s/%s/%s" % (config['directory'], target, version)
        if not create_dir(target_directory) and listdir(target_directory):
            print 'Skip version, directory already exists %s/%s and not empty' % (target, version)
            continue

        info = call("bower install %s#%s -j --allow-root" % (target, version), True)

        tmp_directory = 'tmp'
        if listdir('tmp'):
            tmp_directory = "%s/%s" % (tmp_directory, listdir(tmp_directory)[0])
            move(listdir(tmp_directory), tmp_directory, directory)
            rmtree(tmp_directory)
