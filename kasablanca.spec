Summary:	A graphical ftp client for KDE
Summary(pl):	Graficzny klient ftp dla KDE
Name:		kasablanca
Version:	0.4.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	507e7345e3efaf1647fc164c45d3127e
Patch0:		%{name}-desktop.patch
URL:		http://kasablanca.berlios.de/
BuildRequires:	fam-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	unsermake >= 040511
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Kasablanca is a graphical ftp client for KDE. Among its features are
support for SSL/TLS encryption (both commands and data using auth TLS,
not sftp), fxp (direct ftp to ftp transfer), bookmarks, and queues.

%description -l pl
Kasablanca to graficzny klient ftp dla KDE. Obs�uguje mi�dzy innymi
szyfrowanie SSL/TLS (zar�wno polecenia, jak i dane przy u�yciu
uwierzytelnionego TLS, nie sftp), fxp (bezpo�rednie przesy�anie danych
z ftp do ftp), zak�adki i zapytania.

%prep
%setup -q
%patch0 -p1

%build
cp %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__sed} -i -e 's,\$(TOPSUBDIRS),doc po src,'  Makefile.am

%{__make} cvs -f admin/Makefile.common

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/kasablanca.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde
mv $RPM_BUILD_ROOT%{_iconsdir}/hicolor $RPM_BUILD_ROOT%{_iconsdir}/crystalsvg

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*
%{_datadir}/apps/*
%{_iconsdir}/*/*/*/*
