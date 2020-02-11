Summary: Dnf plugin that removes the yum repo packages that are installed by release files.
Name: dnf-plugin-releasemods
Version: 1.0.0
Release: 1
BuildArch: noarch
Group: System
License: ASL 2.0
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: python3 >= 3.6

%description

%global py3pluginpath %{python3_sitelib}/dnf-plugins
%global pluginconfpath %{_sysconfdir}/dnf/plugins

%prep
%setup

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{py3pluginpath}
install -d %{buildroot}/%{pluginconfpath}
install -d %{buildroot}/%{_docdir}/%{name}
install -m 0644 src/releasemods.py %{buildroot}%{py3pluginpath}/releasemods.py
install -m 0644 src/releasemods.conf %{buildroot}/%{pluginconfpath}/releasemods.conf
#install -m 0644 LICENSE %{buildroot}/%{_docdir}/%{name}/LICENSE

%clean
rm -rf %{buildroot}

%package -n python3-%{name}
Summary: Dnf plugin that removes the yum repo packages that are installed by release files.
Requires: python3-dnf >= 4
Conflicts: yum-plugin-releasemods
Obsoletes: yum-plugin-releasemods

%description -n python3-%{name}
The plugin checks for dnf repository files that were installed by release packages
(such as epel-release) and removes them. This ensures that they don't interfere with
local mirrors of those repositories.

%files -n python3-%{name}
%defattr(-,root,root)
%{py3pluginpath}/releasemods.py
%{py3pluginpath}/__pycache__/
%config(noreplace) %{pluginconfpath}/releasemods.conf
%license LICENSE

%changelog
* Tue Feb 11 2020 Robert Frank <robert.frank@manchester.ac.uk>
- first version, converted from yum-plugin-releasemods
