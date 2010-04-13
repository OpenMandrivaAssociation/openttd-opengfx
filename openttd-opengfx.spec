%define realname opengfx

Name:           openttd-%{realname}
Version:        0.2.3
Release:        %mkrel 1
Summary:        OpenGFX graphics replacement set for OpenTTD

Group:          Games/Strategy
License:        GPLv2
URL:            http://dev.openttdcoop.org/projects/opengfx
Source0:        http://bundles.openttdcoop.org/%{realname}/releases/%{realname}-%{version}-source.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  grfcodec
BuildRequires:  nforenum
Conflicts:      openttd < 1.0.0-2mdv

%description
OpenGFX is an open source graphics base set for OpenTTD which can completely
replace the TTD base set. 

%prep
%setup -q -n %{realname}-%{version}-source

%build
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_gamesdatadir}/openttd/data
make install INSTALL_DIR=%{buildroot}%{_gamesdatadir}/openttd/data

%check
make check

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc docs/*.txt
%{_gamesdatadir}/openttd/data/%{realname}-%{version}.tar
