#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	JPEG
%define		pnam	JFIF
Summary:	JPEG::JFIF module - reads Photoshop additional info from JPEG files (JFIF/JPEG)
Summary(pl):	Modu� JPEG::JFIF - odczytuj�cy dodatkowe informacje Photoshopa z JPEG-�w (JFIF/JPEG)
Name:		perl-JPEG-JFIF
Version:	0.10.0
Release:	3
License:	GPL
Vendor:		Marcin Krzyzanowski
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/K/KR/KRZAK/%{pnam}-%{version}.tar.gz
URL:		http://krzak.linux.net.pl/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
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

%description -l pl
Ten pakiet zawiera modu� JPEG::JFIF, kt�ry potrafi odczyta� dodatkowe
metainformacje zapisane w standardzie JFIF w plikach JPEG. Obs�uguje
niestandardowe rozwi�zania Adobe Photoshop do wersji 6 w��cznie. Nazwy
sekcji, kt�re mo�na poda� funkcji getdata() to: object_name, category,
supplemental_categories, keywords, special_instructions, byline_title,
byline, city, province_state, country_name,
original_transmission_reference, headline, credit_source, caption,
caption_writer.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

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
%dir %{perl_sitelib}/JPEG
%{perl_sitelib}/JPEG/JFIF.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test.pl
