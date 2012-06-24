Summary:	The FOX C++ GUI Toolkit
Summary(pl):	FOX - toolkit graficzny w C++
Name:		fox
Version:	1.1.37
Release:	1
License:	LGPL
Group:		X11/Libraries
#Source0ActiveFTP
Source0:	http://ftp.fox-toolkit.org/ftp/%{name}-%{version}.tar.gz
# Source0-md5:	6248cc760ae9b464cd519b4b6e909e07
Patch0:		%{name}-opt.patch
Patch1:		%{name}-amfix.patch
Patch2:		%{name}-link.patch
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
FOX jest bibliotek� bazuj�c� na C++ do projektowania graficznych
interfejs�w u�ytkownika. Obs�uguje wiele w�a�ciwo�ci wsp�czesnych
GUI: Drag-and-Drop, listy, ikony, interfejsy wielodokumentowe (MDI),
liczniki, przetwarznie w tle, automatyczne uaktualnianie GUI, obs�ug�
grafiki OpenGL. Bazowe klasy widget�w FOX pozwalaj� na �atwe
rozszerzanie.

%package progs
Summary:	FOX example applications
Summary(pl):	Przyk�ady aplikacji w FOX
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	%{name}-example-apps

%description progs
Editor and file browser, written with FOX.

%description progs -l pl
Edytor i przegl�darka plik�w napisane z u�yciem toolkitu FOX.

%package devel
Summary:	Header files and development documentation for the FOX library
Summary(pl):	Pliki nag��wkowe i dokumentacja do biblioteki FOX
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for the FOX library.

%description devel -l pl
Pliki nag��wkowe i dokumentacja programisty do biblioteki FOX.

%package static
Summary:	FOX static libraries
Summary(pl):	Biblioteki statyczne FOX
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
FOX static libraries.

%description static -l pl
Biblioteki statyczne FOX.

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
LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
%configure \
	--with-opengl \
	%{?debug:--enable-debug}%{!?_debug:--enable-release}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

# new fox installs headers in include/fox-1.1, but apps expect them as <fox/*.h>
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	foxincludedir=%{_includedir}/fox \
	chartincludedir=%{_includedir}/fox/chart

ln -sf libFOX-1.1.so $RPM_BUILD_ROOT%{_libdir}/libFOX.so

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
%doc ADDITIONS TRACING doc
%attr(755,root,root) %{_bindir}/reswrap
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_mandir}/man1/*
%{_includedir}/fox

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
