Name:           popup
Version:        1.0        
Release:        1%{?dist}
Summary:        Generating popup messages

License:        GPL-2
URL:            https://github.com/Chakshita04/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
Popup is used to generate messages

%prep
%setup -q


%build
%configure
%make_build


%install
mkdir -p "$RPM_BUILD_ROOT"
cp -R * "$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc README LICENSE CHANGELOG
/usr/bin/%{name}


%changelog
* Sun Apr 26 2020 Chakshita <chakshitamalhotra04@gmail.com> 1.0-1
- Initial package for Fedora.
