%define major   2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:          gigedit
Summary:       Instrument editor for gig files
Version:       0.2.0
Release:       %mkrel 1
License:       GPLv2+
Group:	       Sound
Source0:       %{name}-%{version}.tar.gz
#Patch0:		gigedit-0.1.1-gcc43.patch
URL: 	       http://www.linuxsampler.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: perl(XML::Parser)
BuildRequires: gtkmm2.4-devel
BuildRequires: libgig-devel
BuildRequires: libsndfile-devel
BuildRequires: liblinuxsampler-devel >= 0.5.0
BuildRequires: sqlite3-devel
BuildRequires: libjack-devel
BuildRequires: libalsa-devel
BuildRequires: intltool


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
%_libdir/gigedit/libgigedit.so.%{major}*

#--------------------------------------------------------------------

%package -n     %develname
Group:          Development/Other
Summary:        Libraries for %name
Requires:       %libname = %version-%release
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}%{name}1-devel

%description -n %develname
Development libraries from %name

%files -n %develname
%defattr (-,root,root)
%_libdir/gigedit/*.a
%_libdir/gigedit/*.la
%_libdir/gigedit/*.so
%_libdir/linuxsampler/plugins/*.a
%_libdir/linuxsampler/plugins/*.la
%_libdir/linuxsampler/plugins/*.so

#--------------------------------------------------------------------

%prep
rm -fr %buildroot
%setup -q -n %name-%version

%build
%configure2_5x
make

%install
make DESTDIR=%buildroot  install
%find_lang %name
%clean
rm -fr %buildroot

