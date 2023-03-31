%define upstream_name	 Authen-SASL
%define upstream_version 2.16

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(GSSAPI\\)'
%else
%define _requires_exceptions perl\(GSSAPI\)
%endif

Summary:	SASL Authentication framework
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/release/Authen-SASL
Source0:	https://cpan.metacpan.org/authors/id/G/GB/GBARR/Authen-SASL-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::HMAC_MD5)
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Test::More)

%description
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all protocols
should be able to share.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make_build

%install
%make_install

%files
%doc Changes api.txt
%{perl_vendorlib}/Authen
%{_mandir}/man3/*
