%define realname opengfx

Name:           openttd-%{realname}
Version:        0.3.4
Release:        %mkrel 1
Summary:        OpenGFX graphics replacement set for OpenTTD

Group:          Games/Strategy
License:        GPLv2
URL:            http://dev.openttdcoop.org/projects/opengfx
Source0:        http://gb.binaries.openttd.org/binaries/extra/%{realname}/%{version}/%{realname}-%{version}-source.tar.gz
BuildArch:      noarch
BuildRequires:  grfcodec
Conflicts:      openttd < 1.0.0-2mdv

%description
OpenGFX is an open source graphics base set for OpenTTD which can completely
replace the TTD base set. 

%prep
%setup -q -n %{realname}-%{version}-source

#Makefile.local
cat >> Makefile.local << EOF
DO_NOT_INSTALL_DOCS = 1
DO_NOT_INSTALL_LICENSE = 1
DO_NOT_INSTALL_CHANGELOG = 1
EOF

%build
%make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_gamesdatadir}/openttd/data
%make install \
	INSTALL_DIR=%{buildroot}%{_gamesdatadir}/openttd/data \
	DOCDIR=%{buildroot}%{_docdir}/%{name}

%check
%make check

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc docs/*.txt
%{_gamesdatadir}/openttd/data/*.grf
%{_gamesdatadir}/openttd/data/*.obg
