#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : chrome-gnome-shell
Version  : 10.1
Release  : 19
URL      : https://download.gnome.org/sources/chrome-gnome-shell/10.1/chrome-gnome-shell-10.1.tar.xz
Source0  : https://download.gnome.org/sources/chrome-gnome-shell/10.1/chrome-gnome-shell-10.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: chrome-gnome-shell-bin
Requires: chrome-gnome-shell-python3
Requires: chrome-gnome-shell-data
Requires: chrome-gnome-shell-license
Requires: chrome-gnome-shell-python
BuildRequires : cmake
BuildRequires : jq
BuildRequires : p7zip
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
There is limited number of supported locales.
Google Chrome/Chromium/Vivaldi support:
ar, am, bg, bn, ca, cs, da, de, el, en, en_GB, en_US, es, es_419, et, fa, fi, fil, fr, gu, he, hi, hr, hu, id, it, ja,
kn, ko, lt, lv, ml, mr, ms, nl, no, pl, pt_BR, pt_PT, ro, ru, sk, sl, sr, sv, sw, ta, te, th, tr, uk, vi, zh_CN, zh_TW

%package bin
Summary: bin components for the chrome-gnome-shell package.
Group: Binaries
Requires: chrome-gnome-shell-data
Requires: chrome-gnome-shell-license

%description bin
bin components for the chrome-gnome-shell package.


%package data
Summary: data components for the chrome-gnome-shell package.
Group: Data

%description data
data components for the chrome-gnome-shell package.


%package license
Summary: license components for the chrome-gnome-shell package.
Group: Default

%description license
license components for the chrome-gnome-shell package.


%package python
Summary: python components for the chrome-gnome-shell package.
Group: Default
Requires: chrome-gnome-shell-python3

%description python
python components for the chrome-gnome-shell package.


%package python3
Summary: python3 components for the chrome-gnome-shell package.
Group: Default
Requires: python3-core

%description python3
python3 components for the chrome-gnome-shell package.


%prep
%setup -q -n chrome-gnome-shell-10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530382835
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DPYTHON_EXECUTABLE=/usr/bin/python3
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1530382835
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/chrome-gnome-shell
cp LICENSE %{buildroot}/usr/share/doc/chrome-gnome-shell/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/mozilla/native-messaging-hosts/org.gnome.chrome_gnome_shell.json

%files bin
%defattr(-,root,root,-)
/usr/bin/chrome-gnome-shell

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.ChromeGnomeShell.desktop
/usr/share/dbus-1/services/org.gnome.ChromeGnomeShell.service
/usr/share/icons/gnome/128x128/apps/org.gnome.ChromeGnomeShell.png
/usr/share/icons/gnome/16x16/apps/org.gnome.ChromeGnomeShell.png
/usr/share/icons/gnome/48x48/apps/org.gnome.ChromeGnomeShell.png

%files license
%defattr(-,root,root,-)
/usr/share/doc/chrome-gnome-shell/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
