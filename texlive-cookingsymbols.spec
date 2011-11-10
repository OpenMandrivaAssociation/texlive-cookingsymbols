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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
TeXLive cookingsymbols package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
