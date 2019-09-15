#!/usr/bin/env python3
import json
import sys
from datetime import datetime
import os

import iso_datetime
import unique_filename


class PhotoPackage:
    def run(self):
        self._fetch_path()
        self._read_assets()
        self._filter_assets()
        self._unique_filename_creator = unique_filename.Creator()

    def _fetch_path(self):
        if len(sys.argv) != 4:
            print('Syntax: photo-package <path to backup> '
                  '<inclusive UTC start timestamp> '
                  '<exclusive UTC end timestamp>')
            exit(1)
        self._backup_path = sys.argv[1]
        self._start_timestamp = iso_datetime.parse(sys.argv[2])
        self._end_timestamp = iso_datetime.parse(sys.argv[3])

    def _read_assets(self):
        assets_path = os.path.join(self._backup_path, 'assets', 'assets.json')
        with open(assets_path) as file:
            file_content = json.load(file)
            self._assets = file_content['assets']

    def _filter_assets(self):
        resource_directory_path = os.path.join(self._backup_path, 'resources')
        package_directory_path = os.path.join(os.getcwd(), 'package')
        for asset in self._assets:
            asset_creation_timestamp = self._determine_asset_creation_timestamp(asset)
            if self._is_relevant_creation_timstamp(asset_creation_timestamp):
                print(asset['name'])
                print(asset_creation_timestamp)
                for resource in asset['resourceDescriptions']:
                    print('    ' + resource['checksum'])
                    print('    ' + resource['name'])
                    print('    ' + str(resource['size']) + ' bytes')
                    resource_path = os.path.join(resource_directory_path, resource['checksum'])
                    link_path = os.path.join(package_directory_path, unique_filename)
                    os.symlink()


    def _determine_asset_creation_timestamp(self, asset):
        raw_asset_creation_timestamp = asset['creationDateMs']
        try:
            asset_creation_timestamp = datetime.utcfromtimestamp(raw_asset_creation_timestamp / 1000)
        except ValueError as error:
            print('asset creation ms timestamp ' + str(raw_asset_creation_timestamp) + ': ' + str(error))
            return None
        return asset_creation_timestamp

    def _is_relevant_creation_timstamp(self, asset_creation_timestamp):
        return asset_creation_timestamp and self.timestamp_in_range(asset_creation_timestamp)

    def timestamp_in_range(self, asset_creation_timestamp):
        return self._start_timestamp <= asset_creation_timestamp < self._end_timestamp


PhotoPackage().run()
