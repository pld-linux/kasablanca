Summary:	A graphical ftp client for KDE
Summary(pl):	Graficzny klient ftp dla KDE
Name:		kasablanca
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	491555d8ddeb9a6627bd73b2477dbf26
URL:		http://kasablanca.berlios.de/
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Kasablanca is a graphical ftp client for KDE. Among its features are
support for SSL/TLS encryption (both commands and data using auth TLS,
not sftp), fxp (direct ftp to ftp transfer), bookmarks, and queues.

%description -l pl
Kasablanca to graficzny klient ftp dla KDE. Obs³uguje miêdzy innymi
szyfrowanie SSL/TLS (zarówno polecenia, jak i dane przy u¿yciu
uwierzytelnionego TLS, nie sftp), fxp (bezpo¶rednie przesy³anie danych
z ftp do ftp), zak³adki i zapytania.

%prep
%setup -q

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_desktopdir}/Utilities/* $RPM_BUILD_ROOT%{_desktopdir}/kde
echo "Categories=ConsoleOnly;Network;FileTransfer;" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/kasablanca.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*
%{_datadir}/apps/*
%{_iconsdir}/*/*/*/*
