Summary:	GeoTIFF library
Summary(pl.UTF-8):	Biblioteka GeoTIFF
Name:		libgeotiff
Version:	1.2.4
Release:	1
License:	MIT, partially Public Domain (see LICENSE)
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/geotiff/libgeotiff/%{name}-%{version}.tar.gz
# Source0-md5:	62cd4a515d1f3ba7b41cb4ed9061aa76
Patch0:		%{name}-shared-fix.patch
URL:		http://www.remotesensing.org/geotiff/geotiff.html
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel >= 3.6.0
BuildRequires:	proj-devel
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
%patch0 -p1

# workaround not to rebuild configure on make
touch configure

%build
cp -f /usr/share/automake/config.* .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README docs/*.{html,dox,txt}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libgeotiff.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgeotiff.so.1
%{_datadir}/epsg_csv

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgeotiff.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgeotiff.a
