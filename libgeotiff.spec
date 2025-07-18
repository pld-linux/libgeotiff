Summary:	GeoTIFF library
Summary(pl.UTF-8):	Biblioteka GeoTIFF
Name:		libgeotiff
Version:	1.7.3
Release:	2
License:	MIT, partially Public Domain (see LICENSE)
Group:		Libraries
Source0:	http://download.osgeo.org/geotiff/libgeotiff/%{name}-%{version}.tar.gz
# Source0-md5:	cdca346d3b01d40418f4894c4beef8e9
Patch0:		%{name}-opt.patch
URL:		http://geotiff.osgeo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel >= 3.6.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	proj-devel >= 6.0.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is designed to permit the extraction and parsing of the
"GeoTIFF" Key directories, as well as definition and installation of
GeoTIFF keys in new files.

%description -l pl.UTF-8
Ta biblioteka pozwala na odczytywanie i analizowanie znaczników
"GeoTIFF", a także definiowanie i zapisywanie znaczników w nowych
plikach.

%package devel
Summary:	GeoTIFF header files
Summary(pl.UTF-8):	Pliki nagłówkowe GeoTIFF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libtiff-devel >= 3.6.0
Requires:	proj-devel >= 6.0.0

%description devel
Header files for GeoTIFF library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GeoTIFF.

%package static
Summary:	GeoTIFF static library
Summary(pl.UTF-8):	Statyczna biblioteka GeoTIFF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GeoTIFF static library.

%description static -l pl.UTF-8
Statyczna biblioteka GeoTIFF.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--with-jpeg \
	--with-zip

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgeotiff.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%attr(755,root,root) %{_bindir}/applygeo
%attr(755,root,root) %{_bindir}/geotifcp
%attr(755,root,root) %{_bindir}/listgeo
%attr(755,root,root) %{_libdir}/libgeotiff.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgeotiff.so.5
%{_mandir}/man1/applygeo.1*
%{_mandir}/man1/geotifcp.1*
%{_mandir}/man1/listgeo.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgeotiff.so
%{_includedir}/cpl_serv.h
%{_includedir}/geo_*.h
%{_includedir}/geokeys.h
%{_includedir}/geonames.h
%{_includedir}/geotiff.h
%{_includedir}/geotiffio.h
%{_includedir}/geovalues.h
%{_includedir}/xtiffio.h
%{_includedir}/epsg_*.inc
%{_includedir}/geo_ctrans.inc
%{_includedir}/geokeys*.inc
%{_pkgconfigdir}/libgeotiff.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgeotiff.a
