# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%define oname CPU-X
Name: cpu-x
Version: 3.2.3
Release: 1
Summary: CPU-X is a Free software that gathers information on CPU, motherboard and more
License: GPLv3+
Group: System/Kernel and hardware
Url: https://github.com/X0rg/CPU-X
Source: https://github.com/X0rg/CPU-X/archive/v3.2.3/%{oname}-3.2.3.tar.gz
#Buildrequires(pre): rpm-macros-cmake 
Buildrequires: cmake
#Buildrequires: gcc-c++ 
Buildrequires: pkgconfig(gtk+-3.0) 
Buildrequires: pkgconfig(libarchive) 
Buildrequires: pkgconfig(libcurl) 
Buildrequires: pkgconfig(libpci) 
Buildrequires: pkgconfig(libprocps) 
Buildrequires: pkgconfig(libstatgrab) 
Buildrequires: pkgconfig(ncurses) 
Buildrequires: pkgconfig(libcpuid)
Requires: hicolor-icon-theme

ExclusiveArch: %ix86 x86_64

%description
CPU-X is a Free software that gathers information on CPU, motherboard and more.
CPU-X is similar to CPU-Z (Windows), but CPU-X is a Free and Open Source
software designed for GNU/Linux; also, it works on *BSD.
This software is written in C and built with CMake tool.
It can be used in graphical mode by using GTK or in text-based mode by using
NCurses. A dump mode is present from command line. 

%prep
%setup -qn %{oname}-%{version}

%build
%cmake_insource
%make_build

%install
%makeinstall_std
# fix run as root for sysvinit
sed 's|Exec=/usr/bin/cpu-x_polkit|Exec=xdg-su -c /usr/bin/cpu-x|' -i %buildroot%_desktopdir/cpu-x-root.desktop
%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_iconsdir/hicolor/*/*/*
%_desktopdir/*
%_datadir/polkit-1/actions/org.pkexec.cpu-x.policy
%_datadir/metainfo/%name.appdata.xml
