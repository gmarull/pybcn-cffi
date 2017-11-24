from cffi import FFI

ffibuilder = FFI()
ffibuilder.set_source("_example",
        """ /* passed to the compiler */
            #include <dirent.h>
        """,
        libraries=[])

ffibuilder.cdef("""
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

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
