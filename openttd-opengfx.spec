%define realname opengfx

Name:		openttd-%{realname}
Version:	0.5.2
Release:	1
Summary:	OpenGFX graphics replacement set for OpenTTD
Group:		Games/Strategy
License:	GPLv2
URL:		http://dev.openttdcoop.org/projects/opengfx
Source0:	http://gb.binaries.openttd.org/binaries/extra/%{realname}/%{version}/%{realname}-%{version}-source.tar.xz
Patch0:		opengfx-0.4.1-gimpscript.patch
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRequires:	grfcodec
BuildRequires:	nml >= 0.2.4
BuildRequires:	gimp
Conflicts:	openttd < 1.0.0

%description
OpenGFX is an open source graphics base set for OpenTTD which can completely
replace the TTD base set.

%prep
%setup -q -n %{realname}-%{version}-source
%patch0 -p1

#Makefile.local
cat >> Makefile.local << EOF
DO_NOT_INSTALL_DOCS = 1
DO_NOT_INSTALL_LICENSE = 1
DO_NOT_INSTALL_CHANGELOG = 1
EOF

%build
make

%install
mkdir -p %{buildroot}%{_gamesdatadir}/openttd/data
%make install \
	INSTALL_DIR=%{buildroot}%{_gamesdatadir}/openttd/data \
	DOCDIR=%{buildroot}%{_docdir}/%{name}

%check
%make check

%files
%defattr(0644,root,root,0755)
%doc docs/*.txt
%{_gamesdatadir}/openttd/data/*.grf
%{_gamesdatadir}/openttd/data/*.obg


