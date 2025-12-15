Name:		python-pure-eval
Version:	0.2.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pure_eval/pure_eval-%{version}.tar.gz
Summary:	Safely evaluate AST nodes without side effects
URL:		https://pypi.org/project/pure-eval/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Safely evaluate AST nodes without side effects

%files
%{py_sitedir}/pure_eval
%{py_sitedir}/pure_eval-*.*-info
