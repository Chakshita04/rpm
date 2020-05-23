Name:           popup
Version:        1.0.0        
Release:        1
Summary:        Generating popup messages
License:        Not Applicable
#URL:            
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-chakshita

%description
Popup is used to generate messages
Author:
Chakshita

%global debug_package %{nil}
%prep

%setup -q -c
%build
#Empty

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -a * %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#/test/file1
#/test/file2
/popup-1.0/Makefile
/popup-1.0/main.c
/popup-1.0/popup.spec

%changelog
* Sat May 16 2020 Chakshita -1.0.0-1
-Created first draft


