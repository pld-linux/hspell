%include	/usr/lib/rpm/macros.perl
Summary:	Hspell - a free Hebrew spell checker
Summary(pl):	Hspell - wolnodostךpny program do kontroli pisowni hebrajskiej
Name:		hspell
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/Text
# Source0Download: http://ivrix.org.il/projects/spell-checker/download.html
Source0:	http://ivrix.org.il/projects/spell-checker/%{name}-%{version}.tar.gz
# Source0-md5:	67f402162bdb4f5e7b3099572de1342e
URL:		http://ivrix.org.il/projects/spell-checker/
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hspell is a Hebrew SPELLer. It currently provides a mostly spell-like
interface (gives the list of wrong words in the input text), but can
also suggest corrections (-c).

%description -l he
hspell הוא מאיית עברי, המספק (בינתיים) מנשק דמוי-spell - פולט רשימה של
המילים השגויות המופיעות בקלט. זו גרסה פועלת, אולם היא איננה שלמה עדיין
- מילים תקניות רבות אינן מוכרות והן מדווחות כשגיאות. הקפדנו מאוד
על-מנת שמילים שהיא *כן* מכירה יאויתו שכונה על-פי כללי האקדמיה העברית
לכתיב חסר ניקוד )"כתיב מלא"(.

%description -l pl
hspell to program do kontroli pisowni w jךzyku hebrajskim. Udostךpnia
w wiךkszo¶ci zgodny ze spellem interfejs (podaj±cy listך b³ךdnych s³ףw
w tek¶cie wej¶ciowym), ale mo¿e tak¿e sugerowaז poprawki (-c).

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DDICTIONARY_BASE=\\\"%{_datadir}/hebrew.wgz\\\"" \
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
%{_mandir}/man3/*
