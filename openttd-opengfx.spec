%define realname opengfx

Name:		openttd-%{realname}
Version:	7.1
Release:	2
Summary:	OpenGFX graphics replacement set for OpenTTD
Group:		Games/Strategy
License:	GPLv2
URL:		https://dev.openttdcoop.org/projects/opengfx
Source0:	http://bundles.openttdcoop.org/opengfx/releases/%{version}/%{realname}-%{version}-source.tar.xz
#Patch0:		opengfx-0.4.1-gimpscript.patch
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRequires:	grfcodec
BuildRequires:	nml >= 0.2.4
BuildRequires:	gimp
BuildRequires:	python
Conflicts:	openttd < 1.0.0

%description
OpenGFX is an open source graphics base set for OpenTTD which can completely
replace the TTD base set.

%prep
%setup -q -n %{realname}-%{version}-source
#patch0 -p1

%build
make UNIX2DOS_FLAGS="-q" _V= PYTHON=%{__python3}

%install
mkdir -p %{buildroot}%{_gamesdatadir}/openttd/data/%{realname}
make install \
	_V= PYTHON=%{__python3} \
	INSTALL_DIR=%{buildroot}%{_gamesdatadir}/openttd/data/%{realname} \
	DOCDIR=%{buildroot}%{_gamesdatadir}/openttd/data/%{realname}


%if 0
%check
%make check
%endif

%files
%defattr(0644,root,root,0755)
%{_datadir}/games/openttd/data/opengfx/*
