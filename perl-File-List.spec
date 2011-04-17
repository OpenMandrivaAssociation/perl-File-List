%define module   File-List
%define version    0.3.1
%define release    %mkrel 3

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl extension for crawling directory trees and compiling lists of files
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.gz
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*


