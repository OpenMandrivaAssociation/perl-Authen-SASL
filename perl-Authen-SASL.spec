%define upstream_name Authen-SASL
%define upstream_version 2.2000

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(GSSAPI\\)'
%else
%define _requires_exceptions perl\(GSSAPI\)
%endif

Summary:	SASL Authentication framework
Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/perl-authen-sasl/perl-authen-sasl
Source0:	https://cpan.metacpan.org/authors/id/E/EH/EHUELS/Authen-SASL-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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

# Crypt::URandom not yet packaged in cooker; make optional for DIGEST-MD5
sed -i -e '/Crypt::URandom/d' Makefile.PL META.yml META.json dist.ini 2>/dev/null || true
if [ -f lib/Authen/SASL/Perl/DIGEST_MD5.pm ]; then
  sed -i 's/use Crypt::URandom qw(urandom);/sub urandom { my ($n)=@_; open my $fh, "<:raw", "\/dev\/urandom" or die $!; read($fh, my $b, $n)==$n or die $!; return $b }/' \
    lib/Authen/SASL/Perl/DIGEST_MD5.pm
fi


%build
%__perl -I. Makefile.PL INSTALLDIRS=vendor < /dev/null
%make_build

%check
make test || :

%install
%make_install

%files
%doc Changes api.txt
%{perl_vendorlib}/Authen
%doc %{_mandir}/man3/*
