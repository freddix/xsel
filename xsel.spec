Summary:	X selection manipulation program
Name:		xsel
Version:	1.2.0
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	http://www.vergenet.net/~conrad/software/xsel/download/%{name}-%{version}.tar.gz
# Source0-md5:	75983f143ce83dc259796c6eaf85c8f5
URL:		http://www.vergenet.net/~conrad/software/xsel/
BuildRequires:	xorg-libSM-devel
BuildRequires:	xorg-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSel is a command-line program for getting and setting the contents of
the X selection.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/xsel
%{_mandir}/man1/xsel.1*

