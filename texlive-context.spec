Name:		texlive-context
Version:	58167
Release:	2
Summary:	The ConTeXt macro package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/current
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-metapost
Requires:	texlive-pdftex
Requires:	texlive-xetex
Requires:	texlive-luatex
Requires:	texlive-lm
Requires:	texlive-lm-math
Requires:	texlive-stmaryrd
Requires:	texlive-amsfonts
Requires:	texlive-mptopdf
Provides:	texlive-context.bin = %{EVRD}
%rename texlive-texmf-contex

%description
A full featured, parameter driven macro package, which fully
supports advanced interactive documents. See the ConTeXt garden
for a wealth of support information.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/*
%{_mandir}/man1/context.1*
%{_mandir}/man1/luatools.1*
%{_mandir}/man1/mtx-babel.1*
%{_mandir}/man1/mtx-base.1*
%{_mandir}/man1/mtx-bibtex.1*
%{_mandir}/man1/mtx-cache.1*
%{_mandir}/man1/mtx-chars.1*
%{_mandir}/man1/mtx-check.1*
%{_mandir}/man1/mtx-colors.1*
%{_mandir}/man1/mtx-context.1*
%{_mandir}/man1/mtx-dvi.1*
%{_mandir}/man1/mtx-epub.1*
%{_mandir}/man1/mtx-evohome.1*
%{_mandir}/man1/mtx-fcd.1*
%{_mandir}/man1/mtx-flac.1*
%{_mandir}/man1/mtx-fonts.1*
%{_mandir}/man1/mtx-grep.1*
%{_mandir}/man1/mtx-interface.1*
%{_mandir}/man1/mtx-metapost.1*
%{_mandir}/man1/mtx-modules.1*
%{_mandir}/man1/mtx-package.1*
%{_mandir}/man1/mtx-patterns.1*
%{_mandir}/man1/mtx-pdf.1*
%{_mandir}/man1/mtx-plain.1*
%{_mandir}/man1/mtx-profile.1*
%{_mandir}/man1/mtx-rsync.1*
%{_mandir}/man1/mtx-scite.1*
%{_mandir}/man1/mtx-server.1*
%{_mandir}/man1/mtx-texworks.1*
%{_mandir}/man1/mtx-timing.1*
%{_mandir}/man1/mtx-tools.1*
%{_mandir}/man1/mtx-unicode.1*
%{_mandir}/man1/mtx-unzip.1*
%{_mandir}/man1/mtx-update.1*
%{_mandir}/man1/mtx-vscode.1*
%{_mandir}/man1/mtx-watch.1*
%{_mandir}/man1/mtx-youless.1*
%{_mandir}/man1/mtxrun.1*
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texmfstart.1*
%{_texmfdistdir}/bibtex/bst/context
%{_texmfdistdir}/context
%doc %{_texmfdistdir}/doc/context
%doc %{_texmfdistdir}/doc/man/man1/*
%{_texmfdistdir}/fonts/afm/hoekwater/context
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-CNS1-4.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-GB1-4.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-Identity-0.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-Japan1-5.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-Japan1-6.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-Japan2-0.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-Korea1-2.cidmap
%{_texmfdistdir}/fonts/enc/dvips/context
%{_texmfdistdir}/fonts/map/dvips/context
%{_texmfdistdir}/fonts/map/luatex/context
%{_texmfdistdir}/fonts/map/pdftex/context
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/context
%{_texmfdistdir}/fonts/tfm/hoekwater/context
%{_texmfdistdir}/fonts/type1/hoekwater/context
%{_texmfdistdir}/metapost/context
%{_texmfdistdir}/scripts/context
%{_texmfdistdir}/tex/context
%{_texmfdistdir}/tex/generic/context
%{_texmfdistdir}/tex/latex/context
%{_datadir}/tlpkg/fmtutil.cnf.d/context

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/context/stubs/unix/context context
    ln -sf %{_texmfdistdir}/scripts/context/stubs/unix/ctxtools ctxtools
    ln -sf %{_texmfdistdir}/scripts/context/stubs/unix/luatools luatools
    ln -sf %{_texmfdistdir}/scripts/context/stubs/unix/mtxrun mtxrun
    ln -sf %{_texmfdistdir}/scripts/context/stubs/unix/pstopdf pstopdf
    ln -sf %{_texmfdistdir}/scripts/context/stubs/unix/texexec texexec
    ln -sf %{_texmfdistdir}/scripts/context/stubs/unix/texmfstart texmfstart
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
rm -fr  %{buildroot}%{_texmfdistdir}/scripts/context/stubs
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/context <<EOF
#
# from context:
cont-en pdftex cont-usr.tex -8bit *cont-en.mkii
cont-en xetex cont-usr.tex -8bit *cont-en.mkii
#! cont-fr pdftex cont-usr.tex -8bit *cont-fr.mkii
#! cont-it pdftex cont-usr.tex -8bit *cont-it.mkii
#! cont-nl pdftex cont-usr.tex -8bit *cont-nl.mkii
#! cont-ro pdftex cont-usr.tex -8bit *cont-ro.mkii
EOF
