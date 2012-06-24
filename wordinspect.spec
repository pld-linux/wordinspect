Summary:	GTK+ frontend for dict
Summary(pl):	Nak�adka do dict w GTK+
Name:		wordinspect
Version:	0.1a
Release:	1
License:	GPL v2
Group:		Applications/Dictionaries
Source0:	http://www.suspectclass.com/~sgifford/wordinspect/files/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
URL:		http://www.tir.com/~sgifford/wordinspect/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
Requires:	dict
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Word Inspector is a graphical front-end to the "dict" program. The
dict program allows you to search through one or more dictionary-like
reference books for a word, then displays its definition. Word
Inspector expands that by allowing you to enter words to look up more
easily, easily look up words that appear in the definition for another
word, and automatically look up a word in the X Window selection.

%description -l pl
Word Inspector jest graficzn� nak�adk� na program "dict". Program dict
pozwala na poszukiwanie s�owa w jednym b�d� wielu s�ownikach, po czym
wy�wietla jego definicj�. Word Inspector rozszerza te mo�liwo�ci,
pozwajaj�c �atwiej wyszukiwa� s�owa, sprawdza� s�owa znajduj�ce si� w
definicji innego s�owa, czy automatycznie pobiera� s�owa ze schowka X
Window.

%prep
%setup -q
%patch0 -p1

%build
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install wordinspect $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/*
