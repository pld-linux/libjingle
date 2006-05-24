#
# Conditional build:
%bcond_with	tests		# build with tests
#
Summary:	Google Talk's implementation of Jingle and Jingle-Audio
Summary(pl):	Implementacja Jingle i Jingle-Audio programu Google Talk
Name:		libjingle
Version:	0.3.0
Release:	0.1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	668f5c36bef2b6ac7d5ebfb4e22f6f74
#https://sourceforge.net/tracker/index.php?func=detail&aid=1483115&group_id=155094&atid=794430
Patch0:		%{name}-ortp.patch
URL:		http://code.google.com/apis/talk/
#BuildRequires:	-
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ortp-devel
BuildRequires:	speex-devel
BuildRequires:	expat-devel
#BuildRequires:	
#BuildRequires:	
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Provides:	group(foo)
#Provides:	user(foo)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libjingle is a set of C++ components provided by Google to interoperate
with Google Talk's peer-to-peer and voice calling capabilities. The
package includes source code for Google's implementation of Jingle and
Jingle-Audio, two proposed extensions to the XMPP standard that are
currently available in experimental draft form.

In addition to enabling interoperability with Google Talk, there are
several general purpose components in the library such as the P2P stack
which can be used to build a variety of communication and collaboration
applications.

#%package devel
#Summary:	Header files for ... library
#Summary(pl):	Pliki nag³ówkowe biblioteki ...
#Group:		Development/Libraries
##Requires:	%{name} = %{version}-%{release}
#
#%description devel
#This is the package containing the header files for ... library.
#
#%description devel -l pl
#Ten pakiet zawiera pliki nag³ówkowe biblioteki ....
#
#%package static
#Summary:	Static ... library
#Summary(pl):	Statyczna biblioteka ...
#Group:		Development/Libraries
#Requires:	%{name}-devel = %{version}-%{release}
#
#%description static
#Static ... library.
#
#%description static -l pl
#Statyczna biblioteka ....

%prep
%setup -q
%patch0 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
CFLAGS="%{rpmcflags} -I%{_includedir}/speex"
CXXFLAGS=${CFLAGS}
%configure \
	--with-speex="%{_prefix}" \
	--with-ilbc="%{_prefix}"
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

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

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
