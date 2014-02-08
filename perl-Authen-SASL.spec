%define upstream_name	 Authen-SASL
%define upstream_version 2.15

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(GSSAPI\\)'
%else
%define _requires_exceptions perl\(GSSAPI\)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	SASL Authentication framework
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::HMAC_MD5)
BuildArch:	noarch

%description
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all protocols
should be able to share.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%__make test

%install
%makeinstall_std

%files
%doc Changes api.txt
%{_mandir}/*/*
%{perl_vendorlib}/Authen


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.150.0-6mdv2012.0
+ Revision: 765069
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 2.150.0-4
+ Revision: 763044
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.150.0-3
+ Revision: 667033
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.150.0-2mdv2011.0
+ Revision: 564730
- rebuild for perl 5.12.1

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.150.0-1mdv2011.0
+ Revision: 552257
- update to 2.15

* Tue Mar 30 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.140.100-1mdv2010.1
+ Revision: 529772
- update to 2.1401

* Fri Mar 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.140.0-1mdv2010.1
+ Revision: 518479
- update to 2.14

* Sat Sep 26 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.130.0-1mdv2010.0
+ Revision: 449368
- update to 2.13

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.120.0-1mdv2010.0
+ Revision: 406838
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.12-2mdv2009.1
+ Revision: 351675
- rebuild

* Wed Jul 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.12-1mdv2009.0
+ Revision: 230635
- update to new version 2.12

* Tue Apr 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.11-1mdv2009.0
+ Revision: 196518
- fix build dependency
- update to new version 2.11

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.10-6mdv2008.1
+ Revision: 180367
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 2.10-5mdv2008.0
+ Revision: 67596
- rebuild

* Wed Apr 25 2007 Olivier Thauvin <nanardon@mandriva.org> 2.10-4mdv2008.0
+ Revision: 18038
- rebuild


* Mon Apr 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.10-3mdk
- Don't require optional module GSSAPI

* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.10-2mdk
- fix description lines length

* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.10-1mdk
- new version
- spec cleanup
- rpmbuildupdate aware
- better summary and description
- drop useless explicit requires
- %%mkrel

* Mon May 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.09-1mdk
- 2.09

* Wed May 26 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.08-1mdk
- 2.08

* Wed Apr 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.07-1mdk
- 2.07

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.04-2mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Fri May 23 2003 François Pons <fpons@mandrakesoft.com> 2.04-1mdk
- 2.04.

