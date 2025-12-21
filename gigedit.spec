%global	_disable_ld_no_undefined 1

%define	major	7
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Summary:	Instrument editor for gig files
Name:	gigedit
Version:	1.2.2
Release:	1
License:	GPLv2+
Group:	Sound
Url:	https://www.linuxsampler.org/
Source0:	https://download.linuxsampler.org/packages/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires: docbook-style-xsl
BuildRequires: intltool
BuildRequires: xsltproc
BuildRequires: perl(XML::Parser)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gdkmm-3.0)
BuildRequires: pkgconfig(gig) >= 4.5.0
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(linuxsampler) >= 2.4.0
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(sigc++-2.0)
Requires: %{name}-plugins

%description
An instrument editor for gig files.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}/status_attached.xpm
%{_datadir}/%{name}/status_detached.xpm

%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*.png
%doc %{_docdir}/%{name}/*.css
%doc %{_docdir}/%{name}/*.html

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for %{name}
Group:	System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Libraries for %{name}.

%files -n %{libname}
%{_libdir}/%{name}/libgigedit.so.%{major}*

#--------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for %{name}
Group:	Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:		%{_lib}%{name}1-devel < %{version}-%{release}

%description -n %{develname}
Development libraries from %{name}.

%files -n %{develname}
%{_libdir}/%{name}/libgigedit.so

#--------------------------------------------------------------------

%package plugins
Summary:	Gigedit plugin for LinuxSampler
Group:	Sound
Requires:	linuxsampler >= 2.4.0
Requires:	%{name} = %{version}-%{release}

%description plugins
Gigedit plugin for LinuxSampler. This plugin is required when using
the Edit button in QSampler.

%files plugins
%{_libdir}/linuxsampler/plugins/*.so

#--------------------------------------------------------------------

%prep
%autosetup -p1


%build
export CC=gcc
export CXX=g++
%configure --disable-static
%make_build


%install
%make_install

%find_lang %{name}
