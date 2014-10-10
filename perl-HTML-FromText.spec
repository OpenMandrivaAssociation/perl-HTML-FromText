%define upstream_name    HTML-FromText
%define upstream_version 2.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module to Convert plain text to HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Email::Find)
BuildRequires:	perl(Exporter::Lite)
BuildRequires:	perl(HTML::Parser)
BuildArch:	noarch

%description
HTML::FromText converts text to HTML.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/HTML/FromText.pm
%{_bindir}/text2html
%{_mandir}/man*/*


%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 2.50.0-1mdv2010.0
+ Revision: 407754
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.05-5mdv2009.0
+ Revision: 241469
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Apr 25 2007 Olivier Thauvin <nanardon@mandriva.org> 2.05-3mdv2008.0
+ Revision: 18067
- rebuild && mkrel


* Fri Sep 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.05-2mdk
- Rebuild; fix URL and summary

* Fri Nov 28 2003 Stefan van der Eijk <stefan@eijk.nu> 2.05-1mdk
- initial mdk package

