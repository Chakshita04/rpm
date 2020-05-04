Name:           popup
Version:        1.0        
Release:        1
Summary:        Generating popup messages

License:        GPLv2
URL:            http://theurbanpenguin.com
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%description
Popup is used to generate messages
Author:
Chakshita
%prep
%setup
%build
make

%install
make install

%files
%defattr(4755,root,root,0755)
/usr/bin/popup

