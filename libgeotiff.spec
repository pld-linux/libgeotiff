Summary:	GeoTIFF library
Summary(pl):	Biblioteka GeoTIFF
Name:		libgeotiff
Version:	1.2.3
Release:	1
License:	MIT, partially Public Domain (see LICENSE)
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/geotiff/libgeotiff/%{name}-%{version}.tar.gz
# Source0-md5:	b0fa8c07232610a8ebf4213396581d00
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

%description -l pl
Ta biblioteka pozwala na odczytywanie i analizowanie znaczników
"GeoTIFF", a tak¿e definiowanie i zapisywanie znaczników w nowych
plikach.

%package devel
Summary:	GeoTIFF header files
Summary(pl):	Pliki nag³ówkowe GeoTIFF
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libtiff-devel >= 3.6.0

%description devel
Header files for GeoTIFF library.

%description devel -l pl
Pliki nag³ówkowe biblioteki GeoTIFF.

%package static
Summary:	GeoTIFF static library
Summary(pl):	Statyczna biblioteka GeoTIFF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GeoTIFF static library.

%description static -l pl
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/epsg_csv

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
