Summary:	Utilities to create compressed CD-ROM filesystems
Name:		zisofs-tools
Version:	1.0.8
Release:	12
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
rm -rf $RPM_BUILD_ROOT
make install INSTALLROOT="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README zisofs.magic
%{_bindir}/mkzftree
%{_mandir}/man1/mkzftree.1*




%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.8-6mdv2011.0
+ Revision: 671959
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.8-5mdv2011.0
+ Revision: 608287
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.8-4mdv2010.1
+ Revision: 520293
- rebuilt for 2010.1

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.8-3mdv2009.1
+ Revision: 317972
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.8-2mdv2008.1
+ Revision: 179410
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Mon May 21 2007 Michael Scherer <misc@mandriva.org> 1.0.8-1mdv2008.0
+ Revision: 29070
- Update to new version 1.0.8


* Sun Jan 28 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.6-3mdv2007.0
+ Revision: 114749
- mkrel

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.0.6-2mdk
- Rebuild

* Wed Nov 10 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.0.6-1mdk
- 1.0.6

* Wed Jun 30 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.5-1mdk
- 1.0.5
- cosmetics

