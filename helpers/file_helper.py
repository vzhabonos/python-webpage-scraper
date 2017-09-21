import os.path


class FileHelper:

    @staticmethod
    def directory_exists(path):
        if os.path.exists(path) and not os.path.isfile(path):
            return True
        return False

    @staticmethod
    def create_path_recursively(path):
        current_path = os.getcwd()
        if current_path == path:
            return path
        if not FileHelper.is_path_absolute(path):
            os.chdir('/')
        directories = path.split('/')
        for directory in directories:
            if len(directory) > 0:
                if not os.path.exists('./' + directory):
                    os.mkdir('./' + directory)
                os.chdir('./' + directory)

    @staticmethod
    def is_path_absolute(path):
        if isinstance(path, str) and path[0] == '/':
            return True
        else:
            return False

