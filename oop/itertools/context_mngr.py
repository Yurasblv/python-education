"""Module in which the file manager is written"""


class Manager:
    """Class that have operate files"""
    def __init__(self, file, method):
        self.filename = file
        self.mode = method
        self._file = None

    def __enter__(self):
        """Open file"""
        self._file = open(self.filename, self.mode)
        return self._file

    def __exit__(self,*args):
        """Close file"""
        if not self._file.closed:
            self._file.close()


if __name__ == '__main__':
    with Manager('test.txt', 'a') as f:
        f.write('Yurets was here')
