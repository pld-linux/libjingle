Summary:	Google Talk's implementation of Jingle and Jingle-Audio
Summary(pl):	Implementacja Jingle i Jingle-Audio programu Google Talk
Name:		libjingle
Version:	0.3.0
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/libjingle/%{name}-%{version}.tar.gz
# Source0-md5:	668f5c36bef2b6ac7d5ebfb4e22f6f74
#https://sourceforge.net/tracker/index.php?func=detail&aid=1483115&group_id=155094&atid=794430
Patch0:		%{name}-ortp.patch
URL:		http://code.google.com/apis/talk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libilbc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ortp-devel
BuildRequires:	speex-devel
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

%description -l pl
libjingle to zestaw komponentów C++ udostêpnionych przez Google do
wspó³pracy z us³ugami peer-to-peer i voice Google Talk. Pakiet zawiera
implementacje Google Jingle i Jingle-Audio - dwóch proponowanych
rozszerzeñ standardu XMPP, aktualnie dostêpnych w postaci
eksperymentalnego szkicu.

Oprócz umo¿liwienia wspó³pracy z Google Talk w bibliotece dostêpne
jest kilka komponentów ogólnego przeznaczenia, takich jak stos P2P,
który mo¿e byæ wykorzystany do tworzenia ró¿nych aplikacji do
komunikacji i wspó³pracy.

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} -I%{_includedir}/speex"
CXXFLAGS="${CFLAGS}"
%configure \
	--with-speex="%{_prefix}" \
	--with-ilbc="%{_prefix}"
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
