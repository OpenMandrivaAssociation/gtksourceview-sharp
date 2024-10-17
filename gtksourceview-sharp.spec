%define name    gtksourceview-sharp
%define oname %name-2.0
%define version 0.12
%define release %mkrel 8
%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif
%define monoprefix %_prefix/lib
Summary:       C# language binding for the gtksourceview widget
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source:        http://go-mono.com/sources/gtksourceview-sharp-2.0/%oname-%version.tar.bz2
Patch:	       gtksourceview-sharp2-gnome-print.patch
URL:           https://www.go-mono.com
License:       LGPL
Group:         System/Libraries
Requires:      gtksourceview1.0
BuildRequires: gtksourceview1-devel
BuildRequires: gnome-sharp2-devel
BuildRequires: gnome-desktop-sharp-devel
BuildRequires: mono-tools
BuildRequires: mono-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-buildroot
BuildArch: noarch
%define _requires_exceptions ^lib.*\\|lib.*glib2.0_0

%description 
GtkSourceView-sharp is a C# language binding for the gtksourceview widget.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release
%description devel
GtkSourceView-sharp is a C# language binding for the gtksourceview widget.

%package doc
Summary: Development documentation for %name
Group: Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
GtkSourceView-sharp is a C# language binding for the gtksourceview widget.

This package contains the API documentation for the %name in
Monodoc format.


%prep
%setup -q -n %{oname}-%{version}
%patch -p0

autoreconf

%build
./configure --prefix=%_prefix --libdir=%_libdir
make

%install
rm -rf %buildroot
#mkdir -p %{buildroot}/`monodoc --get-sourcesdir`
%makeinstall apidir=%buildroot%_datadir/gapi docsdir=%{buildroot}/`monodoc --get-sourcesdir` extra_langdir=%buildroot%_datadir/gtksourceview-1.0/language-specs pkgconfigdir=%buildroot%pkgconfigdir

# remove files conflicting with newer gtksourceview
rm -f %{buildroot}/%{_datadir}/gtksourceview-1.0/language-specs/vbnet.lang
rm -f %{buildroot}/%{_datadir}/gtksourceview-1.0/language-specs/nemerle.lang


%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS
%monoprefix/mono/gac/*
%monoprefix/mono/gtksourceview-sharp-2.0/

%files devel
%defattr(-,root,root)
%{pkgconfigdir}/*
%{_datadir}/gapi/gtksourceview-api.xml

%files doc
%defattr(-,root,root)
%monoprefix/monodoc/sources/gtksourceview-sharp-docs.*

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%_bindir/monodoc --make-index > /dev/null
%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi




%changelog
* Thu Oct 13 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.12-8mdv2012.0
+ Revision: 704574
- fix autoconf call
- rebuild

* Sun Oct 10 2010 Funda Wang <fwang@mandriva.org> 0.12-7mdv2011.0
+ Revision: 584585
- rebuild for new mono

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.12-6mdv2011.0
+ Revision: 437833
- rebuild

* Tue Oct 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.12-5mdv2009.1
+ Revision: 293530
- split out devel package

* Mon Oct 13 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.12-3mdv2009.1
+ Revision: 293407
- fix build deps
- rebuild
- fix build

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.12-2mdv2009.0
+ Revision: 266996
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.12-1mdv2009.0
+ Revision: 194007
- fix requires exceptions
- new version
- fix buildrequires
- filter out new automatic mono deps

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jul 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.11-1mdv2008.0
+ Revision: 51538
- new version
- fix deps


* Thu Dec 14 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.10-7mdv2007.0
+ Revision: 96931
- Import gtksourceview-sharp

* Thu Dec 14 2006 Götz Waschk <waschk@mandriva.org> 0.10-7mdv2007.1
- remove nemerle.lang, now in gtksourceview

* Fri Sep 22 2006 Götz Waschk <waschk@mandriva.org> 0.10-6mdv2007.0
- split monodoc docs to separate package

* Wed Jul 19 2006 Götz Waschk <waschk@mandriva.org> 0.10-5mdv2007.0
- fix postun script

* Thu Sep 29 2005 Götz Waschk <waschk@mandriva.org> 0.10-4mdk
- regenerate monodoc index on postun

* Fri Aug 26 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.10-3mdk
- rebuild for new gtk-sharp2

* Sat Jul 02 2005 Götz Waschk <waschk@mandriva.org> 0.10-2mdk
- fix deps

* Sat May 21 2005 Götz Waschk <waschk@mandriva.org> 0.10-1mdk
- update file list
- new source URL
- New release 0.10

* Fri Apr 29 2005 Götz Waschk <waschk@mandriva.org> 0.7-5mdk
- move mono files to /usr/lib
- fix pkgconfig file location

* Sat Apr 02 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7-4mdk
- fix dep on libgtksourceview

* Fri Apr 01 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7-3mdk
- fix buildrequires

* Thu Mar 31 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7-2mdk
- fix buildrequires

* Thu Mar 31 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7-1mdk
- make it noarch
- update file list
- New release 0.7

* Tue Nov 16 2004 Marcel Pol <mpol@mandrake.org> 0.5-4mdk
- remove conflicting file vbnet.lang with gtksourceview-1.1.1

* Thu Jul 29 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-3mdk
- rebuild for new rpm

* Fri Jul 02 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-2mdk
- remove docs, they are already in the monodoc dir

* Fri Jul 02 2004 Götz Waschk <waschk@linux-mandrake.com> 0.5-1mdk
- call monodoc in the post scripts
- add monodoc stuff
- fix installation
- new version

* Tue Jun 22 2004 Götz Waschk <waschk@linux-mandrake.com> 0.3-3mdk
- remove generic docs
- fix configure call
- fix buildrequires

* Sat Jun 05 2004 Marcel Pol <mpol@mandrake.org> 0.3-2mdk
- don't provide gtkmozembed-sharp
- only own files we really own

* Fri Jun 04 2004 Sandino "Tigrux" Flores <tigrux@ximian.com> 0.3-1mdk
- First rpm for mandrake

