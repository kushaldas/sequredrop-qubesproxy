Name:		securedrop-qubesproxy
Version:	0.0.1
Release:	1%{?dist}
Summary:	SecureDrop Python Qubes proxy

License:	GPLv3+
URL:		https://pypi.python.org/pypi/securedrop-qubesproxy
Source0:	https://files.pythonhosted.org/packages/source/s/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
BuildRequires:	python3-requests

Requires:       python3-requests
Requires:       securedrop-sdk

%description
The SecureDrop Python API to be used in QubesOS
as a proxy service.

%package client
Summary:        The Python client API to be called by a client in QubesOS
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       securedrop-sdk
Requires:       qubes-core-agent-qrexec
%description client
This is the actual Python client API which can be used from inside
of a QubesOS APPvm without network.


%prep
%autosetup


%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_sysconfdir}/qubes-rpc/
install -m 755 %{_builddir}/%{name}-%{version}/qubes.SDProxy \
    %{buildroot}%{_sysconfdir}/qubes-rpc/


%files client
%{python3_sitelib}/securedrop_qubesproxy*
%{python3_sitelib}/sdqubes*

%files
%doc README.md
%license LICENSE
%{_bindir}/sd-network-proxy*
%{_sysconfdir}/qubes-rpc/qubes.SDProxy


%changelog
* Mon Sep 03 2018 Kushal Das <kushal@fedoraproject.org> - 0.0.1-1
- Initial build

