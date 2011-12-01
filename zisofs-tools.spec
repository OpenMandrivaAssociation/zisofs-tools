Summary:	Utilities to create compressed CD-ROM filesystems
Name:		zisofs-tools
Version:	1.0.8
Release:	%mkrel 6
License:	GPL
Group:		Archiving/Cd burning
URL:		http://www.kernel.org/pub/linux/utils/fs/zisofs/
Source0:	http://www.kernel.org/pub/linux/utils/fs/zisofs/%{name}-%{version}.tar.bz2
Source1:	http://www.kernel.org/pub/linux/utils/fs/zisofs/%{name}-%{version}.tar.bz2.sign
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tools that, in combination with an appropriately patched version of
mkisofs, allow the creation of compressed CD-ROM filesystems.

%prep
%setup -q 

%build
%configure
%make

%install
rm -rf %{buildroot}
make install INSTALLROOT="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README zisofs.magic
%{_bindir}/mkzftree
%{_mandir}/man1/mkzftree.1*


