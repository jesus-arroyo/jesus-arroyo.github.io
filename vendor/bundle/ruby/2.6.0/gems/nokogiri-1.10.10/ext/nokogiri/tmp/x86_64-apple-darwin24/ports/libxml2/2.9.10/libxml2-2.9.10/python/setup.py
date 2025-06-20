#!/usr/bin/python -u
#
# Setup script for libxml2 and libxslt if found
#
import sys, os
from distutils.core import setup, Extension

# Below ROOT, we expect to find include, include/libxml2, lib and bin.
# On *nix, it is not needed (but should not harm),
# on Windows, it is set by configure.js.
ROOT = r'/Users/jdar/My Drive/Website/jesus-arroyo.github.io/vendor/bundle/ruby/2.6.0/gems/nokogiri-1.10.10/ports/x86_64-apple-darwin24/libxml2/2.9.10'

# Thread-enabled libxml2
with_threads = 1

# If this flag is set (windows only),
# a private copy of the dlls are included in the package.
# If this flag is not set, the libxml2 and libxslt
# dlls must be found somewhere in the PATH at runtime.
WITHDLLS = 1 and sys.platform.startswith('win')

def missing(file):
    if os.access(file, os.R_OK) == 0:
        return 1
    return 0

try:
    HOME = os.environ['HOME']
except:
    HOME="C:"

if WITHDLLS:
    # libxml dlls (expected in ROOT/bin)
    dlls = [ 'iconv.dll','libxml2.dll','libxslt.dll','libexslt.dll' ]
    dlls = [os.path.join(ROOT,'bin',dll) for dll in dlls]

    # create __init__.py for the libxmlmods package
    if not os.path.exists("libxmlmods"):
        os.mkdir("libxmlmods")
        open("libxmlmods/__init__.py","w").close()

    def altImport(s):
        s = s.replace("import libxml2mod","from libxmlmods import libxml2mod")
        s = s.replace("import libxsltmod","from libxmlmods import libxsltmod")
        return s

if sys.platform.startswith('win'):
    libraryPrefix = 'lib'
    platformLibs = []
else:
    libraryPrefix = ''
    platformLibs = ["m","z"]

# those are examined to find
# - libxml2/libxml/tree.h
# - iconv.h
# - libxslt/xsltconfig.h
includes_dir = [
"/usr/include",
"/usr/local/include",
"/opt/include",
os.path.join(ROOT,'include'),
HOME
];

xml_includes=""
for dir in includes_dir:
    if not missing(dir + "/libxml2/libxml/tree.h"):
        xml_includes=dir + "/libxml2"
        break;

if xml_includes == "":
    print("failed to find headers for libxml2: update includes_dir")
    sys.exit(1)

iconv_includes=""
for dir in includes_dir:
    if not missing(dir + "/iconv.h"):
        iconv_includes=dir
        break;

if iconv_includes == "":
    print("failed to find headers for libiconv: update includes_dir")
    sys.exit(1)

# those are added in the linker search path for libraries
libdirs = [
os.path.join(ROOT,'lib'),
]

xml_files = ["libxml2-api.xml", "libxml2-python-api.xml",
             "libxml.c", "libxml.py", "libxml_wrap.h", "types.c",
             "xmlgenerator.py", "README", "TODO", "drv_libxml2.py"]

xslt_files = ["libxslt-api.xml", "libxslt-python-api.xml",
             "libxslt.c", "libxsl.py", "libxslt_wrap.h",
             "xsltgenerator.py"]

if missing("libxml2-py.c") or missing("libxml2.py"):
    try:
        try:
            import xmlgenerator
        except:
            import generator
    except:
        print("failed to find and generate stubs for libxml2, aborting ...")
        print(sys.exc_info()[0], sys.exc_info()[1])
        sys.exit(1)

    head = open("libxml.py", "r")
    generated = open("libxml2class.py", "r")
    result = open("libxml2.py", "w")
    for line in head.readlines():
        if WITHDLLS:
            result.write(altImport(line))
        else:
            result.write(line)
    for line in generated.readlines():
        result.write(line)
    head.close()
    generated.close()
    result.close()

with_xslt=0
if missing("libxslt-py.c") or missing("libxslt.py"):
    if missing("xsltgenerator.py") or missing("libxslt-api.xml"):
        print("libxslt stub generator not found, libxslt not built")
    else:
        try:
            import xsltgenerator
        except:
            print("failed to generate stubs for libxslt, aborting ...")
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            head = open("libxsl.py", "r")
            generated = open("libxsltclass.py", "r")
            result = open("libxslt.py", "w")
            for line in head.readlines():
                if WITHDLLS:
                    result.write(altImport(line))
                else:
                    result.write(line)
            for line in generated.readlines():
                result.write(line)
            head.close()
            generated.close()
            result.close()
            with_xslt=1
else:
    with_xslt=1

if with_xslt == 1:
    xslt_includes=""
    for dir in includes_dir:
        if not missing(dir + "/libxslt/xsltconfig.h"):
            xslt_includes=dir + "/libxslt"
            break;

    if xslt_includes == "":
        print("failed to find headers for libxslt: update includes_dir")
        with_xslt = 0


descr = "libxml2 package"
modules = [ 'libxml2', 'drv_libxml2' ]
if WITHDLLS:
    modules.append('libxmlmods.__init__')
c_files = ['libxml2-py.c', 'libxml.c', 'types.c' ]
includes= [xml_includes, iconv_includes]
libs    = [libraryPrefix + "xml2"] + platformLibs
macros  = []
if with_threads:
    macros.append(('_REENTRANT','1'))
if with_xslt == 1:
    descr = "libxml2 and libxslt package"
    if not sys.platform.startswith('win'):
        #
        # We are gonna build 2 identical shared libs with merge initializing
        # both libxml2mod and libxsltmod
        #
        c_files = c_files + ['libxslt-py.c', 'libxslt.c']
        xslt_c_files = c_files
        macros.append(('MERGED_MODULES', '1'))
    else:
        #
        # On windows the MERGED_MODULE option is not needed
        # (and does not work)
        #
        xslt_c_files = ['libxslt-py.c', 'libxslt.c', 'types.c']
    libs.insert(0, libraryPrefix + 'exslt')
    libs.insert(0, libraryPrefix + 'xslt')
    includes.append(xslt_includes)
    modules.append('libxslt')


extens=[Extension('libxml2mod', c_files, include_dirs=includes,
                  library_dirs=libdirs,
                  libraries=libs, define_macros=macros)]
if with_xslt == 1:
    extens.append(Extension('libxsltmod', xslt_c_files, include_dirs=includes,
                            library_dirs=libdirs,
                            libraries=libs, define_macros=macros))

if missing("MANIFEST"):

    manifest = open("MANIFEST", "w")
    manifest.write("setup.py\n")
    for file in xml_files:
        manifest.write(file + "\n")
    if with_xslt == 1:
        for file in xslt_files:
            manifest.write(file + "\n")
    manifest.close()

if WITHDLLS:
    ext_package = "libxmlmods"
    if sys.version >= "2.2":
        base = "lib/site-packages/"
    else:
        base = ""
    data_files = [(base+"libxmlmods",dlls)]
else:
    ext_package = None
    data_files = []

setup (name = "libxml2-python",
       # On *nix, the version number is created from setup.py.in
       # On windows, it is set by configure.js
       version = "2.9.10",
       description = descr,
       author = "Daniel Veillard",
       author_email = "veillard@redhat.com",
       url = "http://xmlsoft.org/python.html",
       licence="MIT Licence",
       py_modules=modules,
       ext_modules=extens,
       ext_package=ext_package,
       data_files=data_files,
       )

sys.exit(0)

