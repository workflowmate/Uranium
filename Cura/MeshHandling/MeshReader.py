class MeshReader(object):
    def __init__(self):
        self._supported_extension = ""
    
    # Tries to read the file from specified file_name, returns None if it's uncessfull or unable to read.
    def read(self, file_name):
        raise NotImplementedError('Reader plugin was not correctly implemented, no read was specified')
    
    def getSupportedExtention(self):
        return self._supported_type