Summary:	SBLIM CMPI Development Package
Summary(pl.UTF-8):	Pakiet programistyczny SBLIM SMPI
Name:		sblim-cmpi
Version:	2.0.3
Release:	2
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sblim/%{name}-devel-%{version}.tar.bz2
# Source0-md5:	b934616f88a848f17ca3cf1b9e792cbf
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
nagłówkowych i bibliotekę współdzieloną z implementacją wsparcia C++.

%package devel
Summary:	Header files for SBLIM CMPI
Summary(pl.UTF-8):	Pliki nagłówkowe SBLIM CMPI
Group:		Development/Libraries

%description devel
Header files for SBLIM CMPI, needed for compilation of CMPI providers
written in the C programming language.

%description devel -l pl.UTF-8
Pliki nagłówkowe SBLIM CMPI, potrzebne do kompilacji dostarczycieli
CMPI napisanych w języku C.

%package cpp
Summary:	CMPI C++ wrapper library
Summary(pl.UTF-8):	Biblioteka wrappera C++ do CMPI
Group:		Libraries
Obsoletes:	sblim-cmpi

%description cpp
CMPI C++ Wrapper - shared library implementing the C++ support.

%description cpp -l pl.UTF-8
Wrapper C++ do CMPI - biblioteka współdzielona z implementacją
wsparcia C++.

%package cpp-devel
Summary:	Header files for CMPI C++ wrapper
Summary(pl.UTF-8):	Pliki nagłówkowe wrappera C++ do CMPI
Group:		Development/Libraries
Requires:	%{name}-cpp = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description cpp-devel
Header files for CMPI C++ wrapper.

%description cpp-devel -l pl.UTF-8
Pliki nagłówkowe wrappera C++ do CMPI.

%package cpp-static
Summary:	Static CMPI C++ wrapper library
Summary(pl.UTF-8):	Statyczna biblioteka wrappera C++ do CMPI
Group:		Development/Libraries
Requires:	%{name}-cpp-devel = %{version}-%{release}
Obsoletes:	sblim-cmpi-static

%description cpp-static
Static CMPI C++ wrapper library.

%description cpp-static -l pl.UTF-8
Statyczna biblioteka wrappera C++ do CMPI.

%prep
%setup -q -n %{name}-devel-%{version}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-devel-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	cpp -p /sbin/ldconfig
%postun	cpp -p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %{_includedir}/cmpi
%{_includedir}/cmpi/cmpidt.h
%{_includedir}/cmpi/cmpift.h
%{_includedir}/cmpi/cmpimacs.h
%{_includedir}/cmpi/cmpios.h
%{_includedir}/cmpi/cmpipl.h

%files cpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcmpiCppImpl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcmpiCppImpl.so.0

%files cpp-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcmpiCppImpl.so
%{_libdir}/libcmpiCppImpl.la
%{_includedir}/cmpi/Cmpi*.h
%{_includedir}/cmpi/Linkage.h

%files cpp-static
%defattr(644,root,root,755)
%{_libdir}/libcmpiCppImpl.a
