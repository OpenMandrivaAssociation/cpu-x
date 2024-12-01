%define _empty_manifest_terminate_build 0

# Unpackaged files in buildroot should terminate build
#define _unpackaged_files_terminate_build 1
%define oname CPU-X
Name: cpu-x
Version:	5.1.1
Release:	1
Summary: CPU-X is a Free software that gathers information on CPU, motherboard and more
License: GPLv3+
Group: Monitoring
Url: https://github.com/X0rg/CPU-X
Source0: https://github.com/X0rg/CPU-X/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gettext
BuildRequires: bandwidth
BuildRequires: pkgconfig(gtk+-3.0) 
BuildRequires: pkgconfig(libarchive) 
BuildRequires: pkgconfig(libcurl) 
BuildRequires: pkgconfig(libpci) 
BuildRequires: pkgconfig(libproc2)
BuildRequires: pkgconfig(libstatgrab) 
BuildRequires: pkgconfig(ncurses) 
BuildRequires: pkgconfig(libcpuid)
BuildRequires: pkgconfig(glfw3)
BuildRequires: pkgconfig(OpenCL)
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(vulkan)
BuildRequires: mesa-opencl-devel
BuildRequires: atomic-devel

Requires: hicolor-icon-theme
Recommends: gambas3-gb-jita
Recommends: %{_lib}opencl1
Recommends: mesa-opencl
Recommends: vulkan-tools


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
%{_datadir}/glib-2.0/schemas/io.github.thetumultuousunicornofdarkness.cpu-x.gschema.xml
%{_datadir}/metainfo/io.github.thetumultuousunicornofdarkness.cpu-x.appdata.xml
%{_datadir}/polkit-1/actions/io.github.thetumultuousunicornofdarkness.cpu-x-daemon.policy
%{_datadir}/zsh/site-functions/_cpu-x
