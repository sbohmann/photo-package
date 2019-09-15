from itertools import count

from name_and_suffix import NameAndSuffix


class Creator:
    def __init__(self):
        self._used_names = set()

    def create(self, raw_name):
        if raw_name in self._used_names:
            return self._create_altered_name(raw_name)
        else:
            self._used_names.add(raw_name)
            return raw_name

    def _create_altered_name(self, raw_name):
        name_and_suffix = NameAndSuffix(raw_name)
        for file_number in count(2):
            candidate = name_and_suffix.name + '_' + str(file_number) + name_and_suffix.suffix
            if candidate not in self._used_names:
                self._used_names.add(candidate)
                return candidate
