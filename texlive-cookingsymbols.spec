%global tl_name cookingsymbols
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Symbols for recipes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cookingsymbols
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cookingsymbols.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cookingsymbols.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cookingsymbols.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides 11 symbols for typesetting recipes: oven, gasstove,
topheat, fanoven, gloves and dish symbol (among others). The symbols are
defined using Metafont.

