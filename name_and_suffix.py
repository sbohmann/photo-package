class NameAndSuffix:
    def __init__(self, raw_name):
        last_dot_index = raw_name.rfind('.')
        if last_dot_index >= 0:
            self.name = raw_name[:last_dot_index]
            self.suffix = raw_name[last_dot_index:]
        else:
            self.name = raw_name
            self.suffix = ''
