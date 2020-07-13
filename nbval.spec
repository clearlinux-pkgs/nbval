#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbval
Version  : 0.9.5
Release  : 6
URL      : https://files.pythonhosted.org/packages/85/9d/7de4d58a5b423561443a738771b56794e4cb9dc51e6f2996e75737f2eddf/nbval-0.9.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/85/9d/7de4d58a5b423561443a738771b56794e4cb9dc51e6f2996e75737f2eddf/nbval-0.9.5.tar.gz
Summary  : A py.test plugin to validate Jupyter notebooks
Group    : Development/Tools
License  : BSD-3-Clause
Requires: nbval-license = %{version}-%{release}
Requires: nbval-python = %{version}-%{release}
Requires: nbval-python3 = %{version}-%{release}
Requires: coverage
Requires: ipykernel
Requires: jupyter_client
Requires: nbformat
Requires: pytest
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : ipykernel
BuildRequires : jupyter_client
BuildRequires : nbformat
BuildRequires : pytest
BuildRequires : six

%description
# Py.test plugin for validating Jupyter notebooks
[![Build Status](https://travis-ci.org/computationalmodelling/nbval.svg)](https://travis-ci.org/computationalmodelling/nbval)
[![PyPI Version](https://badge.fury.io/py/nbval.svg)](https://pypi.python.org/pypi/nbval)
[![Documentation Status](https://readthedocs.org/projects/nbval/badge/)](https://nbval.readthedocs.io/)

%package license
Summary: license components for the nbval package.
Group: Default

%description license
license components for the nbval package.


%package python
Summary: python components for the nbval package.
Group: Default
Requires: nbval-python3 = %{version}-%{release}

%description python
python components for the nbval package.


%package python3
Summary: python3 components for the nbval package.
Group: Default
Requires: python3-core
Provides: pypi(nbval)
Requires: pypi(coverage)
Requires: pypi(ipykernel)
Requires: pypi(jupyter_client)
Requires: pypi(nbformat)
Requires: pypi(pytest)
Requires: pypi(six)

%description python3
python3 components for the nbval package.


%prep
%setup -q -n nbval-0.9.5
cd %{_builddir}/nbval-0.9.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586385474
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nbval
cp %{_builddir}/nbval-0.9.5/LICENSE %{buildroot}/usr/share/package-licenses/nbval/513445083aea9d04e54fb40e2a366cd48637094d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nbval/513445083aea9d04e54fb40e2a366cd48637094d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
