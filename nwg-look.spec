%global debug_package %{nil}

Name:		nwg-look
Version:	1.0.6
Release:	1
Source0:	https://github.com/nwg-piotr/nwg-look/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	GTK3 settings editor adapted to work in the wlroots environment
URL:		https://github.com/nwg-piotr/nwg-look
License:	MIT
Group:		Window Manager/Utility

BuildRequires:	go
BuildRequires:	pkgconfig(gio-2.0)

%description
Nwg-look is a GTK settings editor, designed to work properly in wlroots-based Wayland environment. The look and feel is strongly influenced by LXAppearance, but nwg-look is intended to free the user from a few inconveniences.

%prep
%autosetup -p1
tar -zxf %{SOURCE1}

%build
go build -o %{buildroot}%{_bindir}/nwg-look

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
