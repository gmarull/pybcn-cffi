from cffi import FFI

ffi = FFI()
ffi.cdef("""
    typedef void DIR;
    typedef long ino_t;
    typedef long off_t;

    struct dirent {
        ino_t          d_ino;       /* inode number */
        off_t          d_off;       /* offset to the next dirent */
        unsigned short d_reclen;    /* length of this record */
        unsigned char  d_type;      /* type of file; not supported
                                       by all file system types */
        char           d_name[256]; /* filename */
    };

    DIR *opendir(const char *name);
    struct dirent *readdir(DIR *dirp);
    int closedir(DIR *dirp);
""")

# load library
# None as libc is already loaded, could be explicitely loaded
lib = ffi.dlopen(None)

# open directory
dir = lib.opendir(b'/tmp')
if not dir:
    raise RuntimeError('opendir failed')

# traverse directory
dirent = lib.readdir(dir)
while dirent:
    print(ffi.string(dirent.d_name))
    dirent = lib.readdir(dir)

# close directory
lib.closedir(dir)
