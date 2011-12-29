# revision 24526
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-cookingsymbols
Version:	20111110
Release:	1
Summary:	TeXLive cookingsymbols package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cookingsymbols.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cookingsymbols.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cookingsymbols.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive cookingsymbols package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/cookingsymbols/cookingsymbols.mf
%{_texmfdistdir}/fonts/tfm/public/cookingsymbols/cookingsymbols.tfm
%{_texmfdistdir}/tex/latex/cookingsymbols/cookingsymbols.sty
%doc %{_texmfdistdir}/doc/latex/cookingsymbols/README
%doc %{_texmfdistdir}/doc/latex/cookingsymbols/cookingsymbols.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cookingsymbols/cookingsymbols.dtx
%doc %{_texmfdistdir}/source/latex/cookingsymbols/cookingsymbols.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
