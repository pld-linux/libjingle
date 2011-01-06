%define		apiver	0.5
Summary:	Google Talk's implementation of Jingle and Jingle-Audio
Summary(pl.UTF-8):	Implementacja Jingle i Jingle-Audio programu Google Talk
Name:		libjingle
Version:	0.5.1
Release:	1
License:	BSD
Group:		Applications
Source0:	http://libjingle.googlecode.com/files/%{name}-%{version}.zip
# Source0-md5:	a59bac5b6111afc79efd3d1e821c13d8
URL:		http://code.google.com/p/libjingle/
# fedora patches
Patch0:		build-sanity.patch
Patch1:		C-linkage-fix.patch
Patch2:		NULL-fix.patch
Patch3:		statfix.patch
Patch4:		uint32-fix.patch
Patch5:		timefix.patch
Patch6:		unixfilesystemfix.patch
Patch7:		system-expat.patch
Patch8:		system-srtp.patch
Patch9:		devicemanager-alsafix.patch
Patch10:	v4llookup-fix.patch
Patch11:	fixconflict.patch
Patch12:	64bittypes.patch
Patch13:	qname-threadsafe.patch
# /fedora patches
Patch100:	bashism.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libilbc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7g
BuildRequires:	ortp-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.583
BuildRequires:	speex-devel
BuildRequires:	srtp-devel
Requires:	openssl >= 0.9.7g
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	libjinglebase.so.*.*.* libjinglexmpp.so.1.0.0 libjinglep2pbase.so.1.0.0 libjinglep2pclient.so.1.0.0 libjinglesessiontunnel.so.1.0.0 libjinglesessionphone.so.1.0.0

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
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libjingle
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%patch100 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
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
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/relayserver
%attr(755,root,root) %{_bindir}/stunserver
%attr(755,root,root) %{_libdir}/libjinglebase.so.*.*.*
%ghost %{_libdir}/libjinglebase.so.1
%attr(755,root,root) %{_libdir}/libjinglep2pbase.so.*.*.*
%ghost %{_libdir}/libjinglep2pbase.so.1
%attr(755,root,root) %{_libdir}/libjinglep2pclient.so.*.*.*
%ghost %{_libdir}/libjinglep2pclient.so.1
%attr(755,root,root) %{_libdir}/libjinglesessionphone.so.*.*.*
%ghost %{_libdir}/libjinglesessionphone.so.1
%attr(755,root,root) %{_libdir}/libjinglesessiontunnel.so.*.*.*
%ghost %{_libdir}/libjinglesessiontunnel.so.1
%attr(755,root,root) %{_libdir}/libjinglexmllite.so.*.*.*
%ghost %{_libdir}/libjinglexmllite.so.1
%attr(755,root,root) %{_libdir}/libjinglexmpp.so.*.*.*
%ghost %{_libdir}/libjinglexmpp.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libjinglebase.so
%{_libdir}/libjinglep2pbase.so
%{_libdir}/libjinglep2pclient.so
%{_libdir}/libjinglesessionphone.so
%{_libdir}/libjinglesessiontunnel.so
%{_libdir}/libjinglexmllite.so
%{_libdir}/libjinglexmpp.so
%{_libdir}/libjinglebase.la
%{_libdir}/libjinglep2pbase.la
%{_libdir}/libjinglep2pclient.la
%{_libdir}/libjinglesessionphone.la
%{_libdir}/libjinglesessiontunnel.la
%{_libdir}/libjinglexmllite.la
%{_libdir}/libjinglexmpp.la
%{_includedir}/libjingle-%{apiver}
%{_pkgconfigdir}/jinglebase-%{apiver}.pc
%{_pkgconfigdir}/jinglep2p-%{apiver}.pc
%{_pkgconfigdir}/jinglesessionphone-%{apiver}.pc
%{_pkgconfigdir}/jinglesessiontunnel-%{apiver}.pc
