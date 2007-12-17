%define module  HTML-FromText
%define version 2.05
%define release %mkrel 3

Summary:	Perl module to Convert plain text to HTML
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	ftp://www.cpan.org/modules/by-module/HTML/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Email-Find
BuildRequires:	perl-Exporter-Lite
BuildRequires:	perl-HTML-Parser
BuildArch:	noarch

%description
HTML::FromText converts text to HTML.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
#make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc Changes README
%{perl_vendorlib}/HTML/FromText.pm
%{_bindir}/text2html
%{_mandir}/man*/*

