Name:           nautilus-dropbox
Epoch:          1
Version:        2026.01.15
Release:        1%{?dist}
Summary:        Dropbox extension for Nautilus
License:        GPL-3.0-or-later AND CC-BY-ND-3.0
URL:            https://www.dropbox.com
Source0:        https://linux.dropbox.com/packages/%{name}-%{version}.tar.bz2

# add 10 second delay to autostart to ensure it loads on session startup
Patch0:         add_startup_delay.patch

ExclusiveArch:  x86_64

BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gtk4-devel
BuildRequires:  nautilus-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-gobject
Requires:       dropbox >= %{?epoch}:%{version}-%{release}

%description
Dropbox extension for nautilus file manager

%package -n dropbox
Summary:        Client for Linux
Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       python3-gpg
Requires:       libatomic

%description -n dropbox
Dropbox allows you to sync your files online and across your computers
automatically.
Note: This package installs an open-source helper application. The version
of this application does not change as frequently as the main Dropbox
application. These packages will always install the latest version of Dropbox
for Linux.

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
%{_libdir}/nautilus/extensions-4/libnautilus-dropbox.so


%changelog
* Tue Feb 03 2026 Julian Sikorski <belegdol@fedoraproject.org> - 1:2026.01.15-1
- Update to 2026.01.15

* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:2024.04.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Apr 03 2025 Julian Sikorski <belegdol@fedoraproject.org> - 1:2024.04.17-1
- Update to 2024.04.17

* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:2023.09.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:2023.09.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:2023.09.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Julian Sikorski <belegdol@fedoraproject.org> - 1:2023.09.06-1
- Update to 2023.09.06

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:2022.12.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 01 2023 Julian Sikorski <belegdol@fedoraproject.org> - 1:2022.12.05-4
- Drop the missing icons hack now that it is no longer needed

* Thu Mar 16 2023 Julian Sikorski <belegdol@fedoraproject.org> - 1:2022.12.05-3
- It is the dropbox package which requires hicolor-icon-theme
- Drop i686 arch and make the dropbox package arched
- Switch to Source0
- Add a note that the dropbox package is a downloader for the actual client

* Tue Mar 14 2023 Julian Sikorski <belegdol@fedoraproject.org> - 1:2022.12.05-2
- Switch the License field to SPDX
- Add missing CC-BY-ND-3.0 license
- Add hicolor-icon-theme to Requires
- Re-download the source

* Thu Dec 15 2022 Julian Sikorski <belegdol@fedoraproject.org> - 1:2022.12.05-1
- Update to 2022.12.05
- Drop upstreamed patches

* Tue Nov 22 2022 Julian Sikorski <belegdol@fedoraproject.org> - 1:2020.03.04-7
- Update the PR code to latest
- Add hack fixing missing emblems

* Tue Nov 15 2022 Julian Sikorski <belegdol@fedoraproject.org> - 1:2020.03.04-6
- Add PR fixing nautilus 43+ support

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:2020.03.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:2020.03.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2020.03.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2020.03.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 24 2020 Leigh Scott <leigh123linux@gmail.com> - 1:2020.03.04-1
- Updated to 2020.03.04

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2019.02.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2019.02.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 16 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1:2019.02.14-2
- add libatomic runtime require, fix rpmfusion (#5461)

* Thu Aug 22 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:2019.02.14-1
- Updated to 2019.02.14

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:2019.01.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:2019.01.31-4
- exclude archs again

* Sun Apr 07 2019 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:2019.01.31-3
- build for all archs

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


