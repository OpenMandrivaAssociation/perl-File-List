%define module   File-List

Name:		perl-%{module}
Version:	0.3.1
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl extension for crawling directory trees and compiling lists of files
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module crawls the directory tree starting at the provided base
directory and can return files (and/or directories if desired) matching a
regular expression

%prep
%setup -q -n File/List 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.3.1-3mdv2011.0
+ Revision: 654187
- rebuild for updated spec-helper

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-2mdv2011.0
+ Revision: 440555
- rebuild

* Tue Oct 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-1mdv2009.1
+ Revision: 293677
- import perl-File-List


* Tue Oct 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-1mdv2009.1
- initial mdv release, generated with cpan2dist
