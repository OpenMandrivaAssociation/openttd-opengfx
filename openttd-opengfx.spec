%define realname opengfx

Name:		openttd-%{realname}
Version:	8.0
Release:	1
Summary:	OpenGFX graphics replacement set for OpenTTD
Group:		Games/Strategy
License:	GPLv2
URL:		https://dev.openttdcoop.org/projects/opengfx
#Source0:	http://bundles.openttdcoop.org/opengfx/releases/%{version}/%{realname}-%{version}-source.tar.xz
Source0:	https://github.com/OpenTTD/OpenGFX/archive/%{version}/OpenGFX-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	make
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
%autosetup -n OpenGFX-%{version} -p1

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
