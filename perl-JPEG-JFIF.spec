#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	JPEG
%define		pnam	JFIF
Summary:	JPEG::JFIF Perl module - reads Photoshop additional info from JPEG files (JFIF/JPEG)
Summary(pl.UTF-8):	Moduł Perla JPEG::JFIF - odczytywanie dodatkowych informacji Photoshopa z JPEG-ów (JFIF/JPEG)
Name:		perl-JPEG-JFIF
Version:	0.12
Release:	1
License:	GPL
Vendor:		Marcin Krzyzanowski
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/K/KR/KRZAK/%{pnam}-%{version}.tar.gz
# Source0-md5:	ed7248157e87f33c550104c3b7b59dd8
URL:		http://krzak.linux.net.pl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can read additional info that is set by Adobe Photoshop
(up to version 6) in JPEG files (JFIF/JPEG format). Available sections
name for getdata(name) are: object_name, category,
supplemental_categories, keywords, special_instructions, byline_title,
byline, city, province_state, country_name,
original_transmission_reference, headline, credit source, caption,
caption_writer.

%description -l pl.UTF-8
Ten pakiet zawiera moduł JPEG::JFIF, który potrafi odczytać dodatkowe
metainformacje zapisane w standardzie JFIF w plikach JPEG. Obsługuje
niestandardowe rozwiązania Adobe Photoshop do wersji 6 włącznie. Nazwy
sekcji, które można podać funkcji getdata() to: object_name, category,
supplemental_categories, keywords, special_instructions, byline_title,
byline, city, province_state, country_name,
original_transmission_reference, headline, credit_source, caption,
caption_writer.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install example/test.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%dir %{perl_vendorlib}/JPEG
%{perl_vendorlib}/JPEG/JFIF.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test.pl
