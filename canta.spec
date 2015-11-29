%define		_rc	rc2
Summary:	Canta - sing, play and learn
Name:		canta
Version:	0.2
Release:	0.%{_rc}.0.1
License:	GPLv3
Group:		X11/Applications/Games
Source0:	http://cgit.canta-game.org/cgit.cgi/canta/snapshot/%{name}-%{version}-%{_rc}.tar.bz2
# Source0-md5:	da823e32c6712fa585752e32efe0c813
Patch0:		%{name}-install_dirs.patch
URL:		http://www.canta-game.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	canta-media
Requires:	python-Soya
Requires:	python-configobj
Requires:	python-gstreamer > 0.10
Requires:	python-mingus >= 0.4.0.1
Requires:	python-mutagen
Requires:	python-wxPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Canta's goal is to provide a platform for playing and creating songs
and singing to them into a microphone. Canta can be used just for fun
or to improve the user's musical knowledge.

%prep
%setup -q -n %{name}-%{version}-%{_rc}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/media/{songs,themes}

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/TODO docs/changelog.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}-*.egg-info
%{_pixmapsdir}/*
%{_desktopdir}/*
