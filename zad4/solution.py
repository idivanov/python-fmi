'''
    - FileSystemError
        - NodeDoesNotExistError
            - SourceNodeDoesNotExistError 
            - DestinationNodeDoesNotExistError 
        - FileSystemMountError
            - MountPointDoesNotExistError
            - MountPointNotADirectoryError 
            - MountPointNotEmptyError
            - NotAMountpointError  
        - NotEnoughSpaceError 
        - NonExplicitDirectoryDeletionError
        - NonEmptyDirectoryDeletionError
        - DestinationNotADirectoryError
        - DestinationNodeExistsError
        - DirectoryHardLinkError
'''

class FileSystemError(Exception):
    def __init__():
        self.message = "File system error!"

    def __str__(self):
        return repr(self.message)


class NodeDoesNotExistError(FileSystemError):
    def __init__(self):
        self.message = "Node does not exist!"


class SourceNodeDoesNotExistError(NodeDoesNotExistError):
    def __init__(self):
        self.message = "Source node does not exist!"


class DestinationNodeDoesNotExistError(NodeDoesNotExistError):
    def __init__(self):
        self.message = "Destination node does not exist!"

class FileSystemMountError(FileSystemError):
    def __init__(self):
        self.message = "File system mount error!"


class MountPointDoesNotExistError(FileSystemMountError):
    def __init__(self):
        self.message = "Mount point does not exist!"


class MountPointNotADirectoryError(FileSystemMountError):
    def __init__(self):
        self.message = "Mount point is not a directory!"


class NotAMountpointError(FileSystemMountError):
    def __init__(self):
        self.message = "Not a mount point!"


class NotEnoughSpaceError(FileSystemError):
    def __init__(self):
        self.message = "Not enough space!"


class NonExplicitDirectoryDeletionError(FileSystemError):
    def __init__(self):
        self.message = "Non explicit directory deletion!"


class NonEmptyDirectoryDeletionError(FileSystemError):
    def __init__(self):
        self.message = "Non empty directory deletion!"


class DestinationNotADirectoryError(FileSystemError):
    def __init__(self):
        self.message = "Destination is not a directory!"


class DestinationNodeExistsError(FileSystemError):
    def __init__(self):
        self.message = "Destination node already exists!"


class DirectoryHardLinkError(FileSystemError):
    def __init__(self):
        self.message = "Directory is a hard link!"


class FilesAndDirectories():
    def __init__(self, is_directory, size, name):
        self.is_directory = is_directory
        self.size = size
        self.name = name

class Directory(FilesAndDirectories):
    def __init__(self, name):
        super().__init__(True, 1, name)
        self.directories = []
        self.files = []
        self.nodes = []


class File(FilesAndDirectories):
    def __init__(self, content, name):
        super().__init__(False, len(content) + 1, name)
        self.content = content

    def append(text):
        self.content += text
#        self.size = 1 + len(self.content)

    def truncate(text):
        self.content = text
 #       self.size = 1 + len(self.content)


class FileSystem():
    def __init__(self, size):
        self.size = size
        self.available_size = size - 1
        self.root = Directory("/")
        

    def get_node(path):
        nodes = path.split("/")
        last_node = nodes[-1]
        current_node = self.root
        next_node = nodes[1]
        #obhojdame
        for node in nodes[:-1]:
            if next_node not in current_node.directories:
                raise NodeDoesNotExistError()
            



    def create(path, directory=False, content=''):
        pass

    def remove(path, directory=False, force=True):
        pass

    def move(source, destination):
        pass

    def link(source, destination, symbolic=True):
        pass

    def mount(file_system, path):
        pass

    def unmount(path):
        pass



'''
    # test na erorite:
def f():
    raise MountPointDoesNotExistError()

try:
    f()
except FileSystemError as e:
    print ("raboti")
    print (e)

'''