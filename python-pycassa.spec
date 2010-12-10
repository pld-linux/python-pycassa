%define 	module	pycassa
Summary:	Simple Python Cassandra library
Summary(pl.UTF-8):	Prosta biblioteka Pythona do Cassandry
Name:		python-%{module}
Version:	0.3.0
Release:	1
License:	MIT/apache
Group:		Development/Languages/Python
Source0:	http://github.com/downloads/%{module}/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	fd6ce985200ea04987c2d53f0a958559
URL:		http://github.com/vomjom/pycassa
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
Requires:	python-thrift
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cassandra library with the following features: Auto-failover single or
thread-local connections A simplified version of the thrift interface
A method to map an existing class to a Cassandra ColumnFamily. Support
for SuperColumns.
It is last version for Cassandra 0.6.x version.

%description -l pl.UTF-8
Biblioteka dostępu do Cassandry dla Pythona posiadająca: Jednowątkowe
lub wielowątkowe interfejs Uproszczona wersję interfejsu thrift.
Metodę do mapowania klass w ColumnFamily Cassandry. Obsługę
SuperColumns.
Ostatnia werjsa przeznaczona do współpracy z linią 0.6.x Cassandry.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py --cassandra build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py --cassandra install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/cassandra
%{py_sitescriptdir}/cassandra/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
