# Created by pyp2rpm-3.1.3
%global pypi_name plotcat

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        Tool to plot live serial input

License:        GPLv3+
URL:            https://github.com/girish946/plot-cat
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch


%description
Tool to plot live serial input. plotcat works on python 2.7 and later.
plotcat comes handy when you want to plot live data that is coming form
different sensors over the serial port. For example you have to plot the output
of a temperature sensor that is coming from an Arduino or any other
micro controller for that matter; plotcat comes handy for such tasks. plotcat
sits on the top of Matplotlib and does all the initialization and drawing stuff
itself. you just have to provide the list of values to be plotted.

%package -n     python2-%{pypi_name}
Summary:        Tool to plot live serial input
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python-setuptools
BuildRequires:  python2-devel
 
Requires:       python-matplotlib
Requires:       pyserial
%description -n python2-%{pypi_name}
Tool to plot live serial input

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Tool to plot live serial input
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
 
Requires:       python3-matplotlib
Requires:       python3-pyserial
%description -n python3-%{pypi_name}
Tool to plot live serial input
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
sed -i -e '/^#!\//, 1d' plotcat/*.py


%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%if 0%{?with_python3}
%py3_install
%endif

%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc 
%{_bindir}/live_plot.py
%{python2_sitelib}/%{pypi_name}/
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info/

%if 0%{?with_python3}

%files -n python3-%{pypi_name}
%license LICENSE
%doc 
%{_bindir}/live_plot.py
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info/
%endif

%changelog
* Mon Jan 16 2017 girish joshi <girish946@gmail.com> - 1.0.2
- multiple figures can be used.
- issue with arguments for multiple plots solved.
- example for multiple figures added.
* Tue Nov 1 2016 girish joshi <girish946@gmail.com> - 1.0.1
- problem with multiple graphs corrected.
- examples corrected.
- live_plot.py updated
* Sun Aug 28 2016 girish joshi <girish946@gmail.com> - 1.0.0-2
- Initial package.
- Builds for python2 and 3 corrected.
