from _example import lib, ffi

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
