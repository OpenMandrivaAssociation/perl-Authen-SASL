%define module	Authen-SASL
%define name	perl-%{module}
%define version 2.12
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	SASL Authentication framework
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/G/GB/GBARR/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Digest::HMAC_MD5)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%define _requires_exceptions perl\(GSSAPI\)

%description
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all protocols
should be able to share.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes api.txt
%{_mandir}/*/*
%{perl_vendorlib}/Authen

