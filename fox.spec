Summary:	The FOX C++ GUI Toolkit
Name:		fox
Version:	0.99.167
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	ftp://ftp.cfdrc.com/pub/%{name}-%{version}.tar.gz
BuildRequires:	OpenGL-devel
URL:		http://www.cfdrc.com/FOX/fox.html
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description
FOX is a C++-Based Library for Graphical User Interface Development
FOX supports modern GUI features, such as Drag-and-Drop, Tooltips, Tab
Books, Tree Lists, Icons, Multiple-Document Interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for 3D
graphics. Subclassing of basic FOX widgets allows for easy extension
beyond the built-in widgets by application writers.

%package example-apps
Summary:	FOX example applications
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Requires:	%{name} = %{version}

%description example-apps
Editor and file browser, written with FOX.

%package devel
Summary:	Header files and development documentation for the FOX library
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for the FOX library.

%package static
Summary:	FOX static libraries
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
FOX static libraries.

%prep
%setup -q

%build
CPPFLAGS="%{!?debug:$RPM_OPT_FLAGS -frtti}%{?debug:-O0 -g}" \
#CFLAGS="%{!?debug:$RPM_OPT_FLAGS -frtti}%{?debug:-O0 -g}" \
%configure \
	--with-opengl=mesa \
	--enable-release
%{__make} GL_LIBS="-lGL -lGLU"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -p pathfinder/.libs/PathFinder $RPM_BUILD_ROOT%{_bindir}

gzip -9nf ADDITIONS AUTHORS BUGS README TRACING

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/reswrap
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/*/*

%files example-apps
%defattr(644,root,root,755)
%attr(755,root,root) /%{_bindir}/textedit
%attr(755,root,root) /%{_bindir}/PathFinder

%files devel
%defattr(644,root,root,755)
%doc *.gz doc
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/fox

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
