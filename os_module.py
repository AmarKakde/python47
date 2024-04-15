import os

"""
['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping',
'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY',
'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC',
'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY',
'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 
'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', 
'__all__', '__builtins__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', '_check_methods', 
'_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_wrap_close', 
'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 
'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 
'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp',
 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 
 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_blocking', 
 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 
 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 
 'kill', 'linesep', 'link', 'listdir', 'listdrives', 'listmounts', 
 'listvolumes', 'lseek', 'lstat', 'makedirs', 'mkdir', 
 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 
 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 
 'scandir', 'sep', 'set_blocking', 'set_handle_inheritable', 'set_inheritable', 
 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 
 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 
 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 
 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 
 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 
 'waitstatus_to_exitcode', 'walk', 'write']
"""

# os.name 

print(os.name)

# current working directory

print(f'{os.getcwd()=}')

# current working directory in bytestream
print(f'{os.getcwdb()=}')

# create a directory
os.mkdir('sample') 

# delete a directory
os.rmdir('sample')

# make nested directory
os.makedirs('ak/ak1/ak2')

# remove nested empty directories 
os.removedirs('ak/ak1/ak2')

# we will check in shutil module how to remove non empty nested directories

# list directories returns list of directories in path
# os.listdir('path')  #<- provide path

# list drives 
print(os.listdrives())

# os.envion return a dict of environment variables
print(os.environ)

# os.getlogin()  get logged in user name
print(os.getlogin())

# os.getenv() returns environment variable value if present
print(os.getenv('ALLUSERSPROFILE'))

# os.scandir returns directorys entries
for val in os.scandir('.'):
    print(val)