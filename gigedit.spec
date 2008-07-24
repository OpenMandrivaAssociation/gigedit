%define major   1
%define libname %mklibname %name %major

Name:          gigedit
Summary:       Instrument editor for gig files
Version:       0.1.1
Release:       %mkrel 3
License:       GPL
Group:	       Sound
Source0:       %{name}-%{version}.tar.gz
URL: 	       http://www.linuxsampler.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: perl(XML::Parser)
BuildRequires: gtkmm2.4-devel
BuildRequires: libgig-devel
BuildRequires: libsndfile-devel

%description
An instrument editor for gig files

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/gigedit
%{_datadir}/gigedit/status_attached.xpm
%{_datadir}/gigedit/status_detached.xpm

%dir %_docdir/gigedit
%doc %_docdir/gigedit/*.png
%doc %_docdir/gigedit/*.css
%doc %_docdir/gigedit/*.html

#--------------------------------------------------------------------

%package -n     %libname
Group:          System/Libraries
Summary:        Libraries for %name
Provides:       %name = %version-%release

%description -n %libname
Librairies from %name

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%_libdir/gigedit/libgigedit.so.1.0.0
%_libdir/gigedit/libgigedit.so.1

#--------------------------------------------------------------------

%package -n     %libname-devel
Group:          Development/Other
Summary:        Libraries for %name
Requires:       %libname = %version-%release
Provides:       %{name}-devel = %{version}-%{release}

%description -n %libname-devel
Development libraries from %name

%files -n %libname-devel
%defattr (-,root,root)
%_libdir/gigedit/libgigedit.a
%_libdir/gigedit/libgigedit.la
%_libdir/gigedit/libgigedit.so

#--------------------------------------------------------------------

%prep
rm -fr %buildroot
%setup -q -n %name-%version

%build
%configure


make

%install
make DESTDIR=%buildroot  install
%find_lang %name
%clean
rm -fr %buildroot

