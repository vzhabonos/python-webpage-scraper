import os.path


class FileHelper:

    @staticmethod
    def directory_exists(path):
        if os.path.exists(path) and not os.path.isfile(path):
            return True
        return False

    @staticmethod
    def create_path_recursively(path):
        start_path = os.getcwd()

        if start_path == path or path == './' or path == '.':
            # no need to continue
            return

        if FileHelper.is_path_absolute(path):
            # change working directory on "/" if given path are absolute
            os.chdir('/')

        directories = path.split('/')
        for directory in directories:
            if len(directory) > 0:
                if not os.path.exists('./' + directory):
                    os.mkdir('./' + directory)
                os.chdir('./' + directory)

        # change working directory back to normal
        os.chdir(start_path)

    @staticmethod
    def is_path_absolute(path):
        if isinstance(path, str) and path[0] == '/':
            return True
        else:
            return False

    @staticmethod
    def create_file(file, path, content = None):
        if not FileHelper.directory_exists(path):
            FileHelper.create_path_recursively(path)
        # Check if path have slash at the end and add slash if not
        if path[-1] != "/":
            path = path + "/"
        file = open(path + file, "a+")
        file.write(content)
        file.close()
