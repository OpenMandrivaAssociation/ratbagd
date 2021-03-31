Name:           ratbagd
Version:        0.15
Release:        %mkrel 1
Summary:        A DBus daemon to configure input devices, mainly gaming mice
Group:          System/Configuration
License:        MIT

URL:            https://github.com/libratbag/libratbag
Source0:        https://github.com/libratbag/libratbag/archive/v%{version}/libratbag-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  swig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  libunistring-devel
BuildRequires:  python3-evdev
BuildRequires:  pkgconfig(python3)

#needed for testsuite
BuildRequires:  valgrind
BuildRequires:  pkgconfig(check)
BuildRequires:  python3-lxml
BuildRequires:  python3-gobject3

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
%setup -q -n libratbag-%{version}

%build

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