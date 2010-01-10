Summary:	Google Talk's implementation of Jingle and Jingle-Audio
Summary(pl.UTF-8):	Implementacja Jingle i Jingle-Audio programu Google Talk
Name:		libjingle
Version:	0.4.0
Release:	1
License:	BSD
Group:		Applications
Source0:	http://libjingle.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	4fd81566ead30285e157a7fa16430b6e
URL:		http://code.google.com/p/libjingle/
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
BuildRequires:	speex-devel
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

# bashism
sed 's/^\([A-Z]*\)+=\(.*\)/\1="$\1 \2"/' -i configure.ac

# outdated C++ style
sed '1i\#include <string.h>\n#include <stdlib.h>\n#include <stdio.h>' \
	-i talk/base/{basictypes.h,stringutils.h,cryptstring.h}
sed 's/std::exit/exit/; 1i\#include <stdlib.h>' -i talk/base/host.cc
sed 's/Base64:://' -i talk/base/base64.h
sed 's/Traits<char>:://' -i talk/base/stringutils.h
sed '1i\#include <malloc.h>\n#include <string.h>' -i talk/base/urlencode.cc
sed 's/std::\(strerror\|memcmp\|memcpy\)/\1/' \
	-i talk/base/{asynctcpsocket.cc,socketadapters.cc} \
	-i talk/base/{natsocketfactory.cc,natserver.cc,testclient.cc} \
	-i talk/p2p/base/{stun.cc,port.cc,relayport.cc,relayserver_main.cc,stunserver.cc,stunserver_main.cc,session_unittest.cc}

sed 's/XmppClient:://' -i talk/xmpp/xmppclient.h
sed 's/SessionManager:://' -i talk/p2p/base/sessionmanager.h

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
