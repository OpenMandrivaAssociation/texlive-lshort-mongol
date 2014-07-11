# revision 15878
# category Package
# catalog-ctan /info/lshort/mongolian/lshort-mongol
# catalog-date 2009-11-09 23:05:00 +0100
# catalog-license lppl
# catalog-version 4.26
Name:		texlive-lshort-mongol
Version:	4.26
Release:	8
Summary:	Short introduction to LaTeX, in Mongolian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/mongolian/lshort-mongol
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-mongol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-mongol.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A translation of Oetiker's Not so short introduction.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/00README
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/CHANGES
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/MANIFEST
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/Makefile
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/README
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/TODO
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/TRANSLATIONS
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/fixdate.pl
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/lshort-mn.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/appendix.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/biblio.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/contrib.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/custom.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/fancyhea.sty
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/graphic.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/lshort-a5.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/lshort-base.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/lshort-mn.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/lshort.sty
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/lssym.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/math.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/mylayout.sty
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/overview.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/spec.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/things.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/title.tex
%doc %{_texmfdistdir}/doc/latex/lshort-mongol/src/typeset.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.26-2
+ Revision: 753475
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.26-1
+ Revision: 718895
- texlive-lshort-mongol
- texlive-lshort-mongol
- texlive-lshort-mongol
- texlive-lshort-mongol

