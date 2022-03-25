#
# Conditional build:
%bcond_with	tests	# unit tests (missing .util in test/server.py?)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Server to test HTTP clients
Summary(pl.UTF-8):	Serwer do testówania klientów HTTP
Name:		python-test-server
Version:	0.0.31
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/test-server/
Source0:	https://files.pythonhosted.org/packages/source/t/test-server/test-server-%{version}.tar.gz
# Source0-md5:	61afb28c2d3455f618f5bfa27bc54153
URL:		https://pypi.org/project/test-server/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-bottle >= 0.12.13
BuildRequires:	python-pytest
BuildRequires:	python-six
BuildRequires:	python-webtest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-bottle >= 0.12.13
BuildRequires:	python3-pytest
BuildRequires:	python3-six
BuildRequires:	python3-webtest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP Server to test HTTP clients.

%description -l pl.UTF-8
Serwer HTTP do testowania klientów HTTP.

%package -n python3-test-server
Summary:	Server to test HTTP clients
Summary(pl.UTF-8):	Serwer do testówania klientów HTTP
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-test-server
HTTP Server to test HTTP clients.

%description -n python3-test-server -l pl.UTF-8
Serwer HTTP do testowania klientów HTTP.

%prep
%setup -q -n test-server-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.rst 
%{py_sitescriptdir}/test_server
%{py_sitescriptdir}/test_server-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-test-server
%defattr(644,root,root,755)
%doc CHANGELOG.md README.rst 
%{py3_sitescriptdir}/test_server
%{py3_sitescriptdir}/test_server-%{version}-py*.egg-info
%endif
