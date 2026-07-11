%global tl_name lshort-mongol
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.26
Release:	%{tl_revision}.1
Summary:	Short introduction to LaTeX, in Mongolian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/lshort/mongolian/lshort-mongol
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-mongol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-mongol.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A translation of Oetiker's Not so short introduction.

