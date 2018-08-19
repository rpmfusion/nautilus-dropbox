Name:           nautilus-dropbox
Epoch:          1
Version:        2015.10.28
Release:        8%{?dist}
Summary:        Dropbox extension for Nautilus
License:        GPLv3+
URL:            https://www.dropbox.com
Source:         https://linux.dropbox.com/packages/%{name}-%{version}.tar.bz2

# add 10 second delay to autostart to ensure it loads on session startup
Patch0:         add_startup_delay.patch
Patch1:         use_python2.patch

ExclusiveArch:  i686 x86_64

BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  nautilus-devel
BuildRequires:  python2-docutils
BuildRequires:  pygobject2-devel
BuildRequires:  pygtk2-devel
Requires:       dropbox >= %{?epoch}:%{version}-%{release}

%description
Dropbox extension for nautilus file manager

%package -n dropbox
Summary:        Client for Linux
BuildArch:      noarch
Requires:       pygtk2
Requires:       python2-pygpgme
Requires:       hicolor-icon-theme

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

%ldconfig_scriptlets

%files -n dropbox
%doc ChangeLog README
%license COPYING
%{_bindir}/dropbox
%{_datadir}/nautilus-dropbox/
%{_datadir}/icons/hicolor/*/apps/dropbox.png
%{_mandir}/man1/dropbox.1.*
%{_datadir}/applications/dropbox.desktop

%files
%{_libdir}/nautilus/extensions-3.0/libnautilus-dropbox.so

%changelog
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


