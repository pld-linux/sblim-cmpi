Summary:	SBLIM CMPI Development Package
Summary(pl.UTF-8):	Pakiet programistyczny SBLIM SMPI
Name:		sblim-cmpi
Version:	2.0.2
Release:	1
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sblim/%{name}-devel-%{version}.tar.bz2
# Source0-md5:	f53dd04e611f7e7b2c1c5d75f3698727
URL:		http://sblim.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this package is to provide a standalone development kit
for CMPI providers. It contains the CMPI header files needed for
compilation of CMPI providers written in the C programming language.

It also contains the so-called CMPI C++ Wrapper, consisting of C++
header files and a shared library implementing the C++ support.

%description -l pl.UTF-8
Celem tego pakietu jest dostarczenie samodzielnego zestawu
programistycznego dla dostarczycieli CMPI. Zawiera pliki nagłówkowe
CMPI niezbędne do kompilacji dostarczycieli CMPI napisanych w języku
C.

Pakiet zawiera także wrapper C++ CMPI, składający się z plików
nagłówkowych i bibliotekę współdzieloną z implementacją obsługi C++.

%package devel
Summary:	Header files for SBLIM CMPI
Summary(pl.UTF-8):	Pliki nagłówkowe SBLIM CMPI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for SBLIM CMPI.

%description devel -l pl.UTF-8
Pliki nagłówkowe SBLIM CMPI.

%package static
Summary:	Static SBLIM CMPI library
Summary(pl.UTF-8):	Statyczna biblioteka SBLIM CMPI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SBLIM CMPI library.

%description static -l pl.UTF-8
Statyczna biblioteka SBLIM CMPI.

%prep
%setup -q -n %{name}-devel-%{version}

%build
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
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libcmpiCppImpl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcmpiCppImpl.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcmpiCppImpl.so
%{_libdir}/libcmpiCppImpl.la
%{_includedir}/cmpi

%files static
%defattr(644,root,root,755)
%{_libdir}/libcmpiCppImpl.a
