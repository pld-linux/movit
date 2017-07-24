#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Modern Video Toolkit - high-quality, high-performance, open-source library for video filters
Summary(pl.UTF-8):	Modern Video Toolkit - wysokiej jakości i wydajności, mające otwarte źródła biblioteka do filtrów obrazu
Name:		movit
Version:	1.5.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://movit.sesse.net/%{name}-%{version}.tar.gz
# Source0-md5:	d89dd8e6186d17932b310a654aa6eb24
URL:		https://movit.sesse.net/
BuildRequires:	SDL2-devel >= 2
BuildRequires:	SDL2_image-devel >= 2
BuildRequires:	eigen3 >= 3
BuildRequires:	fftw3-devel
BuildRequires:	gtest-devel
BuildRequires:	libepoxy-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Movit is the Modern Video Toolkit, notwithstanding that anything
that's called "modern" usually isn't, and it's really not a toolkit.

Movit aims to be a high-quality, high-performance, open-source library
for video filters.

%description -l pl.UTF-8
Nazwa Movit rozwija się jako Modern Video Toolkit (nowoczesny toolkit
do obraz), mimo że wszystko, co nazywa się "modern", zwykle takie nie
jest, a to nie jest w rzeczywistości toolkit.

Movit ma być wysokiej jakości i wydajności, mającą otwarte źródła
biblioteką do filtrów obrazu.

%package devel
Summary:	Header files for Movit library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Movit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	eigen3 >= 3
Requires:	fftw3-devel
Requires:	libepoxy-devel
Requires:	libstdc++-devel

%description devel
Header files for Movit library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Movit.

%package static
Summary:	Static Movit library
Summary(pl.UTF-8):	Statyczna biblioteka Movit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Movit library.

%description static -l pl.UTF-8
Statyczna biblioteka Movit.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmovit.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libmovit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmovit.so.6
%{_datadir}/movit

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmovit.so
%{_includedir}/movit
%{_pkgconfigdir}/movit.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmovit.a
%endif
