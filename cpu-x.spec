%global debug_package %{nil}

# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%define oname CPU-X
Name: cpu-x
Version:	4.2.0
Release:	1
Summary: CPU-X is a Free software that gathers information on CPU, motherboard and more
License: GPLv3+
Group: Monitoring
Url: https://github.com/X0rg/CPU-X
Source0: https://github.com/X0rg/CPU-X/archive/v%{version}/%{oname}-%{version}.tar.gz
Buildrequires: cmake
BuildRequires: gettext
Buildrequires: pkgconfig(gtk+-3.0) 
Buildrequires: pkgconfig(libarchive) 
Buildrequires: pkgconfig(libcurl) 
Buildrequires: pkgconfig(libpci) 
Buildrequires: pkgconfig(libprocps) 
Buildrequires: pkgconfig(libstatgrab) 
Buildrequires: pkgconfig(ncurses) 
Buildrequires: pkgconfig(libcpuid)
BuildRequires: pkgconfig(glfw3)
Requires: hicolor-icon-theme
Recommends: gambas3-gb-jita


%description
CPU-X is a Free software that gathers information on CPU, motherboard and more.
CPU-X is similar to CPU-Z (Windows), but CPU-X is a Free and Open Source
software designed for GNU/Linux; also, it works on *BSD.
This software is written in C and built with CMake tool.
It can be used in graphical mode by using GTK or in text-based mode by using
NCurses. A dump mode is present from command line. 

%prep
%setup -qn %{oname}-%{version}
%autopatch -p1

%build
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release -DWITH_BANDWIDTH=1 -DCMAKE_INSTALL_PREFIX=/usr ..
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install

%files 
%{_usr}/bin/cpu-x
%{_usr}/share/applications/*
%{_usr}/share/cpu-x/*
%{_usr}/share/icons/*
%{_usr}/share/locale/*
%{_usr}/libexec/cpu-x-daemon
%{_datadir}/bash-completion/completions/cpu-x
%{_datadir}/fish/vendor_completions.d/cpu-x.fish
%{_datadir}/glib-2.0/schemas/org.cpu-x.gschema.xml
%{_datadir}/metainfo/org.cpu-x.appdata.xml
%{_datadir}/polkit-1/actions/org.cpu-x-daemon.policy
%{_datadir}/zsh/site-functions/_cpu-x
