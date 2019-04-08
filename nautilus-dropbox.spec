Name:           nautilus-dropbox
Epoch:          1
Version:        2019.01.31
Release:        4%{?dist}
Summary:        Dropbox extension for Nautilus
License:        GPLv3+
URL:            https://www.dropbox.com
Source:         https://linux.dropbox.com/packages/%{name}-%{version}.tar.bz2

# links to fedora repos seems to be wrong for f30
ExcludeArch:    ppc64le

# add 10 second delay to autostart to ensure it loads on session startup
Patch0:         add_startup_delay.patch
Patch1:         python3-docutils_fix.patch
Patch2:         fix_nautilus_includes.patch

ExclusiveArch:  i686 x86_64

BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  nautilus-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-gobject
Requires:       dropbox >= %{?epoch}:%{version}-%{release}

%description
Dropbox extension for nautilus file manager

%package -n dropbox
Summary:        Client for Linux
BuildArch:      noarch
Requires:       python3-gobject
Requires:       python3-gpg

%description -n dropbox
Dropbox allows you to sync your files online and across
your computers automatically.


%prep
%autosetup -p1
autoreconf -fiv

%build
%configure --disable-static
%{make_build}

%install
%{make_install}
find %{buildroot}%{_libdir} -type f -name '*.la' -delete -print

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/dropbox.desktop


%files -n dropbox
%doc ChangeLog
%license COPYING
%{_bindir}/dropbox
%{_datadir}/nautilus-dropbox/
%{_datadir}/icons/hicolor/*/apps/dropbox.png
%{_mandir}/man1/dropbox.1.*
%{_datadir}/applications/dropbox.desktop

%files
%{_libdir}/nautilus/extensions-3.0/libnautilus-dropbox.so


%changelog
* Mon Apr 08 2019 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:2019.01.31-4
- exclude archs again

* Sun Apr 07 2019 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:2019.01.31-3
- build for all archs, except ppc64le for f30

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2019.01.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Feb 12 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:2019.01.31-1
- Updated to 2019.01.31
- Fix nautilus includes
- Fix python3-docutils

* Sun Jan 06 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1:2018.11.28-2
- add upstream patch, port pygtk2 to pygobject-introspection

* Fri Dec 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:2018.11.28-1
- Updated to 2018.11.28

* Tue Sep 25 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:2015.10.28-9
- Add upstream commit to switch to python2-gpg (rfbz#5032)

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2015.10.28-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Tue Jul 24 2018 Leigh Scott <leigh123linux@googlemail.com> - 1:2015.10.28-7
- Fix directory ownership (rfbz#4975)
- Fix scriptlets
- Fix build for f29 python changes

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:2015.10.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:2015.10.28-5
- Add requires python2-pygpgme to dropbox sub-package (rfbz #4682)

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:2015.10.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 1:2015.10.28-3
- spec file clean up

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:2015.10.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 Julian Sikorski <belegdol@fedoraproject.org> - 1:2015.10.28-1
- Updated to 2015.10.28

* Sun May 31 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:2.10.0-3
- add 10 second delay to autostart to ensure it loads on session startup

* Wed Jan 07 2015 Leigh Scott <leigh123linux@googlemail.com> - 1:2.10.0-2
- add ExclusiveArch

* Tue Dec 16 2014 Leigh Scott <leigh123linux@googlemail.com> - 1:2.10.0-1
- first build


