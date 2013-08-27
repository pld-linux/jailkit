Summary:	Utilities to limit user accounts to specific files using chroot()
Summary(pl.UTF-8):	Narzędzia do zamykania użytkowników w ograniczonym środowisku za pomocą chroot()
Name:		jailkit
Version:	2.16
Release:	1
License:	BSD modified
Group:		Applications/System
Source0:	http://olivier.sessink.nl/jailkit/%{name}-%{version}.tar.bz2
# Source0-md5:	de43d5ba8aed1159b22b5803e0bbcca8
URL:		http://olivier.sessink.nl/jailkit/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libcap-devel
BuildRequires:	python >= 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jailkit is a set of utilities to limit user accounts to specific files
using chroot() and or specific commands. Setting up a chroot shell, a
shell limited to some specific command, or a daemon inside a chroot
jail is a lot easier using these utilities.

Jailkit has been in use for a while on CVS servers (in a chroot and
limited to cvs), sftp/scp servers (both in a chroot and limited to
sftp/scp as well as not in a chroot but only limited to sftp/scp), and
also on general servers with accounts where the shell accounts are in
a chroot.

%description -l pl.UTF-8
Jailkit to zestaw narzędzi ograniczających konta użytkowników do
określonych plików przy użyciu wywołania chroot() i/lub określonych
poleceń. Ustawianie powłoki w środowisku chroot, powłoki ograniczonej
do określonego polecenia lub demona uwięzionego w środowisku chroot
jest dzięki tym narzędziom dużo łatwiejsze.

Jailkit jest używane od jakiegoś czasu na serwerach CVS (w środowisku
chroot, z ograniczeniem do polecenia cvs), serwerach sftp/scp (zarówno
w środowisku chroot z ograniczeniem do sftp/scp, jak i bez chroota,
ale z ograniczeniem do sftp/scp), a także serwerach ogólnych
z kontami mającymi powłokę zamkniętą w środowisku chroot.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	PROCMAILPATH=/usr/bin/procmail
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README.txt
%attr(755,root,root) %{_bindir}/jk_uchroot
%attr(4755,root,root) %{_sbindir}/jk_chrootsh
%attr(755,root,root) %{_sbindir}/jk_addjailuser
%attr(755,root,root) %{_sbindir}/jk_check
%attr(755,root,root) %{_sbindir}/jk_chrootlaunch
%attr(755,root,root) %{_sbindir}/jk_cp
%attr(755,root,root) %{_sbindir}/jk_init
%attr(755,root,root) %{_sbindir}/jk_jailuser
%attr(755,root,root) %{_sbindir}/jk_list
%attr(755,root,root) %{_sbindir}/jk_lsh
%attr(755,root,root) %{_sbindir}/jk_procmailwrapper
%attr(755,root,root) %{_sbindir}/jk_socketd
%attr(755,root,root) %{_sbindir}/jk_update
%{_mandir}/man8/jailkit.8*
%{_mandir}/man8/jk_*.8*
%{_datadir}/%{name}
%dir %{_sysconfdir}/jailkit
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/jailkit/jk_*.ini
