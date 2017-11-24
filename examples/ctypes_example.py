import ctypes as ct

# load library
# None as libc is already loaded, could be explicitely loaded
lib = ct.CDLL(None)

# declare the types needed for readdir.
class DIRENT(ct.Structure):
    _fields_ = [('d_ino', ct.c_long),
                ('d_off', ct.c_long),
                ('d_reclen', ct.c_ushort),
                ('d_type', ct.c_ubyte),
                ('d_name', ct.c_char * 256)]

DIR_p = ct.c_void_p
DIRENT_p = ct.POINTER(DIRENT)

# declare needed functions
readdir = lib.readdir
readdir.argtypes = [DIR_p]
readdir.restype = DIRENT_p

opendir = lib.opendir
opendir.argtypes = [ct.c_char_p]
opendir.restype = DIR_p

closedir = lib.closedir
closedir.argtypes = [DIR_p]
closedir.restype = ct.c_int

# open directory
dir = opendir(b'/tmp')
if not dir:
    raise RuntimeError('opendir failed')

# traverse directory
dirent = readdir(dir)
while dirent:
    print(dirent.contents.d_name)
    dirent = readdir(dir)

# close directory
closedir(dir)
