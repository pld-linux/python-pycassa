%define 	module	pycassa
Summary:	Simple Python Cassandra library
Summary(pl.UTF-8):	-
Name:		python-%{module}
Version:	0.2.0
Release:	0.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Development/Languages/Python
# http://github.com/downloads/vomjom/pycassa/pycassa-0.2.0.tar.gz
Source0:	http://github.com/downloads/vomjom/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	-
URL:		-
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:		python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cassandra library with the following features:
Auto-failover single or thread-local connections
A simplified version of the thrift interface
A method to map an existing class to a Cassandra ColumnFamily.
Support for SuperColumns

%description -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/TEMPLATE-*.egg-info
%endif
