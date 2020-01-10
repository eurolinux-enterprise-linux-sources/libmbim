
%global _hardened_build 1

Name: libmbim
Summary: Support library for the Mobile Broadband Interface Model protocol
Version: 1.14.0
Release: 2%{?dist}
License: LGPLv2+
URL: http://freedesktop.org/software/libmbim

#
# Source from http://freedesktop.org/software/libmbim/
#
Source: http://freedesktop.org/software/libmbim/%{name}-%{version}.tar.xz

BuildRequires: glib2-devel
BuildRequires: pkgconfig
BuildRequires: automake autoconf libtool
BuildRequires: python >= 2.7
BuildRequires: pkgconfig(gudev-1.0) >= 147
BuildRequires: gtk-doc


%description
This package contains the libraries that make it easier to use MBIM
functionality from applications that use glib.


%package devel
Summary: Header files for adding MBIM support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa}

%description devel
This package contains the header and pkg-config files for developing
applications using MBIM functionality from applications that use glib.

%package utils
Summary: Utilities to use the MBIM protocol from the command line
Requires: %{name}%{?_isa} = %{version}-%{release}
License: GPLv2+

%description utils
This package contains the utilities that make it easier to use MBIM
functionality from the command line.


%prep
%setup -q

%build
%configure --disable-static --enable-gtk-doc
make %{?_smp_mflags} V=1

# Build the library with older SONAME too
rm src/libmbim-glib/libmbim-glib.la
make %{?_smp_mflags} V=1 -C src/libmbim-glib libmbim_glib_la_LDFLAGS='-version-info 2:0:2' libmbim-glib.la
mv src/libmbim-glib/.libs/libmbim-glib.so.0.2.0 .
rm src/libmbim-glib/libmbim-glib.la
make %{?_smp_mflags} V=1


%install
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.la
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference configure.ac
install libmbim-glib.so.0.2.0 %{buildroot}%{_libdir}/
ln -sf libmbim-glib.so.0.2.0 %{buildroot}%{_libdir}/libmbim-glib.so.0


%check
make check


%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%doc COPYING NEWS AUTHORS README
%{_libdir}/libmbim-glib.so.*
%{_datadir}/bash-completion


%files devel
%{_includedir}/libmbim-glib/
%{_libdir}/pkgconfig/mbim-glib.pc
%{_libdir}/libmbim-glib.so
%dir %{_datadir}/gtk-doc/html/libmbim-glib
%{_datadir}/gtk-doc/html/libmbim-glib/*

%files utils
%{_bindir}/mbimcli
%{_bindir}/mbim-network
%{_mandir}/man1/*
%{_libexecdir}/mbim-proxy


%changelog
* Wed Jul 20 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.14.0-2
- Preserve the older SONAME too

* Fri Jul 08 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.14.0-1
- Update to 1.14.0 release

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.5.0-3.20130815git
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.5.0-2.20130815git
- Mass rebuild 2013-12-27

* Thu Aug 15 2013 Dan Williams <dcbw@redhat.com> - 1.5.0-1.20130815git
- Initial Fedora release

