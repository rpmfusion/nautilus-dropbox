Name:           nautilus-dropbox
Epoch:          1
Version:        2015.10.28
Release:        3%{?dist}
Summary:        Dropbox extension for Nautilus
License:        GPLv3+
URL:            https://www.dropbox.com
Source:         https://linux.dropbox.com/packages/%{name}-%{version}.tar.bz2

# add 10 second delay to autostart to ensure it loads on session startup
Patch0:         add_startup_delay.patch

ExclusiveArch:  i686 x86_64

BuildRequires:  desktop-file-utils
BuildRequires:  nautilus-devel
BuildRequires:  python2-docutils
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pygobject2-devel
BuildRequires:  pygtk2-devel
Requires:       dropbox >= %{?epoch}:%{version}-%{release}

%description
Dropbox extension for nautilus file manager

%package -n dropbox
Summary:        Client for Linux
BuildArch:      noarch
Requires:       pygtk2
Requires:       hicolor-icon-theme

%description -n dropbox
Dropbox allows you to sync your files online and across
your computers automatically.


%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT%{_libdir} -type f -name '*.la' -delete -print

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/dropbox.desktop

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n dropbox
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun -n dropbox
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans -n dropbox
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -n dropbox
%doc ChangeLog README
%license COPYING
%{_bindir}/dropbox
%{_datadir}/nautilus-dropbox/
%{_datadir}/icons/hicolor/*
%{_mandir}/man1/dropbox.1.*
%{_datadir}/applications/dropbox.desktop

%files
%{_libdir}/nautilus/extensions-3.0/libnautilus-dropbox.so

%changelog
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


