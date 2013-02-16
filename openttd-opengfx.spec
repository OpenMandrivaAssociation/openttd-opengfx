%define realname opengfx

Name:		openttd-%{realname}
Version:	0.4.4
Release:	2
Summary:	OpenGFX graphics replacement set for OpenTTD
Group:		Games/Strategy
License:	GPLv2
URL:		http://dev.openttdcoop.org/projects/opengfx
Source0:	http://gb.binaries.openttd.org/binaries/extra/%{realname}/%{version}/%{realname}-%{version}-source.tar.xz
Patch0:		opengfx-0.4.1-gimpscript.patch
BuildArch:	noarch
BuildRequires:	grfcodec
BuildRequires:	nml >= 0.2.3
BuildRequires:	gimp
Conflicts:	openttd < 1.0.0

%description
OpenGFX is an open source graphics base set for OpenTTD which can completely
replace the TTD base set.

%prep
%setup -q -n %{realname}-%{version}-source
%patch0 -p1

#Makefile.local
%__cat >> Makefile.local << EOF
DO_NOT_INSTALL_DOCS = 1
DO_NOT_INSTALL_LICENSE = 1
DO_NOT_INSTALL_CHANGELOG = 1
EOF

%build
%__make

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_gamesdatadir}/openttd/data
%make install \
	INSTALL_DIR=%{buildroot}%{_gamesdatadir}/openttd/data \
	DOCDIR=%{buildroot}%{_docdir}/%{name}

%check
%make check

%clean
%__rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc docs/*.txt
%{_gamesdatadir}/openttd/data/*.grf
%{_gamesdatadir}/openttd/data/*.obg


%changelog
* Mon Apr 16 2012 Andrey Bondrov <abondrov@mandriva.org> 0.4.4-1
+ Revision: 791271
- New version 0.4.4

* Fri Jan 06 2012 Andrey Bondrov <abondrov@mandriva.org> 0.4.1-1
+ Revision: 757984
- New version 0.4.1, add gimp and nml to BR

* Mon Oct 03 2011 Andrey Bondrov <abondrov@mandriva.org> 0.3.6-1
+ Revision: 702519
- New version: 0.3.6

* Wed May 25 2011 Jani Välimaa <wally@mandriva.org> 0.3.4-1
+ Revision: 679047
- new version 0.3.4

* Sat Apr 02 2011 Jani Välimaa <wally@mandriva.org> 0.3.3-1
+ Revision: 649765
- new version 0.3.3
- drop buildroot definition

* Thu Dec 23 2010 Jani Välimaa <wally@mandriva.org> 0.3.2-1mdv2011.0
+ Revision: 624012
- new version 0.3.2

* Tue Sep 21 2010 Jani Välimaa <wally@mandriva.org> 0.3.1-3mdv2011.0
+ Revision: 580387
- new version 0.3.1

* Fri Sep 10 2010 Jani Välimaa <wally@mandriva.org> 0.3.0-3mdv2011.0
+ Revision: 577129
- fix file permissions

* Fri Sep 10 2010 Jani Välimaa <wally@mandriva.org> 0.3.0-2mdv2011.0
+ Revision: 577076
- don't install docs twice

* Fri Sep 10 2010 Jani Välimaa <wally@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 577071
- new version 0.3.0
- fix source url
- fix file list

* Mon May 03 2010 Jani Välimaa <wally@mandriva.org> 0.2.4-1mdv2011.0
+ Revision: 541786
- new version 0.2.4

* Tue Apr 13 2010 Jani Välimaa <wally@mandriva.org> 0.2.3-1mdv2010.1
+ Revision: 534620
- import openttd-opengfx


