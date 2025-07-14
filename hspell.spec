Summary:	Hspell - a free Hebrew spell checker
Summary(pl.UTF-8):	Hspell - wolnodostępny program do kontroli pisowni hebrajskiej
Name:		hspell
Version:	1.4
Release:	1
License:	AGPL v3
Group:		Applications/Text
# Source0Download: http://hspell.ivrix.org.il/download.html
Source0:	http://hspell.ivrix.org.il/%{name}-%{version}.tar.gz
# Source0-md5:	55d9cdc4fe576db8515945e663ef4791
Patch0:		%{name}-perl-inc.patch
URL:		http://hspell.ivrix.org.il/
BuildRequires:	awk
BuildRequires:	perl-base
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
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

%package multispell
Summary:	Multispell - merging results from two speller programs
Summary(pl.UTF-8):	Multispell - łączenie wyników z dwóch programów sprawdzających pisownię
License:	Public Domain
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
Requires:	ispell

%description multispell
Multispell is a program that lets your editor talk to two spellers
simultaneously. It launches two speller programs, one Hebrew (hspell),
one English (ispell), and merges their results.

%description multispell -l pl.UTF-8
Multispell to program pozwalający na jednoczesną współpracę z dwoma
programami kontrolującymi pisownię. Uruchamia dwa programy (hspell dla
języka hebrajskiego i ispell dla języka angielskiego) i łączy ich
wyniki.

%package devel
Summary:	Header files for hspell library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki hspell
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	zlib-devel

%description devel
Header files for hspell (Hebrew SPELLer) library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki hspell (do kontroli pisowni w języku
hebrajskim).

%package static
Summary:	Static hspell library
Summary(pl.UTF-8):	Statyczna biblioteka hspell
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hspell library.

%description static -l pl.UTF-8
Statyczna biblioteka hspell.

%prep
%setup -q
%patch -P0 -p1

%{__sed} -i -e '1s|#!.*|#!/bin/awk -f|g' wzip

%build
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	STRIP=:

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README WHATSNEW
%attr(755,root,root) %{_bindir}/hspell
%attr(755,root,root) %{_bindir}/hspell-i
%attr(755,root,root) %{_libdir}/libhspell.so.0
%{_datadir}/hspell
%{_mandir}/man1/hspell.1*

%files multispell
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/multispell

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhspell.so
%{_includedir}/hspell.h
%{_includedir}/linginfo.h
%{_mandir}/man3/hspell.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libhspell.a
