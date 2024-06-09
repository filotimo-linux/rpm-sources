Name:           filotimo-kde-overrides
Version:        1.3
Release:        1%{?dist}
Summary:        KDE defaults for Filotimo
URL:            https://github.com/filotimo-linux/filotimo-core-packages
Source0:        %URL/releases/download/latest/filotimo-kde-overrides.tar.gz
BuildArch:      noarch
License:        GPLv2+

Requires:       rsms-inter-fonts
Requires:       ibm-plex-fonts-all
Obsoletes:      plasma-discover-offline-updates
Provides:       plasma-discover-offline-updates

%description
KDE defaults for Filotimo

%define debug_package %{nil}

%prep
%setup -T -b 0 -q -n filotimo-kde-overrides

%install
mkdir -p %{buildroot}%{_sysconfdir}/
cp -rv etc/* %{buildroot}%{_sysconfdir}

%files
%license LICENSE
%{_sysconfdir}/xdg/*
%{_sysconfdir}/sddm.conf.d/*

%changelog
