Summary:	GeoTIFF library
Summary(pl):	Biblioteka GeoTIFF
Name:		libgeotiff
Version:	1.2.1
Release:	1
License:	MIT, partially Public Domain (see LICENSE)
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/geotiff/libgeotiff/%{name}-%{version}.tar.gz
# Source0-md5:	cd02f28915f964e4aa914e0e1b39ab4b
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
Requires:	%{name} = %{version}
Requires:	libtiff-devel

%description devel
Header files for GeoTIFF library.

%description devel -l pl
Pliki nag³ówkowe biblioteki GeoTIFF.

%package static
Summary:	GeoTIFF static library
Summary(pl):	Statyczna biblioteka GeoTIFF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GeoTIFF static library.

%description static -l pl
Statyczna biblioteka GeoTIFF.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%configure2_13

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
