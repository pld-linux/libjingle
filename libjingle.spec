Summary:	Google Talk's implementation of Jingle and Jingle-Audio
Summary(pl.UTF-8):   Implementacja Jingle i Jingle-Audio programu Google Talk
Name:		libjingle
Version:	0.3.10
Release:	1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/tapioca-voip/%{name}-%{version}.tar.gz
# Source0-md5:	7ee7d8c834f1e06093130a86cbb9e79a
URL:		http://code.google.com/apis/talk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7g
BuildRequires:	pkgconfig
Requires:	openssl >= 0.9.7g
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libjingle is a set of C++ components provided by Google to
interoperate with Google Talk's peer-to-peer and voice calling
capabilities. The package includes Google's implementation of Jingle
and Jingle-Audio, two proposed extensions to the XMPP standard that
are currently available in experimental draft form.

In addition to enabling interoperability with Google Talk, there are
several general purpose components in the library such as the P2P
stack which can be used to build a variety of communication and
collaboration applications.

%description -l pl.UTF-8
libjingle to zestaw komponentów C++ udostępnionych przez Google do
współpracy z usługami peer-to-peer i voice Google Talk. Pakiet zawiera
implementacje Google Jingle i Jingle-Audio - dwóch proponowanych
rozszerzeń standardu XMPP, aktualnie dostępnych w postaci
eksperymentalnego szkicu.

Oprócz umożliwienia współpracy z Google Talk w bibliotece dostępne
jest kilka komponentów ogólnego przeznaczenia, takich jak stos P2P,
który może być wykorzystany do tworzenia różnych aplikacji do
komunikacji i współpracy.

%package devel
Summary:	Header files for libjingle library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libjingle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	openssl-devel >= 0.9.7g

%description devel
This package provides the necessary header files allow you to compile
applications using libjingle.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do programowania z użyciem libjingle.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS ChangeLog COPYING DOCUMENTATION NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libjingle*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc
