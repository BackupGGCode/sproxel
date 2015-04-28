# Building Sproxel #

The easiest way to build sproxel is to use Qt Creator. But here are minimal build instructions:

## Building on Linux ##

Install IlmBase from [the OpenEXR project](http://www.openexr.com/downloads.html). Unpack the archive and run:

```
./configure
make install
```

Install QT sdk from [Qt Download Page](http://qt.nokia.com/downloads/) if you don't already have it installed with your distro.

If you installed IlmBase in a non-standard location, make sure pkgconfig can find it. You may need to set PKG\_CONFIG\_PATH. If you run:

```
pkg-config --cflags IlmBase
```

It should not give you an error.

Check out the sproxel code and run:
```
qmake
make
```

That should work.

## Building on Mac ##

Same as above.

## Building on Windows ##

I build Sproxel using the LGPL MinGW release of QT.  Download it from http://qt.nokia.com/downloads/, and the mingw package from the same page.  Follow the directions for how to install each.

Next, download the IlmBase source code release from here http://www.openexr.com/downloads.html.  Building this is made much easier by downloading the MSYS package from here http://www.mingw.org/wiki/msys.  After getting that installed, follow the directions for building IlmBase here : http://sourceforge.net/apps/mediawiki/qtpfsgui/index.php?title=Compiling_on_Windows#4._OpenEXR_.28v_6.29.  This should get you a working libIex-6.dll.

From here, it's then just a matter of running qmake and making sure you include the Imath header path and libraries in the resulting makefile.  Good luck!