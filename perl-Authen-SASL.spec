%define upstream_name	 Authen-SASL
%define upstream_version 2.15

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(GSSAPI\\)'
%else
%define _requires_exceptions perl\(GSSAPI\)
%endif

Summary:	SASL Authentication framework
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::HMAC_MD5)

%description
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all protocols
should be able to share.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes api.txt
%{perl_vendorlib}/Authen
%{_mandir}/man3/*

