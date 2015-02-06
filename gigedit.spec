%define major   2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:          gigedit
Summary:       Instrument editor for gig files
Version:       0.2.0
Release:       3
License:       GPLv2+
Group:         Sound
Source0:       %{name}-%{version}.tar.gz
#Patch0:        gigedit-0.1.1-gcc43.patch
URL:           http://www.linuxsampler.org/

BuildRequires: perl(XML::Parser)
BuildRequires: gtkmm2.4-devel
BuildRequires: libgig-devel
BuildRequires: sndfile-devel
BuildRequires: liblinuxsampler-devel >= 0.5.0
BuildRequires: sqlite3-devel
BuildRequires: jackit-devel
BuildRequires: libalsa-devel
BuildRequires: intltool
Requires: %{name}-plugins

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

%files -n %libname
%defattr(-,root,root)
%_libdir/gigedit/libgigedit.so.%{major}*

#--------------------------------------------------------------------

%package -n     %develname
Group:          Development/Other
Summary:        Libraries for %name
Requires:       %libname = %version-%release
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{_lib}%{name}1-devel

%description -n %develname
Development libraries from %name

%files -n %develname
%defattr (-,root,root)
%_libdir/gigedit/*.a
%_libdir/gigedit/*.so

#--------------------------------------------------------------------

%package plugins
Group:          Sound
Summary:        Gigedit plugin for LinuxSampler
Requires:       linuxsampler
Requires:       %{name}

%description plugins
Gigedit plugin for LinuxSampler. This plugin is required when using
the Edit button in QSampler

%files plugins
%defattr (-,root,root)
%_libdir/linuxsampler/plugins/*.a
%_libdir/linuxsampler/plugins/*.so

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
LDFLAGS="-lsigc-2.0" %configure2_5x
make

%install
make DESTDIR=%buildroot  install
%find_lang %name


%changelog
* Fri Aug 28 2009 Emmanuel Andry <eandry@mandriva.org> 0.2.0-1mdv2010.0
+ Revision: 422006
- BR libalsa-devel
- BR libjack-devel
- BR sqlite3-devel
- New version ?\1940.2.0
- drop P0
- fix license
  ?\195- diff patch for gcc43
- apply devel policy

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Dec 16 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.1.1-1mdv2008.1
+ Revision: 120477
- import gigedit


