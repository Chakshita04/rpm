Name:           icecast
Version:        2.4.4
Release:        0
Summary:        Xiph Streaming media server that supports multiple formats.

License:     GPL   
URL:         http://www.icecast.org/  
Vendor:         Xiph.org Foundation team@icecast.org
Source0:     http://downloads.us.xiph.org/releases/icecast/%{name}-%{version}.tar.gz  
BuildRoot:      %{_tmppath}/%{name}-root
#BuildRequires:  gcc
#Requires:       

%description
Icecast is a streaming media server which currently supports Ogg Vorbis
and MP3 audio streams. It can be used to create an Internet radio
station or a privately running jukebox and many things in between.
It is very versatile in that new formats can be added relatively
easily and supports open standards for commuincation and interaction.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=/etc


make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS TODO ChangeLog
%doc doc/*.html
%doc doc/*.jpg
%doc doc/*.css
%config(noreplace) /etc/%{name}.xml
%{_bindir}/icecast
%{_prefix}/share/icecast/*

%changelog

