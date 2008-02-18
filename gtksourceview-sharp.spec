%define name    gtksourceview-sharp
%define oname %name-2.0
%define version 0.11
%define release %mkrel 1
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
URL:           http://www.go-mono.com
License:       LGPL
Group:         System/Libraries
Requires:      gtksourceview1.0
BuildRequires: gtksourceview1-devel
BuildRequires: gnome-sharp2
BuildRequires: mono-tools
BuildRequires: mono-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-buildroot
BuildArch: noarch
%define _requires_exceptions ^lib.*

%description 
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


