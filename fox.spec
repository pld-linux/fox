#
# Conditional build:
%bcond_without	cups		# CUPS support
%bcond_without	openjpeg	# JPEG2000 support
%bcond_without	static_libs	# don't build static libraries
#
Summary:	The FOX C++ GUI Toolkit
Summary(pl.UTF-8):	FOX - toolkit graficzny w C++
Name:		fox
# NOTE: after switching to 1.8.x keep stable (1.8.x) on HEAD and devel (1.9.x) on DEVEL
Version:	1.7.43
Release:	3
License:	LGPL v3+ with relinking exemption
Group:		X11/Libraries
Source0:	http://ftp.fox-toolkit.org/pub/%{name}-%{version}.tar.gz
# Source0-md5:	81bf6b1c8acb2b74ecd65f6f41f50015
Patch0:		%{name}-opt.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-Makefile.patch
URL:		http://www.fox-toolkit.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	bzip2-devel >= 1.0.2
%{?with_cups:BuildRequires:	cups-devel}
BuildRequires:	doxygen
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.5
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 3.5.7
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libwebp-devel
%{?with_openjpeg:BuildRequires:	openjpeg-devel}
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	zlib-devel >= 1.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
FOX is a C++-Based Library for Graphical User Interface Development
FOX supports modern GUI features, such as Drag-and-Drop, Tooltips, Tab
Books, Tree Lists, Icons, Multiple-Document Interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for 3D
graphics. Subclassing of basic FOX widgets allows for easy extension
beyond the built-in widgets by application writers.

%description -l pl.UTF-8
FOX jest biblioteką bazującą na C++ do projektowania graficznych
interfejsów użytkownika. Obsługuje wiele właściwości współczesnych
GUI: Drag-and-Drop, listy, ikony, interfejsy wielodokumentowe (MDI),
liczniki, przetwarzanie w tle, automatyczne uaktualnianie GUI, obsługę
grafiki OpenGL. Bazowe klasy widgetów FOX pozwalają na łatwe
rozszerzanie.

%package progs
Summary:	FOX example applications
Summary(pl.UTF-8):	Przykłady aplikacji w FOX
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	fox-example-apps

%description progs
Editor and file browser, written with FOX.

%description progs -l pl.UTF-8
Edytor i przeglądarka plików napisane z użyciem toolkitu FOX.

%package devel
Summary:	Header files for FOX library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FOX
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	bzip2-devel >= 1.0.2
Requires:	cups-devel
Requires:	libjpeg-devel >= 6b
Requires:	libpng-devel >= 1.2.5
Requires:	libstdc++-devel
Requires:	libtiff-devel >= 3.5.7
Requires:	libwebp-devel
%{?with_openjpeg:Requires:	openjpeg-devel}
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXft-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	zlib-devel >= 1.1.4

%description devel
Header files for FOX library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki FOX.

%package static
Summary:	FOX static libraries
Summary(pl.UTF-8):	Biblioteki statyczne FOX
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
FOX static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne FOX.

%package doc
Summary:	Development documentation for FOX library
Summary(pl.UTF-8):	Dokumentacja programisty do biblioteki FOX
Group:		X11/Development/Libraries

%description doc
Development documentation for FOX library.

%description doc -l pl.UTF-8
Dokumentacja programisty do biblioteki FOX.

%package examples
Summary:	FOX - example programs
Summary(pl.UTF-8):	FOX - programy przykładowe
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
FOX - example programs.

%description examples -l pl.UTF-8
FOX - przykładowe programy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_cups:--enable-cups} \
	%{?debug:--enable-debug}%{!?debug:--enable-release} \
	%{?with_openjpeg:--enable-jp2} \
	--enable-static%{!?with_static_libs:=no} \
	--enable-webp \
	--with-opengl \
	--with-shape \
	--with-xcursor \
	--with-xft \
	--with-xim \
	--with-xrandr \
	--with-xshm

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf libFOX-1.7.so $RPM_BUILD_ROOT%{_libdir}/libFOX.so

%{__make} -C tests clean
cp -r tests/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} doc/Makefile* doc/*/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE_ADDENDUM README
%attr(755,root,root) %{_bindir}/ControlPanel
%attr(755,root,root) %{_libdir}/libCHART-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCHART-1.7.so.0
%attr(755,root,root) %{_libdir}/libFOX-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libFOX-1.7.so.0
%{_mandir}/man1/ControlPanel.1*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Adie.stx
%attr(755,root,root) %{_bindir}/PathFinder
%attr(755,root,root) %{_bindir}/adie
%attr(755,root,root) %{_bindir}/calculator
%attr(755,root,root) %{_bindir}/shutterbug
%{_mandir}/man1/PathFinder.1*
%{_mandir}/man1/adie.1*
%{_mandir}/man1/calculator.1*
%{_mandir}/man1/shutterbug.1*

%files devel
%defattr(644,root,root,755)
%doc ADDITIONS TRACING
%attr(755,root,root) %{_bindir}/fox-config
%attr(755,root,root) %{_bindir}/reswrap
%attr(755,root,root) %{_libdir}/libCHART-1.7.so
%attr(755,root,root) %{_libdir}/libFOX-1.7.so
%attr(755,root,root) %{_libdir}/libFOX.so
%{_libdir}/libCHART-1.7.la
%{_libdir}/libFOX-1.7.la
%{_includedir}/fox-1.7
%{_pkgconfigdir}/fox17.pc
%{_mandir}/man1/reswrap.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libCHART-1.7.a
%{_libdir}/libFOX-1.7.a
%endif

%files doc
%defattr(644,root,root,755)
%doc doc/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
