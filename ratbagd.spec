Name:           ratbagd
Version:        0.15
Release:        1
Summary:        A DBus daemon to configure input devices, mainly gaming mice
Group:          System/Configuration
License:        MIT

URL:            https://github.com/libratbag/libratbag
Source0:        https://github.com/libratbag/libratbag/archive/v%{version}/libratbag-%{version}.tar.gz

# Fix compiling with Clang
Patch0:         https://patch-diff.githubusercontent.com/raw/libratbag/libratbag/pull/1069.patch

BuildRequires:  meson
BuildRequires:  swig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libunistring)
BuildRequires:  python3dist(evdev)
BuildRequires:  pkgconfig(python)

#needed for testsuite
BuildRequires:  valgrind
BuildRequires:  pkgconfig(check)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pygobject)

#GUI for configuration
Recommends:     piper

%description

Ratbagd is a DBus daemon which allow access to the various
features exposed by mainly gaming mices such as profiles, LED, resolution,
extra buttons, etc.

It abstracts away hardware-specific and kernel-specific quirks.

Ratbagd currently supports devices from:
  - Logitech,
  - Etekcity,
  - GSkill,
  - Roccat,
  - Steelseries.

See the device files or the wiki page for a complete list of supported devices:
https://github.com/libratbag/libratbag/wiki/Devices

Users interact through a GUI like Piper.For developers, the ratbagctl tool is
the prime tool for debugging.

%files
%{_bindir}/*
%{_datadir}/dbus-1/system-services/org.freedesktop.ratbag1.service
%{_datadir}/dbus-1/system.d/org.freedesktop.ratbag1.conf
%{_datadir}/libratbag
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_libdir}/liblur.*
%{_libdir}/pkgconfig/liblur.pc
%{_unitdir}/%{name}.service
%{_includedir}/*

%prep
%autopatch -p1
%setup -q -n libratbag-%{version}

%build
#export CC=gcc
#export CXX=g++
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%post
%systemd_post %{name}

%preun
%systemd_preun %{name}
