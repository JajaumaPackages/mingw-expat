%{?mingw_package_header}

Name:           mingw-expat
Version:        2.2.0
Release:        2%{?dist}
Summary:        MinGW Windows port of expat XML parser library

License:        MIT
URL:            http://www.libexpat.org/
Source0:        http://downloads.sourceforge.net/expat/expat-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils


%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

# Win32
%package -n mingw32-expat
Summary:        MinGW Windows port of expat XML parser library

%description -n mingw32-expat
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%package -n mingw32-expat-static
Summary:        Static version of the MinGW Windows expat XML parser library
Requires:       mingw32-expat = %{version}-%{release}

%description -n mingw32-expat-static
Static version of the MinGW Windows expat XML parser library.

# Win64
%package -n mingw64-expat
Summary:        MinGW Windows port of expat XML parser library

%description -n mingw64-expat
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%package -n mingw64-expat-static
Summary:        Static version of the MinGW Windows expat XML parser library
Requires:       mingw64-expat = %{version}-%{release}

%description -n mingw64-expat-static
Static version of the MinGW Windows expat XML parser library.


%?mingw_debug_package


%prep
%setup -q -n expat-%{version}


%build
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Remove .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Remove documentation which duplicates that found in the native package.
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}/man1
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}/man1


# Win32
%files -n mingw32-expat
%license COPYING
%{mingw32_bindir}/libexpat-1.dll
%{mingw32_bindir}/xmlwf
%{mingw32_libdir}/libexpat.dll.a
%{mingw32_libdir}/pkgconfig/expat.pc
%{mingw32_includedir}/expat.h
%{mingw32_includedir}/expat_config.h
%{mingw32_includedir}/expat_external.h

%files -n mingw32-expat-static
%{mingw32_libdir}/libexpat.a

# Win64
%files -n mingw64-expat
%license COPYING
%{mingw64_bindir}/libexpat-1.dll
%{mingw64_bindir}/xmlwf
%{mingw64_libdir}/libexpat.dll.a
%{mingw64_libdir}/pkgconfig/expat.pc
%{mingw64_includedir}/expat.h
%{mingw64_includedir}/expat_config.h
%{mingw64_includedir}/expat_external.h

%files -n mingw64-expat-static
%{mingw64_libdir}/libexpat.a


%changelog
* Thu Feb 02 2017 Jajauma's Packages <jajauma@yandex.ru> - 2.2.0-2
- Rebuilt with GCC 5.4.0

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 2.2.0-1
- Update to 2.2.0
- Don't set group tags
- Use license macro for COPYING

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.1.0-3
- Added static subpackages

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 03 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0
- Dropped the autoconf/libtool regeneration pieces

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.1-12
- Added win64 support
- Dropped unneeded RPM tags

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 2.0.1-11
- Remove .la files

* Tue Mar 06 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.1-10
- Renamed the source package to mingw-expat (RHBZ #800377)
- Use mingw macros without leading underscore
- Use the RPM magic to automatically generate provides/requires tags
- Automatically generate a debuginfo subpackage

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.1-9
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 13 2010 Richard W.M. Jones <rjones@redhat.com> - 2.0.1-6
- Fix Source0 URL.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  9 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.1-4
- Remove +x permissions on COPYING file.

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.1-3
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 2.0.1-2
- Include license.

* Fri Oct 31 2008 Richard W.M. Jones <rjones@redhat.com> - 2.0.1-1
- Initial RPM release.
