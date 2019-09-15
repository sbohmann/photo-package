#!/usr/bin/env python3
import json
import sys
from datetime import datetime

import iso_datetime


class PhotoPackage:
    def run(self):
        self._fetch_path()
        self._read_assets()
        self._filter_assets()

    def _fetch_path(self):
        if len(sys.argv) != 4:
            print('Syntax: photo-package <path to assets json file> '
                  '<inclusive UTC start timestamp> '
                  '<exclusive UTC end timestamp>')
            exit(1)
        self._path = sys.argv[1]
        self._start_timestamp = iso_datetime.parse(sys.argv[2])
        self._end_timestamp = iso_datetime.parse(sys.argv[3])

    def _read_assets(self):
        with open(self._path) as file:
            self._assets = json.load(file)['assets']

    def _filter_assets(self):
        for asset in self._assets:
            asset_creation_timestamp = self._determine_asset_creation_timestamp(asset)
            if self._is_relevant_creation_timstamp(asset_creation_timestamp):
                print(asset)

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
