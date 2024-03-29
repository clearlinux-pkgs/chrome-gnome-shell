#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : chrome-gnome-shell
Version  : 10.1
Release  : 42
URL      : https://download.gnome.org/sources/chrome-gnome-shell/10.1/chrome-gnome-shell-10.1.tar.xz
Source0  : https://download.gnome.org/sources/chrome-gnome-shell/10.1/chrome-gnome-shell-10.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: chrome-gnome-shell-bin = %{version}-%{release}
Requires: chrome-gnome-shell-data = %{version}-%{release}
Requires: chrome-gnome-shell-license = %{version}-%{release}
Requires: chrome-gnome-shell-python = %{version}-%{release}
Requires: chrome-gnome-shell-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : gettext-dev
BuildRequires : git
BuildRequires : jq
BuildRequires : p7zip
BuildRequires : python3

%description
There is limited number of supported locales.
Google Chrome/Chromium/Vivaldi support:
ar, am, bg, bn, ca, cs, da, de, el, en, en_GB, en_US, es, es_419, et, fa, fi, fil, fr, gu, he, hi, hr, hu, id, it, ja,
kn, ko, lt, lv, ml, mr, ms, nl, no, pl, pt_BR, pt_PT, ro, ru, sk, sl, sr, sv, sw, ta, te, th, tr, uk, vi, zh_CN, zh_TW

%package bin
Summary: bin components for the chrome-gnome-shell package.
Group: Binaries
Requires: chrome-gnome-shell-data = %{version}-%{release}
Requires: chrome-gnome-shell-license = %{version}-%{release}

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
Requires: chrome-gnome-shell-python3 = %{version}-%{release}

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
cd %{_builddir}/chrome-gnome-shell-10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635711181
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake .. -DPYTHON_EXECUTABLE=/usr/bin/python3
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1635711181
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/chrome-gnome-shell
cp %{_builddir}/chrome-gnome-shell-10.1/LICENSE %{buildroot}/usr/share/package-licenses/chrome-gnome-shell/8624bcdae55baeef00cd11d5dfcfa60f68710a02
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/chrome-gnome-shell/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
