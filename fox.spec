Summary:	The FOX C++ GUI Toolkit
Name:		fox
Version:	0.99.161
Release:	1
Copyright:	GNU LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
URL:		http://www.cfdrc.com/FOX/fox.html
Source0:	ftp://ftp.cfdrc.com/pub/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	Mesa

%define _prefix /usr/X11R6

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
editor and file browser, written with FOX

%package devel
Summary:	Header files and development documentation for the FOX library
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files  and development documentation for the FOX library

%package static
Summary:	FOX static libraries
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
FOX static libraries

%prep
%setup -q

%build
CPPFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g} -frtti" CFLAGS="$RPM_OPT_FLAGS -frtti" \
./configure --prefix=%{_prefix} --with-opengl=mesa --enable-release
%{__make} GL_LIBS="-lGL -lGLU"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT/%{_prefix}
cp -p pathfinder/.libs/PathFinder $RPM_BUILD_ROOT/%{_bindir}
mkdir $RPM_BUILD_ROOT/%{_prefix}/share
mv $RPM_BUILD_ROOT/%{_prefix}/man $RPM_BUILD_ROOT/%{_prefix}/share

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /%{_bindir}/reswrap
%attr(755,root,root) /%{_libdir}/libFOX-0.99.so.161.0.0
/%{_libdir}/libFOX-0.99.so.161
/%{_mandir}/*/*
%doc ADDITIONS AUTHORS BUGS INSTALL LICENSE README TRACING

%files example-apps
%defattr(644,root,root,755)
%attr(755,root,root) /%{_bindir}/textedit
%attr(755,root,root) /%{_bindir}/PathFinder

%files devel
%defattr(644,root,root,755)
/%{_includedir}/fox
/%{_libdir}/libFOX.so
/%{_libdir}/libFOX.la
%doc doc

%files static
%defattr(644,root,root,755)
/%{_libdir}/libFOX.a
