Summary:	The FOX C++ GUI Toolkit
Summary(pl):	FOX - toolkit graficzny w C++
Name:		fox
Version:	1.2.9
Release:	2
License:	LGPL
Group:		X11/Libraries
Source0:	http://www.fox-toolkit.org/ftp/%{name}-%{version}.tar.gz
# Source0-md5:	6cf5a0562ea2a097e6d1e0c4fd9d1bba
Patch0:		%{name}-opt.patch
Patch1:		%{name}-link.patch
URL:		http://www.fox-toolkit.org/fox.html
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
FOX is a C++-Based Library for Graphical User Interface Development
FOX supports modern GUI features, such as Drag-and-Drop, Tooltips, Tab
Books, Tree Lists, Icons, Multiple-Document Interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for 3D
graphics. Subclassing of basic FOX widgets allows for easy extension
beyond the built-in widgets by application writers.

%description -l pl
FOX jest bibliotek± bazuj±c± na C++ do projektowania graficznych
interfejsów u¿ytkownika. Obs³uguje wiele w³a¶ciwo¶ci wspó³czesnych
GUI: Drag-and-Drop, listy, ikony, interfejsy wielodokumentowe (MDI),
liczniki, przetwarzanie w tle, automatyczne uaktualnianie GUI, obs³ugê
grafiki OpenGL. Bazowe klasy widgetów FOX pozwalaj± na ³atwe
rozszerzanie.

%package progs
Summary:	FOX example applications
Summary(pl):	Przyk³ady aplikacji w FOX
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-example-apps

%description progs
Editor and file browser, written with FOX.

%description progs -l pl
Edytor i przegl±darka plików napisane z u¿yciem toolkitu FOX.

%package devel
Summary:	Header files for FOX library
Summary(pl):	Pliki nag³ówkowe biblioteki FOX
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for FOX library.

%description devel -l pl
Pliki nag³ówkowe biblioteki FOX.

%package static
Summary:	FOX static libraries
Summary(pl):	Biblioteki statyczne FOX
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
FOX static libraries.

%description static -l pl
Biblioteki statyczne FOX.

%package doc
Summary:	Development documentation for FOX library
Summary(pl):	Dokumentacja programisty do biblioteki FOX
Group:		X11/Development/Libraries

%description doc
Development documentation for FOX library.

%description doc -l pl
Dokumentacja programisty do biblioteki FOX.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
LDFLAGS="%{rpmldflags} -L/usr/X11R6/%{_lib}"
%configure \
	--with-opengl \
	%{?debug:--enable-debug}%{!?_debug:--enable-release}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf libFOX-1.2.so $RPM_BUILD_ROOT%{_libdir}/libFOX.so

rm -f doc/Makefile* doc/*/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE_ADDENDUM README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/adie
%attr(755,root,root) %{_bindir}/calculator
%attr(755,root,root) %{_bindir}/PathFinder
%attr(755,root,root) %{_bindir}/shutterbug

%files devel
%defattr(644,root,root,755)
%doc ADDITIONS TRACING
%attr(755,root,root) %{_bindir}/reswrap
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_mandir}/man1/*
%{_includedir}/fox-1.2

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files doc
%defattr(644,root,root,755)
%doc doc/*
