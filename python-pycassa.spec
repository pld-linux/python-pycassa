%define 	module	pycassa
Summary:	Simple Python Cassandra library
Summary(pl.UTF-8):	Prosta biblioteka Pythona do Cassandry
Name:		python-%{module}
Version:	1.7.2
Release:	2
License:	MIT/apache
Group:		Development/Languages/Python
# https://github.com/downloads/pycassa/pycassa/pycassa-1.0.1.tar.gz
Source0:	http://github.com/downloads/%{module}/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	aa69935198b39fb72a2969401180ddc8
URL:		https://github.com/pycassa/pycassa
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	python-setuptools >= 0.6-2.c11 
Requires:	python-modules
Requires:	python-thrift
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cassandra library with the following features: auto-failover single or
thread-local connections, a simplified version of the thrift interface,
a method to map an existing class to a Cassandra ColumnFamily. Supports
SuperColumns.

%description -l pl.UTF-8
Biblioteka dostępu do Cassandry dla Pythona posiadająca: Jednowątkowy
lub wielowątkowy interfejs, uproszczona wersję interfejsu thrift,
metody do mapowania klas w ColumnFamily Cassandry. Wspiera obsługę
superkolumn.


%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install 

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pycassaShell

%{py_sitescriptdir}/ez_setup.py[co]

%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/cassandra
%{py_sitescriptdir}/%{module}/cassandra/*.py[co]
%dir %{py_sitescriptdir}/%{module}/logging
%{py_sitescriptdir}/%{module}/logging/*.py[co]

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
