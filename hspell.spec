%include	/usr/lib/rpm/macros.perl
Summary:	Hspell - a free Hebrew spell checker
Summary(pl.UTF-8):   Hspell - wolnodostępny program do kontroli pisowni hebrajskiej
Name:		hspell
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Text
# Source0Download: http://ivrix.org.il/projects/spell-checker/download.html
Source0:	http://ivrix.org.il/projects/spell-checker/%{name}-%{version}.tar.gz
# Source0-md5:	3e12fa383c2cfd430918d115f33f9841
URL:		http://ivrix.org.il/projects/spell-checker/
BuildRequires:	awk
BuildRequires:	rpm-perlprov
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hspell is a Hebrew SPELLer. It currently provides a mostly spell-like
interface (gives the list of wrong words in the input text), but can
also suggest corrections (-c).

%description -l he.UTF-8
hspell הוא מאיית עברי, המספק (בינתיים) מנשק דמוי-spell - פולט רשימה של
המילים השגויות המופיעות בקלט. זו גרסה פועלת, אולם היא איננה שלמה עדיין
- מילים תקניות רבות אינן מוכרות והן מדווחות כשגיאות. הקפדנו מאוד
על-מנת שמילים שהיא *כן* מכירה יאויתו שכונה על-פי כללי האקדמיה העברית
לכתיב חסר ניקוד )"כתיב מלא"(.

%description -l pl.UTF-8
hspell to program do kontroli pisowni w języku hebrajskim. Udostępnia
w większości zgodny ze spellem interfejs (podający listę błędnych słów
w tekście wejściowym), ale może także sugerować poprawki (-c).

%package devel
Summary:	Header files and static hspell library
Summary(pl.UTF-8):   Pliki nagłówkowe i biblioteka statyczna hspell
Group:		Development/Libraries
Requires:	zlib-devel
# doesn't require base (until shared library is made)

%description devel
Header files and static hspell (Hebrew SPELLer) library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteka statyczna hspell (do kontroli
pisowni w języku hebrajskim).

%prep
%setup -q
sed -i -e 's|#!.*|#!/bin/awk -f|g' wzip

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -DDICTIONARY_BASE=\\\"%{_datadir}/hebrew.wgz\\\"" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	MAN1=%{_mandir}/man1 \
	MAN3=%{_mandir}/man3
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO WHATSNEW
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libhspell.a
%{_includedir}/*.h
%{_mandir}/man3/hspell.3*
