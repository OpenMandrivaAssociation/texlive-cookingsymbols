Name:		texlive-cookingsymbols
Version:	35929
Release:	2
Summary:	TeXLive cookingsymbols package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cookingsymbols.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cookingsymbols.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cookingsymbols.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%define		_unpackaged_subdirs_terminate_build	0

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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
