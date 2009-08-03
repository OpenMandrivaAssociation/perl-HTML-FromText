%define upstream_name    HTML-FromText
%define upstream_version 2.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module to Convert plain text to HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-Email-Find
BuildRequires:	perl-Exporter-Lite
BuildRequires:	perl-HTML-Parser
BuildArch:	noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
HTML::FromText converts text to HTML.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
