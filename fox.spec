#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	The FOX C++ GUI Toolkit
Summary(pl.UTF-8):	FOX - toolkit graficzny w C++
Name:		fox
Version:	1.6.34
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.fox-toolkit.com/pub/%{name}-%{version}.tar.gz
# Source0-md5:	920124025d6495bbd008be635ff759ad
Patch0:		%{name}-opt.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-Makefile.patch
URL:		http://www.fox-toolkit.org/fox.html
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	bzip2-devel >= 1.0.2
BuildRequires:	cups-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.5
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 3.5.7
BuildRequires:	libtool >= 2:1.5
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
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
Requires:	libjpeg-devel >= 6b
Requires:	libpng-devel >= 1.2.5
Requires:	libstdc++-devel
Requires:	libtiff-devel >= 3.5.7
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXft-devel
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
	--enable-cups \
	%{?debug:--enable-debug}%{!?debug:--enable-release} \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no} \
	--with-opengl \
	--with-xft \
	--with-shape \
	--with-xshm \
	--with-xcursor \
	--with-xrandr \
	--with-xim

%{__make}

%{__make} -C doc docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf libFOX-1.6.so $RPM_BUILD_ROOT%{_libdir}/libFOX.so

rm -f doc/Makefile* doc/*/Makefile*

%{__make} -C tests clean
cp -r tests/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE_ADDENDUM README
%attr(755,root,root) %{_libdir}/libCHART-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libCHART-1.6.so.0
%attr(755,root,root) %{_libdir}/libFOX-1.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libFOX-1.6.so.0

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/adie
%attr(755,root,root) %{_bindir}/calculator
%attr(755,root,root) %{_bindir}/PathFinder
%attr(755,root,root) %{_bindir}/shutterbug
%attr(755,root,root) %{_bindir}/Adie.stx
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc ADDITIONS TRACING
%attr(755,root,root) %{_bindir}/fox-config
%attr(755,root,root) %{_bindir}/reswrap
%attr(755,root,root) %{_libdir}/libCHART-1.6.so
%attr(755,root,root) %{_libdir}/libFOX-1.6.so
%attr(755,root,root) %{_libdir}/libFOX.so
%{_libdir}/libCHART-1.6.la
%{_libdir}/libFOX-1.6.la
%{_includedir}/fox-1.6
%{_pkgconfigdir}/fox.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libCHART-1.6.a
%{_libdir}/libFOX-1.6.a
%endif

%files doc
%defattr(644,root,root,755)
%doc doc/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
