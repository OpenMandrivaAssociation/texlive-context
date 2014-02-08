# revision 26863
# category Package
# catalog-ctan /macros/context/current
# catalog-date 2011-08-08 12:26:55 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-context
Version:	20110808
Release:	6
Summary:	The ConTeXt macro package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/current
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context.x86_64-linux.tar.xz
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
%{_texmfdistdir}/bibtex/bst/context/cont-ab.bst
%{_texmfdistdir}/bibtex/bst/context/cont-au.bst
%{_texmfdistdir}/bibtex/bst/context/cont-no.bst
%{_texmfdistdir}/bibtex/bst/context/cont-ti.bst
%{_texmfdistdir}/context/data/scite/lexers/data/scite-context-data-context.lua
%{_texmfdistdir}/context/data/scite/lexers/data/scite-context-data-interfaces.lua
%{_texmfdistdir}/context/data/scite/lexers/data/scite-context-data-metafun.lua
%{_texmfdistdir}/context/data/scite/lexers/data/scite-context-data-metapost.lua
%{_texmfdistdir}/context/data/scite/lexers/data/scite-context-data-tex.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-cld.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-lua-longstring.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-lua.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-mps.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-pdf-object.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-pdf-xref.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-pdf.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-tex.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-txt.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-xml-cdata.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-xml-comment.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer-xml.lua
%{_texmfdistdir}/context/data/scite/lexers/scite-context-lexer.lua
%{_texmfdistdir}/context/data/scite/lexers/themes/scite-context-theme-keep.lua
%{_texmfdistdir}/context/data/scite/lexers/themes/scite-context-theme.lua
%{_texmfdistdir}/context/data/scite/metapost.properties
%{_texmfdistdir}/context/data/scite/scite-context-data-context.properties
%{_texmfdistdir}/context/data/scite/scite-context-data-interfaces.properties
%{_texmfdistdir}/context/data/scite/scite-context-data-metafun.properties
%{_texmfdistdir}/context/data/scite/scite-context-data-metapost.properties
%{_texmfdistdir}/context/data/scite/scite-context-data-tex.properties
%{_texmfdistdir}/context/data/scite/scite-context-external.properties
%{_texmfdistdir}/context/data/scite/scite-context-internal.properties
%{_texmfdistdir}/context/data/scite/scite-context-readme.pdf
%{_texmfdistdir}/context/data/scite/scite-context-readme.tex
%{_texmfdistdir}/context/data/scite/scite-context-user.properties
%{_texmfdistdir}/context/data/scite/scite-context-visual.pdf
%{_texmfdistdir}/context/data/scite/scite-context-visual.png
%{_texmfdistdir}/context/data/scite/scite-context-visual.tex
%{_texmfdistdir}/context/data/scite/scite-context.properties
%{_texmfdistdir}/context/data/scite/scite-ctx-context.properties
%{_texmfdistdir}/context/data/scite/scite-ctx-example.properties
%{_texmfdistdir}/context/data/scite/scite-ctx.lua
%{_texmfdistdir}/context/data/scite/scite-ctx.properties
%{_texmfdistdir}/context/data/scite/scite-metapost.properties
%{_texmfdistdir}/context/data/scite/scite-pragma.properties
%{_texmfdistdir}/context/data/scite/scite-tex.properties
%{_texmfdistdir}/context/data/scite/tex.properties
%{_texmfdistdir}/context/data/texfont/type-buy.dat
%{_texmfdistdir}/context/data/texfont/type-fsf.dat
%{_texmfdistdir}/context/data/texfont/type-ghz.dat
%{_texmfdistdir}/context/data/texfont/type-tmf.dat
%{_texmfdistdir}/context/data/texworks/TUG/TeXworks.ini
%{_texmfdistdir}/context/data/texworks/completion/tw-context.txt
%{_texmfdistdir}/context/data/texworks/configuration/auto-indent-patterns.txt
%{_texmfdistdir}/context/data/texworks/configuration/delimiter-pairs.txt
%{_texmfdistdir}/context/data/texworks/configuration/smart-quotes-modes.txt
%{_texmfdistdir}/context/data/texworks/configuration/syntax-patterns.txt
%{_texmfdistdir}/context/data/texworks/configuration/tag-patterns.txt
%{_texmfdistdir}/context/data/texworks/configuration/texworks-config.txt
%{_texmfdistdir}/context/data/texworks/configuration/tools.ini
%{_texmfdistdir}/context/data/texworks/texworks-context.rme
%{_texmfdistdir}/context/data/texworks/texworks-setup.ini
%{_texmfdistdir}/fonts/afm/hoekwater/context/contnav.afm
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-CNS1-4.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-GB1-4.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-Identity-0.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-Japan1-5.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-Japan1-6.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-Japan2-0.cidmap
%{_texmfdistdir}/fonts/cid/fontforge/Adobe-Korea1-2.cidmap
%{_texmfdistdir}/fonts/enc/dvips/context/cmin.enc
%{_texmfdistdir}/fonts/enc/dvips/context/cmit.enc
%{_texmfdistdir}/fonts/enc/dvips/context/cmitt.enc
%{_texmfdistdir}/fonts/enc/dvips/context/cmrm.enc
%{_texmfdistdir}/fonts/enc/dvips/context/cmsc.enc
%{_texmfdistdir}/fonts/enc/dvips/context/cmtt.enc
%{_texmfdistdir}/fonts/enc/dvips/context/ec-2004.enc
%{_texmfdistdir}/fonts/enc/dvips/context/q-8r.enc
%{_texmfdistdir}/fonts/enc/dvips/context/teff-trinite.enc
%{_texmfdistdir}/fonts/fea/context/greek-babel.fea
%{_texmfdistdir}/fonts/fea/context/test-features.fea
%{_texmfdistdir}/fonts/fea/context/texhistoric.fea
%{_texmfdistdir}/fonts/fea/context/verbose-digits.fea
%{_texmfdistdir}/fonts/map/dvips/context/contnav.map
%{_texmfdistdir}/fonts/map/luatex/context/demo-font.lum
%{_texmfdistdir}/fonts/map/pdftex/context/8r-base.map
%{_texmfdistdir}/fonts/map/pdftex/context/ec-base.map
%{_texmfdistdir}/fonts/map/pdftex/context/ec-os-public-lm.map
%{_texmfdistdir}/fonts/map/pdftex/context/koeieletters.map
%{_texmfdistdir}/fonts/map/pdftex/context/mkiv-base.map
%{_texmfdistdir}/fonts/map/pdftex/context/mkiv-px.map
%{_texmfdistdir}/fonts/map/pdftex/context/mkiv-tx.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-adobe-euro.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-ams-base.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-ams-cmr.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-ams-euler.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-base.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-context-symbol.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-dummy.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-empty.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-micropress-informal.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-public-csr.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-public-lm.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-public-plr.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-public-vnr.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-vogel-symbol.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-wasy.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-youngryu-px.map
%{_texmfdistdir}/fonts/map/pdftex/context/original-youngryu-tx.map
%{_texmfdistdir}/fonts/map/pdftex/context/qx-base.map
%{_texmfdistdir}/fonts/map/pdftex/context/qx-os-public-lm.map
%{_texmfdistdir}/fonts/map/pdftex/context/t5-base.map
%{_texmfdistdir}/fonts/map/pdftex/context/t5-os-public-lm.map
%{_texmfdistdir}/fonts/map/pdftex/context/texnansi-base.map
%{_texmfdistdir}/fonts/map/pdftex/context/texnansi-os-public-lm.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/context/tlig.map
%{_texmfdistdir}/fonts/misc/xetex/fontmapping/context/tlig.tec
%{_texmfdistdir}/fonts/opentype/context/tests/texmfhome.otf
%{_texmfdistdir}/fonts/tfm/hoekwater/context/contnav.tfm
%{_texmfdistdir}/fonts/type1/hoekwater/context/contnav.pfb
%{_texmfdistdir}/metapost/context/base/metafun.mp
%{_texmfdistdir}/metapost/context/base/metafun.mpii
%{_texmfdistdir}/metapost/context/base/metafun.mpiv
%{_texmfdistdir}/metapost/context/base/mp-abck.mpiv
%{_texmfdistdir}/metapost/context/base/mp-apos.mpiv
%{_texmfdistdir}/metapost/context/base/mp-asnc.mpiv
%{_texmfdistdir}/metapost/context/base/mp-back.mp
%{_texmfdistdir}/metapost/context/base/mp-base.mpii
%{_texmfdistdir}/metapost/context/base/mp-base.mpiv
%{_texmfdistdir}/metapost/context/base/mp-butt.mpii
%{_texmfdistdir}/metapost/context/base/mp-butt.mpiv
%{_texmfdistdir}/metapost/context/base/mp-char.mpii
%{_texmfdistdir}/metapost/context/base/mp-char.mpiv
%{_texmfdistdir}/metapost/context/base/mp-chem.mpiv
%{_texmfdistdir}/metapost/context/base/mp-core.mpii
%{_texmfdistdir}/metapost/context/base/mp-core.mpiv
%{_texmfdistdir}/metapost/context/base/mp-crop.mpiv
%{_texmfdistdir}/metapost/context/base/mp-figs.mpii
%{_texmfdistdir}/metapost/context/base/mp-figs.mpiv
%{_texmfdistdir}/metapost/context/base/mp-fobg.mp
%{_texmfdistdir}/metapost/context/base/mp-form.mpii
%{_texmfdistdir}/metapost/context/base/mp-form.mpiv
%{_texmfdistdir}/metapost/context/base/mp-func.mpii
%{_texmfdistdir}/metapost/context/base/mp-func.mpiv
%{_texmfdistdir}/metapost/context/base/mp-grid.mpii
%{_texmfdistdir}/metapost/context/base/mp-grid.mpiv
%{_texmfdistdir}/metapost/context/base/mp-grph.mpii
%{_texmfdistdir}/metapost/context/base/mp-grph.mpiv
%{_texmfdistdir}/metapost/context/base/mp-idea.mpiv
%{_texmfdistdir}/metapost/context/base/mp-mlib.mpiv
%{_texmfdistdir}/metapost/context/base/mp-page.mpii
%{_texmfdistdir}/metapost/context/base/mp-page.mpiv
%{_texmfdistdir}/metapost/context/base/mp-shap.mpii
%{_texmfdistdir}/metapost/context/base/mp-shap.mpiv
%{_texmfdistdir}/metapost/context/base/mp-spec.mpii
%{_texmfdistdir}/metapost/context/base/mp-step.mpii
%{_texmfdistdir}/metapost/context/base/mp-step.mpiv
%{_texmfdistdir}/metapost/context/base/mp-symb.mp
%{_texmfdistdir}/metapost/context/base/mp-text.mpii
%{_texmfdistdir}/metapost/context/base/mp-text.mpiv
%{_texmfdistdir}/metapost/context/base/mp-tool.mpii
%{_texmfdistdir}/metapost/context/base/mp-tool.mpiv
%{_texmfdistdir}/metapost/context/base/mp-txts.mpii
%{_texmfdistdir}/metapost/context/font/punkfont-bold.mp
%{_texmfdistdir}/metapost/context/font/punkfont-boldslanted.mp
%{_texmfdistdir}/metapost/context/font/punkfont-characters.mp
%{_texmfdistdir}/metapost/context/font/punkfont-definitions.mp
%{_texmfdistdir}/metapost/context/font/punkfont-slanted.mp
%{_texmfdistdir}/metapost/context/font/punkfont.mp
%{_texmfdistdir}/scripts/context/lua/mtx-babel.lua
%{_texmfdistdir}/scripts/context/lua/mtx-base.lua
%{_texmfdistdir}/scripts/context/lua/mtx-cache.lua
%{_texmfdistdir}/scripts/context/lua/mtx-chars.lua
%{_texmfdistdir}/scripts/context/lua/mtx-check.lua
%{_texmfdistdir}/scripts/context/lua/mtx-colors.lua
%{_texmfdistdir}/scripts/context/lua/mtx-context.lua
%{_texmfdistdir}/scripts/context/lua/mtx-convert.lua
%{_texmfdistdir}/scripts/context/lua/mtx-epub.lua
%{_texmfdistdir}/scripts/context/lua/mtx-flac.lua
%{_texmfdistdir}/scripts/context/lua/mtx-fonts.lua
%{_texmfdistdir}/scripts/context/lua/mtx-grep.lua
%{_texmfdistdir}/scripts/context/lua/mtx-interface.lua
%{_texmfdistdir}/scripts/context/lua/mtx-metapost.lua
%{_texmfdistdir}/scripts/context/lua/mtx-metatex.lua
%{_texmfdistdir}/scripts/context/lua/mtx-modules.lua
%{_texmfdistdir}/scripts/context/lua/mtx-mtxworks.lua
%{_texmfdistdir}/scripts/context/lua/mtx-package.lua
%{_texmfdistdir}/scripts/context/lua/mtx-patterns.lua
%{_texmfdistdir}/scripts/context/lua/mtx-pdf.lua
%{_texmfdistdir}/scripts/context/lua/mtx-profile.lua
%{_texmfdistdir}/scripts/context/lua/mtx-rsync.lua
%{_texmfdistdir}/scripts/context/lua/mtx-scite.lua
%{_texmfdistdir}/scripts/context/lua/mtx-server-ctx-fonttest.lua
%{_texmfdistdir}/scripts/context/lua/mtx-server-ctx-help.lua
%{_texmfdistdir}/scripts/context/lua/mtx-server-ctx-startup.lua
%{_texmfdistdir}/scripts/context/lua/mtx-server.lua
%{_texmfdistdir}/scripts/context/lua/mtx-texworks.lua
%{_texmfdistdir}/scripts/context/lua/mtx-timing.lua
%{_texmfdistdir}/scripts/context/lua/mtx-tools.lua
%{_texmfdistdir}/scripts/context/lua/mtx-unzip.lua
%{_texmfdistdir}/scripts/context/lua/mtx-update.lua
%{_texmfdistdir}/scripts/context/lua/mtx-watch.lua
%{_texmfdistdir}/scripts/context/lua/mtxrun.lua
%{_texmfdistdir}/scripts/context/perl/makempy.pl
%{_texmfdistdir}/scripts/context/perl/path_tre.pm
%{_texmfdistdir}/scripts/context/perl/pdftrimwhite.pl
%{_texmfdistdir}/scripts/context/perl/texfind.pl
%{_texmfdistdir}/scripts/context/perl/texfont.pl
%{_texmfdistdir}/scripts/context/ruby/base/ctx.rb
%{_texmfdistdir}/scripts/context/ruby/base/exa.rb
%{_texmfdistdir}/scripts/context/ruby/base/file.rb
%{_texmfdistdir}/scripts/context/ruby/base/kpse.rb
%{_texmfdistdir}/scripts/context/ruby/base/kpse/drb.rb
%{_texmfdistdir}/scripts/context/ruby/base/kpse/soap.rb
%{_texmfdistdir}/scripts/context/ruby/base/kpse/trees.rb
%{_texmfdistdir}/scripts/context/ruby/base/kpsedirect.rb
%{_texmfdistdir}/scripts/context/ruby/base/kpsefast.rb
%{_texmfdistdir}/scripts/context/ruby/base/kpseremote.rb
%{_texmfdistdir}/scripts/context/ruby/base/kpserunner.rb
%{_texmfdistdir}/scripts/context/ruby/base/logger.rb
%{_texmfdistdir}/scripts/context/ruby/base/merge.rb
%{_texmfdistdir}/scripts/context/ruby/base/mp.rb
%{_texmfdistdir}/scripts/context/ruby/base/pdf.rb
%{_texmfdistdir}/scripts/context/ruby/base/state.rb
%{_texmfdistdir}/scripts/context/ruby/base/switch.rb
%{_texmfdistdir}/scripts/context/ruby/base/system.rb
%{_texmfdistdir}/scripts/context/ruby/base/tex.rb
%{_texmfdistdir}/scripts/context/ruby/base/texutil.rb
%{_texmfdistdir}/scripts/context/ruby/base/tool.rb
%{_texmfdistdir}/scripts/context/ruby/base/variables.rb
%{_texmfdistdir}/scripts/context/ruby/concheck.rb
%{_texmfdistdir}/scripts/context/ruby/ctxtools.rb
%{_texmfdistdir}/scripts/context/ruby/fcd_start.rb
%{_texmfdistdir}/scripts/context/ruby/graphics/gs.rb
%{_texmfdistdir}/scripts/context/ruby/graphics/inkscape.rb
%{_texmfdistdir}/scripts/context/ruby/graphics/magick.rb
%{_texmfdistdir}/scripts/context/ruby/imgtopdf.rb
%{_texmfdistdir}/scripts/context/ruby/mpstools.rb
%{_texmfdistdir}/scripts/context/ruby/pdftools.rb
%{_texmfdistdir}/scripts/context/ruby/pstopdf.rb
%{_texmfdistdir}/scripts/context/ruby/rlxtools.rb
%{_texmfdistdir}/scripts/context/ruby/rscortool.rb
%{_texmfdistdir}/scripts/context/ruby/rsfiltool.rb
%{_texmfdistdir}/scripts/context/ruby/rslibtool.rb
%{_texmfdistdir}/scripts/context/ruby/runtools.rb
%{_texmfdistdir}/scripts/context/ruby/texexec.rb
%{_texmfdistdir}/scripts/context/ruby/texmfstart.rb
%{_texmfdistdir}/scripts/context/ruby/texsync.rb
%{_texmfdistdir}/scripts/context/ruby/textools.rb
%{_texmfdistdir}/scripts/context/ruby/texutil.rb
%{_texmfdistdir}/scripts/context/ruby/tmftools.rb
%{_texmfdistdir}/scripts/context/ruby/xmltools.rb
%{_texmfdistdir}/scripts/context/stubs/mswin/context.exe
%{_texmfdistdir}/scripts/context/stubs/mswin/luatools.exe
%{_texmfdistdir}/scripts/context/stubs/mswin/metatex.exe
%{_texmfdistdir}/scripts/context/stubs/mswin/mptopdf.exe
%{_texmfdistdir}/scripts/context/stubs/mswin/mtxrun.dll
%{_texmfdistdir}/scripts/context/stubs/mswin/mtxrun.exe
%{_texmfdistdir}/scripts/context/stubs/mswin/mtxrun.lua
%{_texmfdistdir}/scripts/context/stubs/mswin/mtxworks.exe
%{_texmfdistdir}/scripts/context/stubs/mswin/texexec.exe
%{_texmfdistdir}/scripts/context/stubs/mswin/texmfstart.exe
%{_texmfdistdir}/scripts/context/stubs/source/mtxrun_dll.c
%{_texmfdistdir}/scripts/context/stubs/source/mtxrun_exe.c
%{_texmfdistdir}/scripts/context/stubs/source/readme.txt
%{_texmfdistdir}/scripts/context/stubs/unix/context
%{_texmfdistdir}/scripts/context/stubs/unix/luatools
%{_texmfdistdir}/scripts/context/stubs/unix/metatex
%{_texmfdistdir}/scripts/context/stubs/unix/mptopdf
%{_texmfdistdir}/scripts/context/stubs/unix/mtxrun
%{_texmfdistdir}/scripts/context/stubs/unix/mtxworks
%{_texmfdistdir}/scripts/context/stubs/unix/texexec
%{_texmfdistdir}/scripts/context/stubs/unix/texmfstart
%{_texmfdistdir}/tex/context/base/anch-bar.mkii
%{_texmfdistdir}/tex/context/base/anch-bar.mkiv
%{_texmfdistdir}/tex/context/base/anch-bck.mkvi
%{_texmfdistdir}/tex/context/base/anch-pgr.lua
%{_texmfdistdir}/tex/context/base/anch-pgr.mkii
%{_texmfdistdir}/tex/context/base/anch-pgr.mkiv
%{_texmfdistdir}/tex/context/base/anch-pos.lua
%{_texmfdistdir}/tex/context/base/anch-pos.mkii
%{_texmfdistdir}/tex/context/base/anch-pos.mkiv
%{_texmfdistdir}/tex/context/base/anch-snc.mkii
%{_texmfdistdir}/tex/context/base/anch-snc.mkiv
%{_texmfdistdir}/tex/context/base/anch-tab.mkiv
%{_texmfdistdir}/tex/context/base/attr-col.lua
%{_texmfdistdir}/tex/context/base/attr-col.mkiv
%{_texmfdistdir}/tex/context/base/attr-eff.lua
%{_texmfdistdir}/tex/context/base/attr-eff.mkiv
%{_texmfdistdir}/tex/context/base/attr-ini.lua
%{_texmfdistdir}/tex/context/base/attr-ini.mkiv
%{_texmfdistdir}/tex/context/base/attr-lay.lua
%{_texmfdistdir}/tex/context/base/attr-lay.mkiv
%{_texmfdistdir}/tex/context/base/attr-neg.lua
%{_texmfdistdir}/tex/context/base/attr-neg.mkiv
%{_texmfdistdir}/tex/context/base/back-exp.lua
%{_texmfdistdir}/tex/context/base/back-exp.mkiv
%{_texmfdistdir}/tex/context/base/back-ini.lua
%{_texmfdistdir}/tex/context/base/back-ini.mkiv
%{_texmfdistdir}/tex/context/base/back-pdf.lua
%{_texmfdistdir}/tex/context/base/back-pdf.mkiv
%{_texmfdistdir}/tex/context/base/back-swf.mkiv
%{_texmfdistdir}/tex/context/base/back-u3d.mkiv
%{_texmfdistdir}/tex/context/base/bibl-bib.lua
%{_texmfdistdir}/tex/context/base/bibl-bib.mkiv
%{_texmfdistdir}/tex/context/base/bibl-tra.lua
%{_texmfdistdir}/tex/context/base/bibl-tra.mkii
%{_texmfdistdir}/tex/context/base/bibl-tra.mkiv
%{_texmfdistdir}/tex/context/base/bibl-tst.lua
%{_texmfdistdir}/tex/context/base/blob-ini.lua
%{_texmfdistdir}/tex/context/base/blob-ini.mkiv
%{_texmfdistdir}/tex/context/base/buff-imp-default.lua
%{_texmfdistdir}/tex/context/base/buff-imp-default.mkiv
%{_texmfdistdir}/tex/context/base/buff-imp-escaped.lua
%{_texmfdistdir}/tex/context/base/buff-imp-escaped.mkiv
%{_texmfdistdir}/tex/context/base/buff-imp-lua.lua
%{_texmfdistdir}/tex/context/base/buff-imp-lua.mkiv
%{_texmfdistdir}/tex/context/base/buff-imp-mp.lua
%{_texmfdistdir}/tex/context/base/buff-imp-mp.mkiv
%{_texmfdistdir}/tex/context/base/buff-imp-nested.lua
%{_texmfdistdir}/tex/context/base/buff-imp-nested.mkiv
%{_texmfdistdir}/tex/context/base/buff-imp-parsed-xml.lua
%{_texmfdistdir}/tex/context/base/buff-imp-parsed-xml.mkiv
%{_texmfdistdir}/tex/context/base/buff-imp-tex.lua
%{_texmfdistdir}/tex/context/base/buff-imp-tex.mkiv
%{_texmfdistdir}/tex/context/base/buff-imp-xml.lua
%{_texmfdistdir}/tex/context/base/buff-imp-xml.mkiv
%{_texmfdistdir}/tex/context/base/buff-ini.lua
%{_texmfdistdir}/tex/context/base/buff-ini.mkii
%{_texmfdistdir}/tex/context/base/buff-ini.mkiv
%{_texmfdistdir}/tex/context/base/buff-par.lua
%{_texmfdistdir}/tex/context/base/buff-par.mkiv
%{_texmfdistdir}/tex/context/base/buff-ver.lua
%{_texmfdistdir}/tex/context/base/buff-ver.mkii
%{_texmfdistdir}/tex/context/base/buff-ver.mkiv
%{_texmfdistdir}/tex/context/base/bxml-apa.mkiv
%{_texmfdistdir}/tex/context/base/catc-act.mkii
%{_texmfdistdir}/tex/context/base/catc-act.mkiv
%{_texmfdistdir}/tex/context/base/catc-ctx.mkii
%{_texmfdistdir}/tex/context/base/catc-ctx.mkiv
%{_texmfdistdir}/tex/context/base/catc-def.mkii
%{_texmfdistdir}/tex/context/base/catc-def.mkiv
%{_texmfdistdir}/tex/context/base/catc-ini.lua
%{_texmfdistdir}/tex/context/base/catc-ini.mkii
%{_texmfdistdir}/tex/context/base/catc-ini.mkiv
%{_texmfdistdir}/tex/context/base/catc-sym.mkii
%{_texmfdistdir}/tex/context/base/catc-sym.mkiv
%{_texmfdistdir}/tex/context/base/catc-xml.mkii
%{_texmfdistdir}/tex/context/base/catc-xml.mkiv
%{_texmfdistdir}/tex/context/base/char-act.mkiv
%{_texmfdistdir}/tex/context/base/char-cjk.lua
%{_texmfdistdir}/tex/context/base/char-def.lua
%{_texmfdistdir}/tex/context/base/char-enc.lua
%{_texmfdistdir}/tex/context/base/char-enc.mkiv
%{_texmfdistdir}/tex/context/base/char-ent.lua
%{_texmfdistdir}/tex/context/base/char-ini.lua
%{_texmfdistdir}/tex/context/base/char-ini.mkiv
%{_texmfdistdir}/tex/context/base/char-map.lua
%{_texmfdistdir}/tex/context/base/char-tex.lua
%{_texmfdistdir}/tex/context/base/char-utf.lua
%{_texmfdistdir}/tex/context/base/char-utf.mkiv
%{_texmfdistdir}/tex/context/base/chem-ini.lua
%{_texmfdistdir}/tex/context/base/chem-ini.mkiv
%{_texmfdistdir}/tex/context/base/chem-str.lua
%{_texmfdistdir}/tex/context/base/chem-str.mkiv
%{_texmfdistdir}/tex/context/base/cldf-bas.lua
%{_texmfdistdir}/tex/context/base/cldf-bas.mkiv
%{_texmfdistdir}/tex/context/base/cldf-com.lua
%{_texmfdistdir}/tex/context/base/cldf-com.mkiv
%{_texmfdistdir}/tex/context/base/cldf-ini.lua
%{_texmfdistdir}/tex/context/base/cldf-ini.mkiv
%{_texmfdistdir}/tex/context/base/cldf-int.lua
%{_texmfdistdir}/tex/context/base/cldf-int.mkiv
%{_texmfdistdir}/tex/context/base/cldf-ver.lua
%{_texmfdistdir}/tex/context/base/cldf-ver.mkiv
%{_texmfdistdir}/tex/context/base/colo-ema.mkii
%{_texmfdistdir}/tex/context/base/colo-ext.mkii
%{_texmfdistdir}/tex/context/base/colo-ext.mkiv
%{_texmfdistdir}/tex/context/base/colo-grp.mkiv
%{_texmfdistdir}/tex/context/base/colo-hex.mkii
%{_texmfdistdir}/tex/context/base/colo-icc.lua
%{_texmfdistdir}/tex/context/base/colo-imp-dem.mkiv
%{_texmfdistdir}/tex/context/base/colo-imp-ema.mkiv
%{_texmfdistdir}/tex/context/base/colo-imp-rgb.mkiv
%{_texmfdistdir}/tex/context/base/colo-imp-x11.mkiv
%{_texmfdistdir}/tex/context/base/colo-imp-xwi.mkiv
%{_texmfdistdir}/tex/context/base/colo-ini.lua
%{_texmfdistdir}/tex/context/base/colo-ini.mkii
%{_texmfdistdir}/tex/context/base/colo-ini.mkiv
%{_texmfdistdir}/tex/context/base/colo-rgb.mkii
%{_texmfdistdir}/tex/context/base/colo-run.lua
%{_texmfdistdir}/tex/context/base/colo-run.mkii
%{_texmfdistdir}/tex/context/base/colo-run.mkiv
%{_texmfdistdir}/tex/context/base/colo-x11.mkii
%{_texmfdistdir}/tex/context/base/colo-xwi.mkii
%{_texmfdistdir}/tex/context/base/cont-cs.mkii
%{_texmfdistdir}/tex/context/base/cont-cs.mkiv
%{_texmfdistdir}/tex/context/base/cont-de.mkii
%{_texmfdistdir}/tex/context/base/cont-de.mkiv
%{_texmfdistdir}/tex/context/base/cont-en.mkii
%{_texmfdistdir}/tex/context/base/cont-en.mkiv
%{_texmfdistdir}/tex/context/base/cont-err.mkii
%{_texmfdistdir}/tex/context/base/cont-fil.mkii
%{_texmfdistdir}/tex/context/base/cont-fil.mkiv
%{_texmfdistdir}/tex/context/base/cont-fr.mkii
%{_texmfdistdir}/tex/context/base/cont-fr.mkiv
%{_texmfdistdir}/tex/context/base/cont-gb.mkii
%{_texmfdistdir}/tex/context/base/cont-gb.mkiv
%{_texmfdistdir}/tex/context/base/cont-it.mkii
%{_texmfdistdir}/tex/context/base/cont-it.mkiv
%{_texmfdistdir}/tex/context/base/cont-log.mkii
%{_texmfdistdir}/tex/context/base/cont-log.mkiv
%{_texmfdistdir}/tex/context/base/cont-new.mkii
%{_texmfdistdir}/tex/context/base/cont-new.mkiv
%{_texmfdistdir}/tex/context/base/cont-nl.mkii
%{_texmfdistdir}/tex/context/base/cont-nl.mkiv
%{_texmfdistdir}/tex/context/base/cont-pe.mkiv
%{_texmfdistdir}/tex/context/base/cont-ro.mkii
%{_texmfdistdir}/tex/context/base/cont-ro.mkiv
%{_texmfdistdir}/tex/context/base/cont-sys.ori
%{_texmfdistdir}/tex/context/base/context-base.lmx
%{_texmfdistdir}/tex/context/base/context-characters.lmx
%{_texmfdistdir}/tex/context/base/context-debug.lmx
%{_texmfdistdir}/tex/context/base/context-error.lmx
%{_texmfdistdir}/tex/context/base/context-fonttest.lmx
%{_texmfdistdir}/tex/context/base/context-help.lmx
%{_texmfdistdir}/tex/context/base/context-timing.lmx
%{_texmfdistdir}/tex/context/base/context-version.pdf
%{_texmfdistdir}/tex/context/base/context-version.png
%{_texmfdistdir}/tex/context/base/context.css
%{_texmfdistdir}/tex/context/base/context.lus
%{_texmfdistdir}/tex/context/base/context.mkii
%{_texmfdistdir}/tex/context/base/context.mkiv
%{_texmfdistdir}/tex/context/base/context.rme
%{_texmfdistdir}/tex/context/base/context.todo
%{_texmfdistdir}/tex/context/base/core-con.lua
%{_texmfdistdir}/tex/context/base/core-con.mkii
%{_texmfdistdir}/tex/context/base/core-con.mkiv
%{_texmfdistdir}/tex/context/base/core-ctx.lua
%{_texmfdistdir}/tex/context/base/core-ctx.mkii
%{_texmfdistdir}/tex/context/base/core-ctx.mkiv
%{_texmfdistdir}/tex/context/base/core-dat.lua
%{_texmfdistdir}/tex/context/base/core-dat.mkiv
%{_texmfdistdir}/tex/context/base/core-def.mkii
%{_texmfdistdir}/tex/context/base/core-def.mkiv
%{_texmfdistdir}/tex/context/base/core-env.lua
%{_texmfdistdir}/tex/context/base/core-env.mkii
%{_texmfdistdir}/tex/context/base/core-env.mkiv
%{_texmfdistdir}/tex/context/base/core-fil.mkii
%{_texmfdistdir}/tex/context/base/core-fnt.mkii
%{_texmfdistdir}/tex/context/base/core-fnt.mkiv
%{_texmfdistdir}/tex/context/base/core-gen.mkii
%{_texmfdistdir}/tex/context/base/core-ini.mkii
%{_texmfdistdir}/tex/context/base/core-ini.mkiv
%{_texmfdistdir}/tex/context/base/core-job.mkii
%{_texmfdistdir}/tex/context/base/core-mis.mkii
%{_texmfdistdir}/tex/context/base/core-mis.mkiv
%{_texmfdistdir}/tex/context/base/core-par.mkii
%{_texmfdistdir}/tex/context/base/core-stg.mkii
%{_texmfdistdir}/tex/context/base/core-sys.lua
%{_texmfdistdir}/tex/context/base/core-sys.mkii
%{_texmfdistdir}/tex/context/base/core-sys.mkiv
%{_texmfdistdir}/tex/context/base/core-two.lua
%{_texmfdistdir}/tex/context/base/core-two.mkii
%{_texmfdistdir}/tex/context/base/core-two.mkiv
%{_texmfdistdir}/tex/context/base/core-uti.lua
%{_texmfdistdir}/tex/context/base/core-uti.mkii
%{_texmfdistdir}/tex/context/base/core-uti.mkiv
%{_texmfdistdir}/tex/context/base/core-var.mkii
%{_texmfdistdir}/tex/context/base/core-var.mkiv
%{_texmfdistdir}/tex/context/base/data-aux.lua
%{_texmfdistdir}/tex/context/base/data-bin.lua
%{_texmfdistdir}/tex/context/base/data-con.lua
%{_texmfdistdir}/tex/context/base/data-crl.lua
%{_texmfdistdir}/tex/context/base/data-ctx.lua
%{_texmfdistdir}/tex/context/base/data-env.lua
%{_texmfdistdir}/tex/context/base/data-exp.lua
%{_texmfdistdir}/tex/context/base/data-fil.lua
%{_texmfdistdir}/tex/context/base/data-gen.lua
%{_texmfdistdir}/tex/context/base/data-ini.lua
%{_texmfdistdir}/tex/context/base/data-inp.lua
%{_texmfdistdir}/tex/context/base/data-lst.lua
%{_texmfdistdir}/tex/context/base/data-lua.lua
%{_texmfdistdir}/tex/context/base/data-met.lua
%{_texmfdistdir}/tex/context/base/data-out.lua
%{_texmfdistdir}/tex/context/base/data-pre.lua
%{_texmfdistdir}/tex/context/base/data-res.lua
%{_texmfdistdir}/tex/context/base/data-sch.lua
%{_texmfdistdir}/tex/context/base/data-tex.lua
%{_texmfdistdir}/tex/context/base/data-tmf.lua
%{_texmfdistdir}/tex/context/base/data-tmp.lua
%{_texmfdistdir}/tex/context/base/data-tre.lua
%{_texmfdistdir}/tex/context/base/data-use.lua
%{_texmfdistdir}/tex/context/base/data-vir.lua
%{_texmfdistdir}/tex/context/base/data-zip.lua
%{_texmfdistdir}/tex/context/base/enco-032.mkii
%{_texmfdistdir}/tex/context/base/enco-037.mkii
%{_texmfdistdir}/tex/context/base/enco-acc.mkii
%{_texmfdistdir}/tex/context/base/enco-agr.mkii
%{_texmfdistdir}/tex/context/base/enco-ans.mkii
%{_texmfdistdir}/tex/context/base/enco-cas.mkii
%{_texmfdistdir}/tex/context/base/enco-chi.mkii
%{_texmfdistdir}/tex/context/base/enco-com.mkii
%{_texmfdistdir}/tex/context/base/enco-cyr.mkii
%{_texmfdistdir}/tex/context/base/enco-def.mkii
%{_texmfdistdir}/tex/context/base/enco-ec.mkii
%{_texmfdistdir}/tex/context/base/enco-ecm.mkii
%{_texmfdistdir}/tex/context/base/enco-el.mkii
%{_texmfdistdir}/tex/context/base/enco-fde.mkii
%{_texmfdistdir}/tex/context/base/enco-ffr.mkii
%{_texmfdistdir}/tex/context/base/enco-fpl.mkii
%{_texmfdistdir}/tex/context/base/enco-fro.mkii
%{_texmfdistdir}/tex/context/base/enco-fsl.mkii
%{_texmfdistdir}/tex/context/base/enco-grk.mkii
%{_texmfdistdir}/tex/context/base/enco-heb.mkii
%{_texmfdistdir}/tex/context/base/enco-ibm.mkii
%{_texmfdistdir}/tex/context/base/enco-il2.mkii
%{_texmfdistdir}/tex/context/base/enco-ini.mkii
%{_texmfdistdir}/tex/context/base/enco-ini.mkiv
%{_texmfdistdir}/tex/context/base/enco-l7x.mkii
%{_texmfdistdir}/tex/context/base/enco-lat.mkii
%{_texmfdistdir}/tex/context/base/enco-mis.mkii
%{_texmfdistdir}/tex/context/base/enco-pdf.mkii
%{_texmfdistdir}/tex/context/base/enco-pfr.mkii
%{_texmfdistdir}/tex/context/base/enco-pol.mkii
%{_texmfdistdir}/tex/context/base/enco-qx.mkii
%{_texmfdistdir}/tex/context/base/enco-raw.mkii
%{_texmfdistdir}/tex/context/base/enco-run.mkii
%{_texmfdistdir}/tex/context/base/enco-t5.mkii
%{_texmfdistdir}/tex/context/base/enco-tbo.mkii
%{_texmfdistdir}/tex/context/base/enco-uc.mkii
%{_texmfdistdir}/tex/context/base/enco-vis.mkii
%{_texmfdistdir}/tex/context/base/enco-vna.mkii
%{_texmfdistdir}/tex/context/base/enco-win.mkii
%{_texmfdistdir}/tex/context/base/enco-x5.mkii
%{_texmfdistdir}/tex/context/base/export-example.css
%{_texmfdistdir}/tex/context/base/export-example.rng
%{_texmfdistdir}/tex/context/base/export-example.tex
%{_texmfdistdir}/tex/context/base/file-ini.lua
%{_texmfdistdir}/tex/context/base/file-ini.mkvi
%{_texmfdistdir}/tex/context/base/file-job.lua
%{_texmfdistdir}/tex/context/base/file-job.mkvi
%{_texmfdistdir}/tex/context/base/file-lib.lua
%{_texmfdistdir}/tex/context/base/file-lib.mkvi
%{_texmfdistdir}/tex/context/base/file-mod.lua
%{_texmfdistdir}/tex/context/base/file-mod.mkvi
%{_texmfdistdir}/tex/context/base/file-res.lua
%{_texmfdistdir}/tex/context/base/file-res.mkvi
%{_texmfdistdir}/tex/context/base/file-syn.lua
%{_texmfdistdir}/tex/context/base/file-syn.mkvi
%{_texmfdistdir}/tex/context/base/filt-bas.mkii
%{_texmfdistdir}/tex/context/base/filt-ini.mkii
%{_texmfdistdir}/tex/context/base/font-afm.lua
%{_texmfdistdir}/tex/context/base/font-age.lua
%{_texmfdistdir}/tex/context/base/font-agl.lua
%{_texmfdistdir}/tex/context/base/font-arb.mkii
%{_texmfdistdir}/tex/context/base/font-aux.lua
%{_texmfdistdir}/tex/context/base/font-bfm.mkii
%{_texmfdistdir}/tex/context/base/font-chi.mkii
%{_texmfdistdir}/tex/context/base/font-chk.lua
%{_texmfdistdir}/tex/context/base/font-cid.lua
%{_texmfdistdir}/tex/context/base/font-col.lua
%{_texmfdistdir}/tex/context/base/font-col.mkvi
%{_texmfdistdir}/tex/context/base/font-con.lua
%{_texmfdistdir}/tex/context/base/font-ctx.lua
%{_texmfdistdir}/tex/context/base/font-def.lua
%{_texmfdistdir}/tex/context/base/font-emp.mkvi
%{_texmfdistdir}/tex/context/base/font-enc.lua
%{_texmfdistdir}/tex/context/base/font-enh.lua
%{_texmfdistdir}/tex/context/base/font-ext.lua
%{_texmfdistdir}/tex/context/base/font-fbk.lua
%{_texmfdistdir}/tex/context/base/font-fea.mkvi
%{_texmfdistdir}/tex/context/base/font-fil.mkvi
%{_texmfdistdir}/tex/context/base/font-gds.lua
%{_texmfdistdir}/tex/context/base/font-gds.mkiv
%{_texmfdistdir}/tex/context/base/font-heb.mkii
%{_texmfdistdir}/tex/context/base/font-ini.lua
%{_texmfdistdir}/tex/context/base/font-ini.mkii
%{_texmfdistdir}/tex/context/base/font-ini.mkvi
%{_texmfdistdir}/tex/context/base/font-jap.mkii
%{_texmfdistdir}/tex/context/base/font-ldr.lua
%{_texmfdistdir}/tex/context/base/font-lib.mkvi
%{_texmfdistdir}/tex/context/base/font-log.lua
%{_texmfdistdir}/tex/context/base/font-lua.lua
%{_texmfdistdir}/tex/context/base/font-map.lua
%{_texmfdistdir}/tex/context/base/font-mat.mkvi
%{_texmfdistdir}/tex/context/base/font-mis.lua
%{_texmfdistdir}/tex/context/base/font-ota.lua
%{_texmfdistdir}/tex/context/base/font-otb.lua
%{_texmfdistdir}/tex/context/base/font-otc.lua
%{_texmfdistdir}/tex/context/base/font-otd.lua
%{_texmfdistdir}/tex/context/base/font-otf.lua
%{_texmfdistdir}/tex/context/base/font-oth.lua
%{_texmfdistdir}/tex/context/base/font-oti.lua
%{_texmfdistdir}/tex/context/base/font-otn.lua
%{_texmfdistdir}/tex/context/base/font-otp.lua
%{_texmfdistdir}/tex/context/base/font-ott.lua
%{_texmfdistdir}/tex/context/base/font-pat.lua
%{_texmfdistdir}/tex/context/base/font-pre.mkiv
%{_texmfdistdir}/tex/context/base/font-run.mkii
%{_texmfdistdir}/tex/context/base/font-run.mkiv
%{_texmfdistdir}/tex/context/base/font-set.mkvi
%{_texmfdistdir}/tex/context/base/font-sty.mkvi
%{_texmfdistdir}/tex/context/base/font-sym.mkvi
%{_texmfdistdir}/tex/context/base/font-syn.lua
%{_texmfdistdir}/tex/context/base/font-tfm.lua
%{_texmfdistdir}/tex/context/base/font-tra.mkiv
%{_texmfdistdir}/tex/context/base/font-uni.mkii
%{_texmfdistdir}/tex/context/base/font-uni.mkiv
%{_texmfdistdir}/tex/context/base/font-unk.mkii
%{_texmfdistdir}/tex/context/base/font-unk.mkiv
%{_texmfdistdir}/tex/context/base/font-var.mkvi
%{_texmfdistdir}/tex/context/base/font-vf.lua
%{_texmfdistdir}/tex/context/base/font-xtx.mkii
%{_texmfdistdir}/tex/context/base/grph-epd.lua
%{_texmfdistdir}/tex/context/base/grph-epd.mkiv
%{_texmfdistdir}/tex/context/base/grph-fig.mkii
%{_texmfdistdir}/tex/context/base/grph-fig.mkiv
%{_texmfdistdir}/tex/context/base/grph-fil.lua
%{_texmfdistdir}/tex/context/base/grph-inc.lua
%{_texmfdistdir}/tex/context/base/grph-inc.mkii
%{_texmfdistdir}/tex/context/base/grph-inc.mkiv
%{_texmfdistdir}/tex/context/base/grph-raw.lua
%{_texmfdistdir}/tex/context/base/grph-raw.mkiv
%{_texmfdistdir}/tex/context/base/grph-swf.lua
%{_texmfdistdir}/tex/context/base/grph-trf.mkii
%{_texmfdistdir}/tex/context/base/grph-trf.mkiv
%{_texmfdistdir}/tex/context/base/grph-u3d.lua
%{_texmfdistdir}/tex/context/base/grph-wnd.lua
%{_texmfdistdir}/tex/context/base/hand-def.mkii
%{_texmfdistdir}/tex/context/base/hand-ini.mkii
%{_texmfdistdir}/tex/context/base/hand-ini.mkiv
%{_texmfdistdir}/tex/context/base/java-ans.mkii
%{_texmfdistdir}/tex/context/base/java-exa.mkii
%{_texmfdistdir}/tex/context/base/java-fil.mkii
%{_texmfdistdir}/tex/context/base/java-fld.mkii
%{_texmfdistdir}/tex/context/base/java-imp-exa.mkiv
%{_texmfdistdir}/tex/context/base/java-imp-fil.mkiv
%{_texmfdistdir}/tex/context/base/java-imp-fld.mkiv
%{_texmfdistdir}/tex/context/base/java-imp-rhh.mkiv
%{_texmfdistdir}/tex/context/base/java-imp-stp.mkiv
%{_texmfdistdir}/tex/context/base/java-ini.lua
%{_texmfdistdir}/tex/context/base/java-ini.mkii
%{_texmfdistdir}/tex/context/base/java-ini.mkiv
%{_texmfdistdir}/tex/context/base/java-stp.mkii
%{_texmfdistdir}/tex/context/base/l-boolean.lua
%{_texmfdistdir}/tex/context/base/l-dir.lua
%{_texmfdistdir}/tex/context/base/l-file.lua
%{_texmfdistdir}/tex/context/base/l-io.lua
%{_texmfdistdir}/tex/context/base/l-lpeg.lua
%{_texmfdistdir}/tex/context/base/l-math.lua
%{_texmfdistdir}/tex/context/base/l-md5.lua
%{_texmfdistdir}/tex/context/base/l-number.lua
%{_texmfdistdir}/tex/context/base/l-os.lua
%{_texmfdistdir}/tex/context/base/l-pdfview.lua
%{_texmfdistdir}/tex/context/base/l-set.lua
%{_texmfdistdir}/tex/context/base/l-string.lua
%{_texmfdistdir}/tex/context/base/l-table.lua
%{_texmfdistdir}/tex/context/base/l-unicode.lua
%{_texmfdistdir}/tex/context/base/l-url.lua
%{_texmfdistdir}/tex/context/base/l-xml.lua
%{_texmfdistdir}/tex/context/base/lang-all.xml
%{_texmfdistdir}/tex/context/base/lang-alt.mkii
%{_texmfdistdir}/tex/context/base/lang-ana.mkii
%{_texmfdistdir}/tex/context/base/lang-art.mkii
%{_texmfdistdir}/tex/context/base/lang-bal.mkii
%{_texmfdistdir}/tex/context/base/lang-cel.mkii
%{_texmfdistdir}/tex/context/base/lang-chi.mkii
%{_texmfdistdir}/tex/context/base/lang-ctx.mkii
%{_texmfdistdir}/tex/context/base/lang-cyr.mkii
%{_texmfdistdir}/tex/context/base/lang-def.lua
%{_texmfdistdir}/tex/context/base/lang-def.mkiv
%{_texmfdistdir}/tex/context/base/lang-dis.mkii
%{_texmfdistdir}/tex/context/base/lang-frd.mkii
%{_texmfdistdir}/tex/context/base/lang-frq.mkii
%{_texmfdistdir}/tex/context/base/lang-ger.mkii
%{_texmfdistdir}/tex/context/base/lang-grk.mkii
%{_texmfdistdir}/tex/context/base/lang-ind.mkii
%{_texmfdistdir}/tex/context/base/lang-ini.lua
%{_texmfdistdir}/tex/context/base/lang-ini.mkii
%{_texmfdistdir}/tex/context/base/lang-ini.mkiv
%{_texmfdistdir}/tex/context/base/lang-ita.mkii
%{_texmfdistdir}/tex/context/base/lang-jap.mkii
%{_texmfdistdir}/tex/context/base/lang-lab.lua
%{_texmfdistdir}/tex/context/base/lang-lab.mkii
%{_texmfdistdir}/tex/context/base/lang-lab.mkiv
%{_texmfdistdir}/tex/context/base/lang-mis.mkii
%{_texmfdistdir}/tex/context/base/lang-mis.mkiv
%{_texmfdistdir}/tex/context/base/lang-run.mkii
%{_texmfdistdir}/tex/context/base/lang-sla.mkii
%{_texmfdistdir}/tex/context/base/lang-spa.mkii
%{_texmfdistdir}/tex/context/base/lang-spa.mkiv
%{_texmfdistdir}/tex/context/base/lang-spe.mkii
%{_texmfdistdir}/tex/context/base/lang-txt.lua
%{_texmfdistdir}/tex/context/base/lang-ura.mkii
%{_texmfdistdir}/tex/context/base/lang-url.lua
%{_texmfdistdir}/tex/context/base/lang-url.mkii
%{_texmfdistdir}/tex/context/base/lang-url.mkiv
%{_texmfdistdir}/tex/context/base/lang-vn.mkii
%{_texmfdistdir}/tex/context/base/lang-wrd.lua
%{_texmfdistdir}/tex/context/base/lang-wrd.mkiv
%{_texmfdistdir}/tex/context/base/layo-ini.lua
%{_texmfdistdir}/tex/context/base/layo-ini.mkiv
%{_texmfdistdir}/tex/context/base/lpdf-ano.lua
%{_texmfdistdir}/tex/context/base/lpdf-col.lua
%{_texmfdistdir}/tex/context/base/lpdf-enc.lua
%{_texmfdistdir}/tex/context/base/lpdf-epa.lua
%{_texmfdistdir}/tex/context/base/lpdf-epd.lua
%{_texmfdistdir}/tex/context/base/lpdf-fld.lua
%{_texmfdistdir}/tex/context/base/lpdf-fmt.lua
%{_texmfdistdir}/tex/context/base/lpdf-grp.lua
%{_texmfdistdir}/tex/context/base/lpdf-ini.lua
%{_texmfdistdir}/tex/context/base/lpdf-mis.lua
%{_texmfdistdir}/tex/context/base/lpdf-mov.lua
%{_texmfdistdir}/tex/context/base/lpdf-nod.lua
%{_texmfdistdir}/tex/context/base/lpdf-pda.xml
%{_texmfdistdir}/tex/context/base/lpdf-pdx.xml
%{_texmfdistdir}/tex/context/base/lpdf-ren.lua
%{_texmfdistdir}/tex/context/base/lpdf-swf.lua
%{_texmfdistdir}/tex/context/base/lpdf-tag.lua
%{_texmfdistdir}/tex/context/base/lpdf-u3d.lua
%{_texmfdistdir}/tex/context/base/lpdf-wid.lua
%{_texmfdistdir}/tex/context/base/lpdf-xmp.lua
%{_texmfdistdir}/tex/context/base/luat-bas.mkiv
%{_texmfdistdir}/tex/context/base/luat-bwc.lua
%{_texmfdistdir}/tex/context/base/luat-cbk.lua
%{_texmfdistdir}/tex/context/base/luat-cnf.lua
%{_texmfdistdir}/tex/context/base/luat-cod.lua
%{_texmfdistdir}/tex/context/base/luat-cod.mkiv
%{_texmfdistdir}/tex/context/base/luat-env.lua
%{_texmfdistdir}/tex/context/base/luat-exe.lua
%{_texmfdistdir}/tex/context/base/luat-fio.lua
%{_texmfdistdir}/tex/context/base/luat-fmt.lua
%{_texmfdistdir}/tex/context/base/luat-ini.lua
%{_texmfdistdir}/tex/context/base/luat-ini.mkiv
%{_texmfdistdir}/tex/context/base/luat-iop.lua
%{_texmfdistdir}/tex/context/base/luat-lib.mkiv
%{_texmfdistdir}/tex/context/base/luat-lua.lua
%{_texmfdistdir}/tex/context/base/luat-mac.lua
%{_texmfdistdir}/tex/context/base/luat-run.lua
%{_texmfdistdir}/tex/context/base/luat-soc.lua
%{_texmfdistdir}/tex/context/base/luat-sta.lua
%{_texmfdistdir}/tex/context/base/luat-sto.lua
%{_texmfdistdir}/tex/context/base/lxml-aux.lua
%{_texmfdistdir}/tex/context/base/lxml-css.lua
%{_texmfdistdir}/tex/context/base/lxml-css.mkiv
%{_texmfdistdir}/tex/context/base/lxml-ctx.lua
%{_texmfdistdir}/tex/context/base/lxml-ctx.mkiv
%{_texmfdistdir}/tex/context/base/lxml-dir.lua
%{_texmfdistdir}/tex/context/base/lxml-ent.lua
%{_texmfdistdir}/tex/context/base/lxml-inf.lua
%{_texmfdistdir}/tex/context/base/lxml-ini.mkiv
%{_texmfdistdir}/tex/context/base/lxml-lpt.lua
%{_texmfdistdir}/tex/context/base/lxml-mis.lua
%{_texmfdistdir}/tex/context/base/lxml-sor.lua
%{_texmfdistdir}/tex/context/base/lxml-sor.mkiv
%{_texmfdistdir}/tex/context/base/lxml-tab.lua
%{_texmfdistdir}/tex/context/base/lxml-tex.lua
%{_texmfdistdir}/tex/context/base/lxml-xml.lua
%{_texmfdistdir}/tex/context/base/m-arabtex.mkii
%{_texmfdistdir}/tex/context/base/m-barcodes.mkiv
%{_texmfdistdir}/tex/context/base/m-chart.lua
%{_texmfdistdir}/tex/context/base/m-chart.mkii
%{_texmfdistdir}/tex/context/base/m-chart.mkvi
%{_texmfdistdir}/tex/context/base/m-chemic.mkii
%{_texmfdistdir}/tex/context/base/m-chemic.mkiv
%{_texmfdistdir}/tex/context/base/m-cweb.tex
%{_texmfdistdir}/tex/context/base/m-database.lua
%{_texmfdistdir}/tex/context/base/m-database.mkii
%{_texmfdistdir}/tex/context/base/m-database.mkiv
%{_texmfdistdir}/tex/context/base/m-datastrc.tex
%{_texmfdistdir}/tex/context/base/m-directives.mkiv
%{_texmfdistdir}/tex/context/base/m-dratex.mkii
%{_texmfdistdir}/tex/context/base/m-edtsnc.mkii
%{_texmfdistdir}/tex/context/base/m-educat.tex
%{_texmfdistdir}/tex/context/base/m-fields.mkiv
%{_texmfdistdir}/tex/context/base/m-format.tex
%{_texmfdistdir}/tex/context/base/m-graph.mkii
%{_texmfdistdir}/tex/context/base/m-graph.mkiv
%{_texmfdistdir}/tex/context/base/m-layout.tex
%{_texmfdistdir}/tex/context/base/m-level.mkii
%{_texmfdistdir}/tex/context/base/m-logcategories.mkiv
%{_texmfdistdir}/tex/context/base/m-markdown.lua
%{_texmfdistdir}/tex/context/base/m-markdown.mkiv
%{_texmfdistdir}/tex/context/base/m-mathcrap.mkiv
%{_texmfdistdir}/tex/context/base/m-mkii.mkiv
%{_texmfdistdir}/tex/context/base/m-mkivhacks.mkiv
%{_texmfdistdir}/tex/context/base/m-morse.mkvi
%{_texmfdistdir}/tex/context/base/m-narrowtt.tex
%{_texmfdistdir}/tex/context/base/m-newmat.tex
%{_texmfdistdir}/tex/context/base/m-ntb-to-xtb.mkiv
%{_texmfdistdir}/tex/context/base/m-obsolete.mkii
%{_texmfdistdir}/tex/context/base/m-obsolete.mkiv
%{_texmfdistdir}/tex/context/base/m-pdfsnc.mkii
%{_texmfdistdir}/tex/context/base/m-pictex.tex
%{_texmfdistdir}/tex/context/base/m-pstricks.lua
%{_texmfdistdir}/tex/context/base/m-pstricks.mkii
%{_texmfdistdir}/tex/context/base/m-pstricks.mkiv
%{_texmfdistdir}/tex/context/base/m-punk.mkiv
%{_texmfdistdir}/tex/context/base/m-r.tex
%{_texmfdistdir}/tex/context/base/m-spreadsheet.mkiv
%{_texmfdistdir}/tex/context/base/m-steps.lua
%{_texmfdistdir}/tex/context/base/m-steps.mkii
%{_texmfdistdir}/tex/context/base/m-steps.mkvi
%{_texmfdistdir}/tex/context/base/m-streams.tex
%{_texmfdistdir}/tex/context/base/m-subsub.tex
%{_texmfdistdir}/tex/context/base/m-tex4ht.mkii
%{_texmfdistdir}/tex/context/base/m-timing.mkiv
%{_texmfdistdir}/tex/context/base/m-trackers.mkiv
%{_texmfdistdir}/tex/context/base/m-translate.mkiv
%{_texmfdistdir}/tex/context/base/m-units.mkii
%{_texmfdistdir}/tex/context/base/m-units.mkiv
%{_texmfdistdir}/tex/context/base/m-visual.mkii
%{_texmfdistdir}/tex/context/base/m-visual.mkiv
%{_texmfdistdir}/tex/context/base/m-zint.mkiv
%{_texmfdistdir}/tex/context/base/math-act.lua
%{_texmfdistdir}/tex/context/base/math-ali.mkiv
%{_texmfdistdir}/tex/context/base/math-ams.mkii
%{_texmfdistdir}/tex/context/base/math-arr.mkii
%{_texmfdistdir}/tex/context/base/math-arr.mkiv
%{_texmfdistdir}/tex/context/base/math-cow.mkii
%{_texmfdistdir}/tex/context/base/math-def.mkiv
%{_texmfdistdir}/tex/context/base/math-del.mkiv
%{_texmfdistdir}/tex/context/base/math-dim.lua
%{_texmfdistdir}/tex/context/base/math-dis.mkiv
%{_texmfdistdir}/tex/context/base/math-eul.mkii
%{_texmfdistdir}/tex/context/base/math-ext.lua
%{_texmfdistdir}/tex/context/base/math-for.mkiv
%{_texmfdistdir}/tex/context/base/math-fou.mkii
%{_texmfdistdir}/tex/context/base/math-frc.mkii
%{_texmfdistdir}/tex/context/base/math-frc.mkiv
%{_texmfdistdir}/tex/context/base/math-ini.lua
%{_texmfdistdir}/tex/context/base/math-ini.mkii
%{_texmfdistdir}/tex/context/base/math-ini.mkiv
%{_texmfdistdir}/tex/context/base/math-inl.mkiv
%{_texmfdistdir}/tex/context/base/math-int.mkiv
%{_texmfdistdir}/tex/context/base/math-lbr.mkii
%{_texmfdistdir}/tex/context/base/math-map.lua
%{_texmfdistdir}/tex/context/base/math-noa.lua
%{_texmfdistdir}/tex/context/base/math-pln.mkii
%{_texmfdistdir}/tex/context/base/math-pln.mkiv
%{_texmfdistdir}/tex/context/base/math-ren.lua
%{_texmfdistdir}/tex/context/base/math-run.mkii
%{_texmfdistdir}/tex/context/base/math-scr.mkiv
%{_texmfdistdir}/tex/context/base/math-tag.lua
%{_texmfdistdir}/tex/context/base/math-tex.mkii
%{_texmfdistdir}/tex/context/base/math-tim.mkii
%{_texmfdistdir}/tex/context/base/math-uni.mkii
%{_texmfdistdir}/tex/context/base/math-vfu.lua
%{_texmfdistdir}/tex/context/base/meta-clp.mkii
%{_texmfdistdir}/tex/context/base/meta-dum.mkii
%{_texmfdistdir}/tex/context/base/meta-fig.mkii
%{_texmfdistdir}/tex/context/base/meta-fig.mkiv
%{_texmfdistdir}/tex/context/base/meta-fun.lua
%{_texmfdistdir}/tex/context/base/meta-fun.mkiv
%{_texmfdistdir}/tex/context/base/meta-imp-clp.mkiv
%{_texmfdistdir}/tex/context/base/meta-imp-dum.mkiv
%{_texmfdistdir}/tex/context/base/meta-imp-fen.mkiv
%{_texmfdistdir}/tex/context/base/meta-imp-mis.mkiv
%{_texmfdistdir}/tex/context/base/meta-imp-nav.mkiv
%{_texmfdistdir}/tex/context/base/meta-imp-pre.mkiv
%{_texmfdistdir}/tex/context/base/meta-imp-txt.mkiv
%{_texmfdistdir}/tex/context/base/meta-ini.lua
%{_texmfdistdir}/tex/context/base/meta-ini.mkii
%{_texmfdistdir}/tex/context/base/meta-ini.mkiv
%{_texmfdistdir}/tex/context/base/meta-mis.mkii
%{_texmfdistdir}/tex/context/base/meta-nav.mkii
%{_texmfdistdir}/tex/context/base/meta-pag.mkii
%{_texmfdistdir}/tex/context/base/meta-pag.mkiv
%{_texmfdistdir}/tex/context/base/meta-pdf.lua
%{_texmfdistdir}/tex/context/base/meta-pdf.mkii
%{_texmfdistdir}/tex/context/base/meta-pdf.mkiv
%{_texmfdistdir}/tex/context/base/meta-pdh.lua
%{_texmfdistdir}/tex/context/base/meta-pdh.mkiv
%{_texmfdistdir}/tex/context/base/meta-pre.mkii
%{_texmfdistdir}/tex/context/base/meta-tex.lua
%{_texmfdistdir}/tex/context/base/meta-tex.mkii
%{_texmfdistdir}/tex/context/base/meta-tex.mkiv
%{_texmfdistdir}/tex/context/base/meta-txt.mkii
%{_texmfdistdir}/tex/context/base/meta-xml.mkii
%{_texmfdistdir}/tex/context/base/meta-xml.mkiv
%{_texmfdistdir}/tex/context/base/metatex.lus
%{_texmfdistdir}/tex/context/base/metatex.tex
%{_texmfdistdir}/tex/context/base/mlib-ctx.lua
%{_texmfdistdir}/tex/context/base/mlib-ctx.mkiv
%{_texmfdistdir}/tex/context/base/mlib-pdf.lua
%{_texmfdistdir}/tex/context/base/mlib-pdf.mkiv
%{_texmfdistdir}/tex/context/base/mlib-pps.lua
%{_texmfdistdir}/tex/context/base/mlib-pps.mkiv
%{_texmfdistdir}/tex/context/base/mlib-run.lua
%{_texmfdistdir}/tex/context/base/mtx-context-arrange.tex
%{_texmfdistdir}/tex/context/base/mtx-context-combine.tex
%{_texmfdistdir}/tex/context/base/mtx-context-common.tex
%{_texmfdistdir}/tex/context/base/mtx-context-ideas.tex
%{_texmfdistdir}/tex/context/base/mtx-context-listing.tex
%{_texmfdistdir}/tex/context/base/mtx-context-markdown.tex
%{_texmfdistdir}/tex/context/base/mtx-context-select.tex
%{_texmfdistdir}/tex/context/base/mtx-context-timing.tex
%{_texmfdistdir}/tex/context/base/mult-aux.lua
%{_texmfdistdir}/tex/context/base/mult-aux.mkii
%{_texmfdistdir}/tex/context/base/mult-aux.mkiv
%{_texmfdistdir}/tex/context/base/mult-chk.lua
%{_texmfdistdir}/tex/context/base/mult-chk.mkii
%{_texmfdistdir}/tex/context/base/mult-chk.mkiv
%{_texmfdistdir}/tex/context/base/mult-com.mkii
%{_texmfdistdir}/tex/context/base/mult-con.mkii
%{_texmfdistdir}/tex/context/base/mult-de.mkii
%{_texmfdistdir}/tex/context/base/mult-def.lua
%{_texmfdistdir}/tex/context/base/mult-def.mkii
%{_texmfdistdir}/tex/context/base/mult-def.mkiv
%{_texmfdistdir}/tex/context/base/mult-dim.mkvi
%{_texmfdistdir}/tex/context/base/mult-en.mkii
%{_texmfdistdir}/tex/context/base/mult-fr.mkii
%{_texmfdistdir}/tex/context/base/mult-fst.mkii
%{_texmfdistdir}/tex/context/base/mult-ini.lua
%{_texmfdistdir}/tex/context/base/mult-ini.mkii
%{_texmfdistdir}/tex/context/base/mult-ini.mkiv
%{_texmfdistdir}/tex/context/base/mult-it.mkii
%{_texmfdistdir}/tex/context/base/mult-low.lua
%{_texmfdistdir}/tex/context/base/mult-mcs.mkii
%{_texmfdistdir}/tex/context/base/mult-mde.mkii
%{_texmfdistdir}/tex/context/base/mult-men.mkii
%{_texmfdistdir}/tex/context/base/mult-mes.lua
%{_texmfdistdir}/tex/context/base/mult-mfr.mkii
%{_texmfdistdir}/tex/context/base/mult-mit.mkii
%{_texmfdistdir}/tex/context/base/mult-mnl.mkii
%{_texmfdistdir}/tex/context/base/mult-mno.mkii
%{_texmfdistdir}/tex/context/base/mult-mpe.mkii
%{_texmfdistdir}/tex/context/base/mult-mps.lua
%{_texmfdistdir}/tex/context/base/mult-mro.mkii
%{_texmfdistdir}/tex/context/base/mult-nl.mkii
%{_texmfdistdir}/tex/context/base/mult-pe.mkii
%{_texmfdistdir}/tex/context/base/mult-prm.lua
%{_texmfdistdir}/tex/context/base/mult-prm.mkiv
%{_texmfdistdir}/tex/context/base/mult-ro.mkii
%{_texmfdistdir}/tex/context/base/mult-sys.mkii
%{_texmfdistdir}/tex/context/base/mult-sys.mkiv
%{_texmfdistdir}/tex/context/base/node-acc.lua
%{_texmfdistdir}/tex/context/base/node-aux.lua
%{_texmfdistdir}/tex/context/base/node-bck.lua
%{_texmfdistdir}/tex/context/base/node-bck.mkiv
%{_texmfdistdir}/tex/context/base/node-dir.lua
%{_texmfdistdir}/tex/context/base/node-ext.lua
%{_texmfdistdir}/tex/context/base/node-fin.lua
%{_texmfdistdir}/tex/context/base/node-fin.mkiv
%{_texmfdistdir}/tex/context/base/node-fnt.lua
%{_texmfdistdir}/tex/context/base/node-ini.lua
%{_texmfdistdir}/tex/context/base/node-ini.mkiv
%{_texmfdistdir}/tex/context/base/node-inj.lua
%{_texmfdistdir}/tex/context/base/node-mig.lua
%{_texmfdistdir}/tex/context/base/node-mig.mkiv
%{_texmfdistdir}/tex/context/base/node-pag.lua
%{_texmfdistdir}/tex/context/base/node-pag.mkiv
%{_texmfdistdir}/tex/context/base/node-par.lua
%{_texmfdistdir}/tex/context/base/node-par.mkiv
%{_texmfdistdir}/tex/context/base/node-pro.lua
%{_texmfdistdir}/tex/context/base/node-ref.lua
%{_texmfdistdir}/tex/context/base/node-res.lua
%{_texmfdistdir}/tex/context/base/node-rul.lua
%{_texmfdistdir}/tex/context/base/node-rul.mkiv
%{_texmfdistdir}/tex/context/base/node-ser.lua
%{_texmfdistdir}/tex/context/base/node-shp.lua
%{_texmfdistdir}/tex/context/base/node-spl.lua
%{_texmfdistdir}/tex/context/base/node-spl.mkiv
%{_texmfdistdir}/tex/context/base/node-tex.lua
%{_texmfdistdir}/tex/context/base/node-tra.lua
%{_texmfdistdir}/tex/context/base/node-tsk.lua
%{_texmfdistdir}/tex/context/base/node-tst.lua
%{_texmfdistdir}/tex/context/base/node-typ.lua
%{_texmfdistdir}/tex/context/base/norm-alo.mkii
%{_texmfdistdir}/tex/context/base/norm-ctx.mkii
%{_texmfdistdir}/tex/context/base/norm-ctx.mkiv
%{_texmfdistdir}/tex/context/base/norm-etx.mkii
%{_texmfdistdir}/tex/context/base/norm-ltx.mkii
%{_texmfdistdir}/tex/context/base/norm-ptx.mkii
%{_texmfdistdir}/tex/context/base/norm-tex.mkii
%{_texmfdistdir}/tex/context/base/norm-xtx.mkii
%{_texmfdistdir}/tex/context/base/pack-bar.mkiv
%{_texmfdistdir}/tex/context/base/pack-bck.mkvi
%{_texmfdistdir}/tex/context/base/pack-box.mkii
%{_texmfdistdir}/tex/context/base/pack-box.mkiv
%{_texmfdistdir}/tex/context/base/pack-com.mkiv
%{_texmfdistdir}/tex/context/base/pack-fen.mkiv
%{_texmfdistdir}/tex/context/base/pack-lyr.mkii
%{_texmfdistdir}/tex/context/base/pack-lyr.mkiv
%{_texmfdistdir}/tex/context/base/pack-mis.mkvi
%{_texmfdistdir}/tex/context/base/pack-mrl.mkiv
%{_texmfdistdir}/tex/context/base/pack-obj.lua
%{_texmfdistdir}/tex/context/base/pack-obj.mkii
%{_texmfdistdir}/tex/context/base/pack-obj.mkiv
%{_texmfdistdir}/tex/context/base/pack-pos.mkiv
%{_texmfdistdir}/tex/context/base/pack-rul.lua
%{_texmfdistdir}/tex/context/base/pack-rul.mkii
%{_texmfdistdir}/tex/context/base/pack-rul.mkiv
%{_texmfdistdir}/tex/context/base/page-app.mkii
%{_texmfdistdir}/tex/context/base/page-app.mkiv
%{_texmfdistdir}/tex/context/base/page-bck.mkii
%{_texmfdistdir}/tex/context/base/page-bck.mkiv
%{_texmfdistdir}/tex/context/base/page-box.mkvi
%{_texmfdistdir}/tex/context/base/page-brk.mkiv
%{_texmfdistdir}/tex/context/base/page-col.mkiv
%{_texmfdistdir}/tex/context/base/page-com.mkiv
%{_texmfdistdir}/tex/context/base/page-fac.mkiv
%{_texmfdistdir}/tex/context/base/page-flt.lua
%{_texmfdistdir}/tex/context/base/page-flt.mkiv
%{_texmfdistdir}/tex/context/base/page-flw.mkii
%{_texmfdistdir}/tex/context/base/page-flw.mkiv
%{_texmfdistdir}/tex/context/base/page-grd.mkiv
%{_texmfdistdir}/tex/context/base/page-imp.mkii
%{_texmfdistdir}/tex/context/base/page-imp.mkiv
%{_texmfdistdir}/tex/context/base/page-inf.mkiv
%{_texmfdistdir}/tex/context/base/page-ini.mkii
%{_texmfdistdir}/tex/context/base/page-ini.mkiv
%{_texmfdistdir}/tex/context/base/page-ins.mkii
%{_texmfdistdir}/tex/context/base/page-ins.mkiv
%{_texmfdistdir}/tex/context/base/page-lay.mkii
%{_texmfdistdir}/tex/context/base/page-lay.mkiv
%{_texmfdistdir}/tex/context/base/page-lin.lua
%{_texmfdistdir}/tex/context/base/page-lin.mkii
%{_texmfdistdir}/tex/context/base/page-lin.mkiv
%{_texmfdistdir}/tex/context/base/page-log.mkii
%{_texmfdistdir}/tex/context/base/page-mak.mkii
%{_texmfdistdir}/tex/context/base/page-mak.mkvi
%{_texmfdistdir}/tex/context/base/page-mar.mkii
%{_texmfdistdir}/tex/context/base/page-mbk.mkvi
%{_texmfdistdir}/tex/context/base/page-mis.lua
%{_texmfdistdir}/tex/context/base/page-mis.mkii
%{_texmfdistdir}/tex/context/base/page-mis.mkiv
%{_texmfdistdir}/tex/context/base/page-mrk.mkiv
%{_texmfdistdir}/tex/context/base/page-mul.mkii
%{_texmfdistdir}/tex/context/base/page-mul.mkiv
%{_texmfdistdir}/tex/context/base/page-not.mkii
%{_texmfdistdir}/tex/context/base/page-not.mkiv
%{_texmfdistdir}/tex/context/base/page-one.mkii
%{_texmfdistdir}/tex/context/base/page-one.mkiv
%{_texmfdistdir}/tex/context/base/page-otr.mkvi
%{_texmfdistdir}/tex/context/base/page-par.mkii
%{_texmfdistdir}/tex/context/base/page-par.mkiv
%{_texmfdistdir}/tex/context/base/page-plg.mkii
%{_texmfdistdir}/tex/context/base/page-plg.mkiv
%{_texmfdistdir}/tex/context/base/page-run.mkii
%{_texmfdistdir}/tex/context/base/page-run.mkiv
%{_texmfdistdir}/tex/context/base/page-sel.mkiv
%{_texmfdistdir}/tex/context/base/page-set.mkii
%{_texmfdistdir}/tex/context/base/page-set.mkiv
%{_texmfdistdir}/tex/context/base/page-sid.mkii
%{_texmfdistdir}/tex/context/base/page-sid.mkiv
%{_texmfdistdir}/tex/context/base/page-spr.mkii
%{_texmfdistdir}/tex/context/base/page-spr.mkiv
%{_texmfdistdir}/tex/context/base/page-str.lua
%{_texmfdistdir}/tex/context/base/page-str.mkii
%{_texmfdistdir}/tex/context/base/page-str.mkiv
%{_texmfdistdir}/tex/context/base/page-txt.mkii
%{_texmfdistdir}/tex/context/base/page-txt.mkvi
%{_texmfdistdir}/tex/context/base/page-var.mkiv
%{_texmfdistdir}/tex/context/base/pdfr-def.mkii
%{_texmfdistdir}/tex/context/base/pdfr-ec.mkii
%{_texmfdistdir}/tex/context/base/pdfr-il2.mkii
%{_texmfdistdir}/tex/context/base/phys-dim.lua
%{_texmfdistdir}/tex/context/base/phys-dim.mkiv
%{_texmfdistdir}/tex/context/base/ppchtex.mkii
%{_texmfdistdir}/tex/context/base/ppchtex.mkiv
%{_texmfdistdir}/tex/context/base/prop-ini.mkii
%{_texmfdistdir}/tex/context/base/prop-ini.mkiv
%{_texmfdistdir}/tex/context/base/prop-lay.mkii
%{_texmfdistdir}/tex/context/base/prop-mis.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-1.lua
%{_texmfdistdir}/tex/context/base/regi-8859-1.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-10.lua
%{_texmfdistdir}/tex/context/base/regi-8859-10.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-11.lua
%{_texmfdistdir}/tex/context/base/regi-8859-13.lua
%{_texmfdistdir}/tex/context/base/regi-8859-13.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-14.lua
%{_texmfdistdir}/tex/context/base/regi-8859-15.lua
%{_texmfdistdir}/tex/context/base/regi-8859-15.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-16.lua
%{_texmfdistdir}/tex/context/base/regi-8859-16.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-2.lua
%{_texmfdistdir}/tex/context/base/regi-8859-2.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-3.lua
%{_texmfdistdir}/tex/context/base/regi-8859-3.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-4.lua
%{_texmfdistdir}/tex/context/base/regi-8859-4.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-5.lua
%{_texmfdistdir}/tex/context/base/regi-8859-5.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-6.lua
%{_texmfdistdir}/tex/context/base/regi-8859-7.lua
%{_texmfdistdir}/tex/context/base/regi-8859-7.mkii
%{_texmfdistdir}/tex/context/base/regi-8859-8.lua
%{_texmfdistdir}/tex/context/base/regi-8859-9.lua
%{_texmfdistdir}/tex/context/base/regi-8859-9.mkii
%{_texmfdistdir}/tex/context/base/regi-cp1250.lua
%{_texmfdistdir}/tex/context/base/regi-cp1250.mkii
%{_texmfdistdir}/tex/context/base/regi-cp1251.lua
%{_texmfdistdir}/tex/context/base/regi-cp1251.mkii
%{_texmfdistdir}/tex/context/base/regi-cp1252.lua
%{_texmfdistdir}/tex/context/base/regi-cp1252.mkii
%{_texmfdistdir}/tex/context/base/regi-cp1253.lua
%{_texmfdistdir}/tex/context/base/regi-cp1253.mkii
%{_texmfdistdir}/tex/context/base/regi-cp1254.lua
%{_texmfdistdir}/tex/context/base/regi-cp1254.mkii
%{_texmfdistdir}/tex/context/base/regi-cp1255.lua
%{_texmfdistdir}/tex/context/base/regi-cp1256.lua
%{_texmfdistdir}/tex/context/base/regi-cp1257.lua
%{_texmfdistdir}/tex/context/base/regi-cp1257.mkii
%{_texmfdistdir}/tex/context/base/regi-cp1258.lua
%{_texmfdistdir}/tex/context/base/regi-cyp.mkii
%{_texmfdistdir}/tex/context/base/regi-cyr.mkii
%{_texmfdistdir}/tex/context/base/regi-def.mkii
%{_texmfdistdir}/tex/context/base/regi-demo.lua
%{_texmfdistdir}/tex/context/base/regi-ibm.mkii
%{_texmfdistdir}/tex/context/base/regi-ini.lua
%{_texmfdistdir}/tex/context/base/regi-ini.mkii
%{_texmfdistdir}/tex/context/base/regi-ini.mkiv
%{_texmfdistdir}/tex/context/base/regi-mac.mkii
%{_texmfdistdir}/tex/context/base/regi-syn.mkii
%{_texmfdistdir}/tex/context/base/regi-uni.mkii
%{_texmfdistdir}/tex/context/base/regi-utf.mkii
%{_texmfdistdir}/tex/context/base/regi-vis.mkii
%{_texmfdistdir}/tex/context/base/rlxcache.rlx
%{_texmfdistdir}/tex/context/base/rlxtools.rlx
%{_texmfdistdir}/tex/context/base/s-abr-01.tex
%{_texmfdistdir}/tex/context/base/s-abr-02.tex
%{_texmfdistdir}/tex/context/base/s-abr-03.tex
%{_texmfdistdir}/tex/context/base/s-abr-04.tex
%{_texmfdistdir}/tex/context/base/s-art-01.mkiv
%{_texmfdistdir}/tex/context/base/s-cdr-01.tex
%{_texmfdistdir}/tex/context/base/s-chi-00.mkii
%{_texmfdistdir}/tex/context/base/s-def-01.mkiv
%{_texmfdistdir}/tex/context/base/s-faq-00.tex
%{_texmfdistdir}/tex/context/base/s-faq-01.tex
%{_texmfdistdir}/tex/context/base/s-faq-02.tex
%{_texmfdistdir}/tex/context/base/s-faq-03.tex
%{_texmfdistdir}/tex/context/base/s-fnt-01.mkii
%{_texmfdistdir}/tex/context/base/s-fnt-02.mkii
%{_texmfdistdir}/tex/context/base/s-fnt-10.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-11.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-20.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-21.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-23.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-24.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-26.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-28.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-29.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-30.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-31.mkiv
%{_texmfdistdir}/tex/context/base/s-fnt-32.mkiv
%{_texmfdistdir}/tex/context/base/s-fonts-missing.mkiv
%{_texmfdistdir}/tex/context/base/s-fonts-tables.lua
%{_texmfdistdir}/tex/context/base/s-fonts-tables.mkiv
%{_texmfdistdir}/tex/context/base/s-grk-00.mkii
%{_texmfdistdir}/tex/context/base/s-inf-01.mkvi
%{_texmfdistdir}/tex/context/base/s-inf-02.mkiv
%{_texmfdistdir}/tex/context/base/s-inf-03.mkiv
%{_texmfdistdir}/tex/context/base/s-inf-04.mkiv
%{_texmfdistdir}/tex/context/base/s-jap-00.mkii
%{_texmfdistdir}/tex/context/base/s-lan-03.mkiv
%{_texmfdistdir}/tex/context/base/s-lan-04.mkiv
%{_texmfdistdir}/tex/context/base/s-mag-01.tex
%{_texmfdistdir}/tex/context/base/s-map-10.mkii
%{_texmfdistdir}/tex/context/base/s-map-10.mkiv
%{_texmfdistdir}/tex/context/base/s-mat-10.mkiv
%{_texmfdistdir}/tex/context/base/s-mat-11.mkiv
%{_texmfdistdir}/tex/context/base/s-mat-12.mkiv
%{_texmfdistdir}/tex/context/base/s-mod-00.mkii
%{_texmfdistdir}/tex/context/base/s-mod-00.mkiv
%{_texmfdistdir}/tex/context/base/s-mod-01.mkii
%{_texmfdistdir}/tex/context/base/s-mod-01.mkiv
%{_texmfdistdir}/tex/context/base/s-mod-02.mkii
%{_texmfdistdir}/tex/context/base/s-mod-02.mkiv
%{_texmfdistdir}/tex/context/base/s-mod.ctx
%{_texmfdistdir}/tex/context/base/s-phy-01.mkiv
%{_texmfdistdir}/tex/context/base/s-pre-00.tex
%{_texmfdistdir}/tex/context/base/s-pre-01.tex
%{_texmfdistdir}/tex/context/base/s-pre-02.tex
%{_texmfdistdir}/tex/context/base/s-pre-03.tex
%{_texmfdistdir}/tex/context/base/s-pre-04.tex
%{_texmfdistdir}/tex/context/base/s-pre-05.tex
%{_texmfdistdir}/tex/context/base/s-pre-06.tex
%{_texmfdistdir}/tex/context/base/s-pre-07.tex
%{_texmfdistdir}/tex/context/base/s-pre-08.tex
%{_texmfdistdir}/tex/context/base/s-pre-09.tex
%{_texmfdistdir}/tex/context/base/s-pre-10.tex
%{_texmfdistdir}/tex/context/base/s-pre-11.tex
%{_texmfdistdir}/tex/context/base/s-pre-12.tex
%{_texmfdistdir}/tex/context/base/s-pre-13.tex
%{_texmfdistdir}/tex/context/base/s-pre-14.tex
%{_texmfdistdir}/tex/context/base/s-pre-15.tex
%{_texmfdistdir}/tex/context/base/s-pre-16.tex
%{_texmfdistdir}/tex/context/base/s-pre-17.tex
%{_texmfdistdir}/tex/context/base/s-pre-18.tex
%{_texmfdistdir}/tex/context/base/s-pre-19.tex
%{_texmfdistdir}/tex/context/base/s-pre-22.tex
%{_texmfdistdir}/tex/context/base/s-pre-23.tex
%{_texmfdistdir}/tex/context/base/s-pre-26.tex
%{_texmfdistdir}/tex/context/base/s-pre-27.tex
%{_texmfdistdir}/tex/context/base/s-pre-30.mkii
%{_texmfdistdir}/tex/context/base/s-pre-30.mkiv
%{_texmfdistdir}/tex/context/base/s-pre-50.tex
%{_texmfdistdir}/tex/context/base/s-pre-60.mkii
%{_texmfdistdir}/tex/context/base/s-pre-60.mkiv
%{_texmfdistdir}/tex/context/base/s-pre-61.tex
%{_texmfdistdir}/tex/context/base/s-pre-62.tex
%{_texmfdistdir}/tex/context/base/s-pre-63.tex
%{_texmfdistdir}/tex/context/base/s-pre-64.tex
%{_texmfdistdir}/tex/context/base/s-pre-66.tex
%{_texmfdistdir}/tex/context/base/s-pre-67.tex
%{_texmfdistdir}/tex/context/base/s-pre-68.tex
%{_texmfdistdir}/tex/context/base/s-pre-69.mkiv
%{_texmfdistdir}/tex/context/base/s-pre-70.mkiv
%{_texmfdistdir}/tex/context/base/s-pre-71.lua
%{_texmfdistdir}/tex/context/base/s-pre-71.mkii
%{_texmfdistdir}/tex/context/base/s-pre-71.mkiv
%{_texmfdistdir}/tex/context/base/s-pre-93.tex
%{_texmfdistdir}/tex/context/base/s-pre-96.tex
%{_texmfdistdir}/tex/context/base/s-ptj-01.tex
%{_texmfdistdir}/tex/context/base/s-reg-01.mkiv
%{_texmfdistdir}/tex/context/base/s-set-31.mkiv
%{_texmfdistdir}/tex/context/base/s-syn-01.tex
%{_texmfdistdir}/tex/context/base/scrn-bar.mkvi
%{_texmfdistdir}/tex/context/base/scrn-but.lua
%{_texmfdistdir}/tex/context/base/scrn-but.mkvi
%{_texmfdistdir}/tex/context/base/scrn-fld.lua
%{_texmfdistdir}/tex/context/base/scrn-fld.mkii
%{_texmfdistdir}/tex/context/base/scrn-fld.mkvi
%{_texmfdistdir}/tex/context/base/scrn-hlp.lua
%{_texmfdistdir}/tex/context/base/scrn-hlp.mkii
%{_texmfdistdir}/tex/context/base/scrn-hlp.mkvi
%{_texmfdistdir}/tex/context/base/scrn-ini.lua
%{_texmfdistdir}/tex/context/base/scrn-ini.mkvi
%{_texmfdistdir}/tex/context/base/scrn-int.mkii
%{_texmfdistdir}/tex/context/base/scrn-nav.mkii
%{_texmfdistdir}/tex/context/base/scrn-pag.lua
%{_texmfdistdir}/tex/context/base/scrn-pag.mkvi
%{_texmfdistdir}/tex/context/base/scrn-ref.lua
%{_texmfdistdir}/tex/context/base/scrn-ref.mkvi
%{_texmfdistdir}/tex/context/base/scrn-wid.lua
%{_texmfdistdir}/tex/context/base/scrn-wid.mkvi
%{_texmfdistdir}/tex/context/base/scrp-cjk.lua
%{_texmfdistdir}/tex/context/base/scrp-eth.lua
%{_texmfdistdir}/tex/context/base/scrp-ini.lua
%{_texmfdistdir}/tex/context/base/scrp-ini.mkiv
%{_texmfdistdir}/tex/context/base/sort-def.mkii
%{_texmfdistdir}/tex/context/base/sort-ini.lua
%{_texmfdistdir}/tex/context/base/sort-ini.mkii
%{_texmfdistdir}/tex/context/base/sort-ini.mkiv
%{_texmfdistdir}/tex/context/base/sort-lan.lua
%{_texmfdistdir}/tex/context/base/sort-lan.mkii
%{_texmfdistdir}/tex/context/base/spac-adj.lua
%{_texmfdistdir}/tex/context/base/spac-adj.mkiv
%{_texmfdistdir}/tex/context/base/spac-ali.lua
%{_texmfdistdir}/tex/context/base/spac-ali.mkiv
%{_texmfdistdir}/tex/context/base/spac-chr.lua
%{_texmfdistdir}/tex/context/base/spac-chr.mkiv
%{_texmfdistdir}/tex/context/base/spac-def.mkiv
%{_texmfdistdir}/tex/context/base/spac-gen.mkii
%{_texmfdistdir}/tex/context/base/spac-grd.mkii
%{_texmfdistdir}/tex/context/base/spac-grd.mkiv
%{_texmfdistdir}/tex/context/base/spac-hor.lua
%{_texmfdistdir}/tex/context/base/spac-hor.mkiv
%{_texmfdistdir}/tex/context/base/spac-lin.mkiv
%{_texmfdistdir}/tex/context/base/spac-pag.mkiv
%{_texmfdistdir}/tex/context/base/spac-par.mkiv
%{_texmfdistdir}/tex/context/base/spac-ver.lua
%{_texmfdistdir}/tex/context/base/spac-ver.mkiv
%{_texmfdistdir}/tex/context/base/spec-def.mkii
%{_texmfdistdir}/tex/context/base/spec-dpm.mkii
%{_texmfdistdir}/tex/context/base/spec-dpx.mkii
%{_texmfdistdir}/tex/context/base/spec-dvi.mkii
%{_texmfdistdir}/tex/context/base/spec-fdf.mkii
%{_texmfdistdir}/tex/context/base/spec-ini.mkii
%{_texmfdistdir}/tex/context/base/spec-mis.mkii
%{_texmfdistdir}/tex/context/base/spec-pdf.mkii
%{_texmfdistdir}/tex/context/base/spec-ps.mkii
%{_texmfdistdir}/tex/context/base/spec-tpd.mkii
%{_texmfdistdir}/tex/context/base/spec-tr.mkii
%{_texmfdistdir}/tex/context/base/spec-tst.mkii
%{_texmfdistdir}/tex/context/base/spec-var.mkii
%{_texmfdistdir}/tex/context/base/spec-win.mkii
%{_texmfdistdir}/tex/context/base/spec-xet.mkii
%{_texmfdistdir}/tex/context/base/spec-xtx.mkii
%{_texmfdistdir}/tex/context/base/spec-yy.mkii
%{_texmfdistdir}/tex/context/base/status-files.pdf
%{_texmfdistdir}/tex/context/base/status-lua.pdf
%{_texmfdistdir}/tex/context/base/status-mkiv.lua
%{_texmfdistdir}/tex/context/base/status-mkiv.tex
%{_texmfdistdir}/tex/context/base/strc-bkm.lua
%{_texmfdistdir}/tex/context/base/strc-bkm.mkiv
%{_texmfdistdir}/tex/context/base/strc-blk.lua
%{_texmfdistdir}/tex/context/base/strc-blk.mkii
%{_texmfdistdir}/tex/context/base/strc-blk.mkiv
%{_texmfdistdir}/tex/context/base/strc-con.lua
%{_texmfdistdir}/tex/context/base/strc-con.mkvi
%{_texmfdistdir}/tex/context/base/strc-def.mkiv
%{_texmfdistdir}/tex/context/base/strc-des.mkii
%{_texmfdistdir}/tex/context/base/strc-des.mkvi
%{_texmfdistdir}/tex/context/base/strc-doc.lua
%{_texmfdistdir}/tex/context/base/strc-doc.mkiv
%{_texmfdistdir}/tex/context/base/strc-enu.mkvi
%{_texmfdistdir}/tex/context/base/strc-flt.lua
%{_texmfdistdir}/tex/context/base/strc-flt.mkii
%{_texmfdistdir}/tex/context/base/strc-flt.mkvi
%{_texmfdistdir}/tex/context/base/strc-ind.mkiv
%{_texmfdistdir}/tex/context/base/strc-ini.lua
%{_texmfdistdir}/tex/context/base/strc-ini.mkvi
%{_texmfdistdir}/tex/context/base/strc-itm.lua
%{_texmfdistdir}/tex/context/base/strc-itm.mkii
%{_texmfdistdir}/tex/context/base/strc-itm.mkvi
%{_texmfdistdir}/tex/context/base/strc-lab.mkiv
%{_texmfdistdir}/tex/context/base/strc-lev.lua
%{_texmfdistdir}/tex/context/base/strc-lev.mkvi
%{_texmfdistdir}/tex/context/base/strc-lnt.mkii
%{_texmfdistdir}/tex/context/base/strc-lnt.mkvi
%{_texmfdistdir}/tex/context/base/strc-lst.lua
%{_texmfdistdir}/tex/context/base/strc-lst.mkii
%{_texmfdistdir}/tex/context/base/strc-lst.mkvi
%{_texmfdistdir}/tex/context/base/strc-mar.lua
%{_texmfdistdir}/tex/context/base/strc-mar.mkii
%{_texmfdistdir}/tex/context/base/strc-mar.mkiv
%{_texmfdistdir}/tex/context/base/strc-mat.lua
%{_texmfdistdir}/tex/context/base/strc-mat.mkii
%{_texmfdistdir}/tex/context/base/strc-mat.mkiv
%{_texmfdistdir}/tex/context/base/strc-not.lua
%{_texmfdistdir}/tex/context/base/strc-not.mkii
%{_texmfdistdir}/tex/context/base/strc-not.mkvi
%{_texmfdistdir}/tex/context/base/strc-num.lua
%{_texmfdistdir}/tex/context/base/strc-num.mkii
%{_texmfdistdir}/tex/context/base/strc-num.mkiv
%{_texmfdistdir}/tex/context/base/strc-pag.lua
%{_texmfdistdir}/tex/context/base/strc-pag.mkii
%{_texmfdistdir}/tex/context/base/strc-pag.mkiv
%{_texmfdistdir}/tex/context/base/strc-ref.lua
%{_texmfdistdir}/tex/context/base/strc-ref.mkii
%{_texmfdistdir}/tex/context/base/strc-ref.mkvi
%{_texmfdistdir}/tex/context/base/strc-reg.lua
%{_texmfdistdir}/tex/context/base/strc-reg.mkii
%{_texmfdistdir}/tex/context/base/strc-reg.mkiv
%{_texmfdistdir}/tex/context/base/strc-ren.mkiv
%{_texmfdistdir}/tex/context/base/strc-rsc.lua
%{_texmfdistdir}/tex/context/base/strc-sbe.mkiv
%{_texmfdistdir}/tex/context/base/strc-sec.mkii
%{_texmfdistdir}/tex/context/base/strc-sec.mkiv
%{_texmfdistdir}/tex/context/base/strc-swd.mkii
%{_texmfdistdir}/tex/context/base/strc-syn.lua
%{_texmfdistdir}/tex/context/base/strc-syn.mkii
%{_texmfdistdir}/tex/context/base/strc-syn.mkiv
%{_texmfdistdir}/tex/context/base/strc-tag.lua
%{_texmfdistdir}/tex/context/base/strc-tag.mkiv
%{_texmfdistdir}/tex/context/base/strc-xml.mkiv
%{_texmfdistdir}/tex/context/base/supp-ali.mkii
%{_texmfdistdir}/tex/context/base/supp-ali.mkiv
%{_texmfdistdir}/tex/context/base/supp-box.lua
%{_texmfdistdir}/tex/context/base/supp-box.mkii
%{_texmfdistdir}/tex/context/base/supp-box.mkiv
%{_texmfdistdir}/tex/context/base/supp-dir.mkii
%{_texmfdistdir}/tex/context/base/supp-dir.mkiv
%{_texmfdistdir}/tex/context/base/supp-emp.mkii
%{_texmfdistdir}/tex/context/base/supp-eps.mkii
%{_texmfdistdir}/tex/context/base/supp-fil.mkii
%{_texmfdistdir}/tex/context/base/supp-fun.mkii
%{_texmfdistdir}/tex/context/base/supp-fun.mkiv
%{_texmfdistdir}/tex/context/base/supp-lat.mkii
%{_texmfdistdir}/tex/context/base/supp-mat.mkii
%{_texmfdistdir}/tex/context/base/supp-mat.mkiv
%{_texmfdistdir}/tex/context/base/supp-mis.tex
%{_texmfdistdir}/tex/context/base/supp-mpe.tex
%{_texmfdistdir}/tex/context/base/supp-mps.mkii
%{_texmfdistdir}/tex/context/base/supp-mrk.mkii
%{_texmfdistdir}/tex/context/base/supp-num.mkii
%{_texmfdistdir}/tex/context/base/supp-num.mkiv
%{_texmfdistdir}/tex/context/base/supp-pat.mkii
%{_texmfdistdir}/tex/context/base/supp-pdf.tex
%{_texmfdistdir}/tex/context/base/supp-ran.lua
%{_texmfdistdir}/tex/context/base/supp-ran.mkii
%{_texmfdistdir}/tex/context/base/supp-ran.mkiv
%{_texmfdistdir}/tex/context/base/supp-spe.mkii
%{_texmfdistdir}/tex/context/base/supp-tpi.mkii
%{_texmfdistdir}/tex/context/base/supp-vis.mkii
%{_texmfdistdir}/tex/context/base/supp-vis.mkiv
%{_texmfdistdir}/tex/context/base/symb-cow.mkii
%{_texmfdistdir}/tex/context/base/symb-eur.mkii
%{_texmfdistdir}/tex/context/base/symb-glm.mkii
%{_texmfdistdir}/tex/context/base/symb-imp-cow.mkiv
%{_texmfdistdir}/tex/context/base/symb-imp-eur.mkiv
%{_texmfdistdir}/tex/context/base/symb-imp-jmn.mkiv
%{_texmfdistdir}/tex/context/base/symb-imp-mis.mkiv
%{_texmfdistdir}/tex/context/base/symb-imp-mvs.mkiv
%{_texmfdistdir}/tex/context/base/symb-imp-nav.mkiv
%{_texmfdistdir}/tex/context/base/symb-ini.lua
%{_texmfdistdir}/tex/context/base/symb-ini.mkii
%{_texmfdistdir}/tex/context/base/symb-ini.mkiv
%{_texmfdistdir}/tex/context/base/symb-jmn.mkii
%{_texmfdistdir}/tex/context/base/symb-mis.mkii
%{_texmfdistdir}/tex/context/base/symb-mvs.mkii
%{_texmfdistdir}/tex/context/base/symb-nav.mkii
%{_texmfdistdir}/tex/context/base/symb-run.mkii
%{_texmfdistdir}/tex/context/base/symb-run.mkiv
%{_texmfdistdir}/tex/context/base/symb-uni.mkii
%{_texmfdistdir}/tex/context/base/symb-was.mkii
%{_texmfdistdir}/tex/context/base/syst-aux.lua
%{_texmfdistdir}/tex/context/base/syst-aux.mkiv
%{_texmfdistdir}/tex/context/base/syst-con.lua
%{_texmfdistdir}/tex/context/base/syst-con.mkii
%{_texmfdistdir}/tex/context/base/syst-con.mkiv
%{_texmfdistdir}/tex/context/base/syst-ext.mkii
%{_texmfdistdir}/tex/context/base/syst-fnt.mkii
%{_texmfdistdir}/tex/context/base/syst-fnt.mkiv
%{_texmfdistdir}/tex/context/base/syst-gen.mkii
%{_texmfdistdir}/tex/context/base/syst-ini.mkii
%{_texmfdistdir}/tex/context/base/syst-ini.mkiv
%{_texmfdistdir}/tex/context/base/syst-lua.lua
%{_texmfdistdir}/tex/context/base/syst-lua.mkiv
%{_texmfdistdir}/tex/context/base/syst-mes.mkiv
%{_texmfdistdir}/tex/context/base/syst-new.mkii
%{_texmfdistdir}/tex/context/base/syst-pln.mkii
%{_texmfdistdir}/tex/context/base/syst-pln.mkiv
%{_texmfdistdir}/tex/context/base/syst-rtp.mkii
%{_texmfdistdir}/tex/context/base/syst-rtp.mkiv
%{_texmfdistdir}/tex/context/base/syst-str.mkii
%{_texmfdistdir}/tex/context/base/tabl-com.mkii
%{_texmfdistdir}/tex/context/base/tabl-com.mkiv
%{_texmfdistdir}/tex/context/base/tabl-ltb.mkii
%{_texmfdistdir}/tex/context/base/tabl-ltb.mkiv
%{_texmfdistdir}/tex/context/base/tabl-ntb.mkii
%{_texmfdistdir}/tex/context/base/tabl-ntb.mkiv
%{_texmfdistdir}/tex/context/base/tabl-nte.mkii
%{_texmfdistdir}/tex/context/base/tabl-nte.mkiv
%{_texmfdistdir}/tex/context/base/tabl-pln.mkii
%{_texmfdistdir}/tex/context/base/tabl-pln.mkiv
%{_texmfdistdir}/tex/context/base/tabl-tab.mkii
%{_texmfdistdir}/tex/context/base/tabl-tab.mkiv
%{_texmfdistdir}/tex/context/base/tabl-tbl.lua
%{_texmfdistdir}/tex/context/base/tabl-tbl.mkii
%{_texmfdistdir}/tex/context/base/tabl-tbl.mkiv
%{_texmfdistdir}/tex/context/base/tabl-tsp.mkii
%{_texmfdistdir}/tex/context/base/tabl-tsp.mkiv
%{_texmfdistdir}/tex/context/base/tabl-xnt.mkvi
%{_texmfdistdir}/tex/context/base/tabl-xtb.lua
%{_texmfdistdir}/tex/context/base/tabl-xtb.mkvi
%{_texmfdistdir}/tex/context/base/task-ini.lua
%{_texmfdistdir}/tex/context/base/task-ini.mkiv
%{_texmfdistdir}/tex/context/base/thrd-pic.mkii
%{_texmfdistdir}/tex/context/base/thrd-ran.mkii
%{_texmfdistdir}/tex/context/base/thrd-tab.mkii
%{_texmfdistdir}/tex/context/base/thrd-trg.mkii
%{_texmfdistdir}/tex/context/base/toks-ini.lua
%{_texmfdistdir}/tex/context/base/toks-ini.mkiv
%{_texmfdistdir}/tex/context/base/trac-deb.lua
%{_texmfdistdir}/tex/context/base/trac-deb.mkiv
%{_texmfdistdir}/tex/context/base/trac-fil.lua
%{_texmfdistdir}/tex/context/base/trac-inf.lua
%{_texmfdistdir}/tex/context/base/trac-lmx.lua
%{_texmfdistdir}/tex/context/base/trac-log.lua
%{_texmfdistdir}/tex/context/base/trac-pro.lua
%{_texmfdistdir}/tex/context/base/trac-set.lua
%{_texmfdistdir}/tex/context/base/trac-tex.lua
%{_texmfdistdir}/tex/context/base/trac-tex.mkiv
%{_texmfdistdir}/tex/context/base/trac-tim.lua
%{_texmfdistdir}/tex/context/base/trac-vis.mkii
%{_texmfdistdir}/tex/context/base/trac-vis.mkiv
%{_texmfdistdir}/tex/context/base/type-buy.mkii
%{_texmfdistdir}/tex/context/base/type-cbg.mkii
%{_texmfdistdir}/tex/context/base/type-cow.mkii
%{_texmfdistdir}/tex/context/base/type-def.mkii
%{_texmfdistdir}/tex/context/base/type-def.mkiv
%{_texmfdistdir}/tex/context/base/type-exp.mkii
%{_texmfdistdir}/tex/context/base/type-fbk.mkiv
%{_texmfdistdir}/tex/context/base/type-fsf.mkii
%{_texmfdistdir}/tex/context/base/type-ghz.mkii
%{_texmfdistdir}/tex/context/base/type-hgz.mkii
%{_texmfdistdir}/tex/context/base/type-imp-antykwa.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-antykwapoltawskiego.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-asana.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-averia.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-buy.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-cambria.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-charter.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-cleartype.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-computer-modern-unicode.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-cow.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-dejavu.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-euler.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-ghz.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-hgz.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-husayni.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-hvmath.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-inconsolata.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-informal.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-iwona.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-kurier.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-latinmodern.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-liberation.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-libertine.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-lmnames.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-lucida-opentype.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-lucida-typeone.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-mathdesign.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-mathtimes.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-mscore.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-osx.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-postscript.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-punknova.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-texgyre.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-unfonts.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-xits.mkiv
%{_texmfdistdir}/tex/context/base/type-imp-xitsbidi.mkiv
%{_texmfdistdir}/tex/context/base/type-ini.lua
%{_texmfdistdir}/tex/context/base/type-ini.mkii
%{_texmfdistdir}/tex/context/base/type-ini.mkvi
%{_texmfdistdir}/tex/context/base/type-lua.mkiv
%{_texmfdistdir}/tex/context/base/type-mac.mkii
%{_texmfdistdir}/tex/context/base/type-msw.mkii
%{_texmfdistdir}/tex/context/base/type-one.mkii
%{_texmfdistdir}/tex/context/base/type-one.mkiv
%{_texmfdistdir}/tex/context/base/type-otf.mkii
%{_texmfdistdir}/tex/context/base/type-otf.mkiv
%{_texmfdistdir}/tex/context/base/type-pre.mkii
%{_texmfdistdir}/tex/context/base/type-run.mkii
%{_texmfdistdir}/tex/context/base/type-run.mkiv
%{_texmfdistdir}/tex/context/base/type-set.mkii
%{_texmfdistdir}/tex/context/base/type-set.mkiv
%{_texmfdistdir}/tex/context/base/type-siz.mkii
%{_texmfdistdir}/tex/context/base/type-siz.mkiv
%{_texmfdistdir}/tex/context/base/type-tmf.mkii
%{_texmfdistdir}/tex/context/base/type-tmf.mkiv
%{_texmfdistdir}/tex/context/base/type-win.mkii
%{_texmfdistdir}/tex/context/base/type-xtx.mkii
%{_texmfdistdir}/tex/context/base/typo-brk.lua
%{_texmfdistdir}/tex/context/base/typo-brk.mkiv
%{_texmfdistdir}/tex/context/base/typo-cap.lua
%{_texmfdistdir}/tex/context/base/typo-cap.mkiv
%{_texmfdistdir}/tex/context/base/typo-cln.lua
%{_texmfdistdir}/tex/context/base/typo-cln.mkiv
%{_texmfdistdir}/tex/context/base/typo-del.mkiv
%{_texmfdistdir}/tex/context/base/typo-dig.lua
%{_texmfdistdir}/tex/context/base/typo-dig.mkiv
%{_texmfdistdir}/tex/context/base/typo-dir.lua
%{_texmfdistdir}/tex/context/base/typo-dir.mkiv
%{_texmfdistdir}/tex/context/base/typo-ini.lua
%{_texmfdistdir}/tex/context/base/typo-ini.mkii
%{_texmfdistdir}/tex/context/base/typo-ini.mkiv
%{_texmfdistdir}/tex/context/base/typo-itc.lua
%{_texmfdistdir}/tex/context/base/typo-itc.mkvi
%{_texmfdistdir}/tex/context/base/typo-krn.lua
%{_texmfdistdir}/tex/context/base/typo-krn.mkiv
%{_texmfdistdir}/tex/context/base/typo-mar.lua
%{_texmfdistdir}/tex/context/base/typo-mar.mkiv
%{_texmfdistdir}/tex/context/base/typo-pag.lua
%{_texmfdistdir}/tex/context/base/typo-pag.mkiv
%{_texmfdistdir}/tex/context/base/typo-par.lua
%{_texmfdistdir}/tex/context/base/typo-par.mkiv
%{_texmfdistdir}/tex/context/base/typo-prc.lua
%{_texmfdistdir}/tex/context/base/typo-prc.mkvi
%{_texmfdistdir}/tex/context/base/typo-rep.lua
%{_texmfdistdir}/tex/context/base/typo-rep.mkiv
%{_texmfdistdir}/tex/context/base/typo-scr.mkiv
%{_texmfdistdir}/tex/context/base/typo-spa.lua
%{_texmfdistdir}/tex/context/base/typo-spa.mkiv
%{_texmfdistdir}/tex/context/base/typo-txt.mkvi
%{_texmfdistdir}/tex/context/base/unic-000.mkii
%{_texmfdistdir}/tex/context/base/unic-001.mkii
%{_texmfdistdir}/tex/context/base/unic-002.mkii
%{_texmfdistdir}/tex/context/base/unic-003.mkii
%{_texmfdistdir}/tex/context/base/unic-004.mkii
%{_texmfdistdir}/tex/context/base/unic-005.mkii
%{_texmfdistdir}/tex/context/base/unic-030.mkii
%{_texmfdistdir}/tex/context/base/unic-031.mkii
%{_texmfdistdir}/tex/context/base/unic-032.mkii
%{_texmfdistdir}/tex/context/base/unic-033.mkii
%{_texmfdistdir}/tex/context/base/unic-034.mkii
%{_texmfdistdir}/tex/context/base/unic-035.mkii
%{_texmfdistdir}/tex/context/base/unic-037.mkii
%{_texmfdistdir}/tex/context/base/unic-039.mkii
%{_texmfdistdir}/tex/context/base/unic-251.mkii
%{_texmfdistdir}/tex/context/base/unic-cjk.mkii
%{_texmfdistdir}/tex/context/base/unic-exp.mkii
%{_texmfdistdir}/tex/context/base/unic-ini.lua
%{_texmfdistdir}/tex/context/base/unic-ini.mkii
%{_texmfdistdir}/tex/context/base/unic-ini.mkiv
%{_texmfdistdir}/tex/context/base/unic-run.mkii
%{_texmfdistdir}/tex/context/base/util-deb.lua
%{_texmfdistdir}/tex/context/base/util-dim.lua
%{_texmfdistdir}/tex/context/base/util-fmt.lua
%{_texmfdistdir}/tex/context/base/util-lua.lua
%{_texmfdistdir}/tex/context/base/util-mrg.lua
%{_texmfdistdir}/tex/context/base/util-pck.lua
%{_texmfdistdir}/tex/context/base/util-prs.lua
%{_texmfdistdir}/tex/context/base/util-seq.lua
%{_texmfdistdir}/tex/context/base/util-sto.lua
%{_texmfdistdir}/tex/context/base/util-str.lua
%{_texmfdistdir}/tex/context/base/util-tab.lua
%{_texmfdistdir}/tex/context/base/verb-c.mkii
%{_texmfdistdir}/tex/context/base/verb-eif.mkii
%{_texmfdistdir}/tex/context/base/verb-ini.mkii
%{_texmfdistdir}/tex/context/base/verb-js.mkii
%{_texmfdistdir}/tex/context/base/verb-jv.mkii
%{_texmfdistdir}/tex/context/base/verb-mp.mkii
%{_texmfdistdir}/tex/context/base/verb-pas.mkii
%{_texmfdistdir}/tex/context/base/verb-pl.mkii
%{_texmfdistdir}/tex/context/base/verb-raw.mkii
%{_texmfdistdir}/tex/context/base/verb-sql.mkii
%{_texmfdistdir}/tex/context/base/verb-tex.mkii
%{_texmfdistdir}/tex/context/base/verb-xml.mkii
%{_texmfdistdir}/tex/context/base/x-asciimath.lua
%{_texmfdistdir}/tex/context/base/x-asciimath.mkiv
%{_texmfdistdir}/tex/context/base/x-calcmath.lua
%{_texmfdistdir}/tex/context/base/x-calcmath.mkii
%{_texmfdistdir}/tex/context/base/x-calcmath.mkiv
%{_texmfdistdir}/tex/context/base/x-cals.lua
%{_texmfdistdir}/tex/context/base/x-cals.mkiv
%{_texmfdistdir}/tex/context/base/x-chemml.lua
%{_texmfdistdir}/tex/context/base/x-chemml.mkii
%{_texmfdistdir}/tex/context/base/x-chemml.mkiv
%{_texmfdistdir}/tex/context/base/x-chemml.xsd
%{_texmfdistdir}/tex/context/base/x-contml.mkii
%{_texmfdistdir}/tex/context/base/x-contml.xsd
%{_texmfdistdir}/tex/context/base/x-corres.mkii
%{_texmfdistdir}/tex/context/base/x-corres.rng
%{_texmfdistdir}/tex/context/base/x-ct.lua
%{_texmfdistdir}/tex/context/base/x-ct.mkiv
%{_texmfdistdir}/tex/context/base/x-dir-01.tex
%{_texmfdistdir}/tex/context/base/x-dir-05.mkii
%{_texmfdistdir}/tex/context/base/x-dir-05.mkiv
%{_texmfdistdir}/tex/context/base/x-entities.mkiv
%{_texmfdistdir}/tex/context/base/x-fdf-00.mkii
%{_texmfdistdir}/tex/context/base/x-fe.mkii
%{_texmfdistdir}/tex/context/base/x-fig-00.dtd
%{_texmfdistdir}/tex/context/base/x-fig-00.mkii
%{_texmfdistdir}/tex/context/base/x-fig-00.xsd
%{_texmfdistdir}/tex/context/base/x-fig-01.mkii
%{_texmfdistdir}/tex/context/base/x-fig-02.mkii
%{_texmfdistdir}/tex/context/base/x-fig-03.mkii
%{_texmfdistdir}/tex/context/base/x-fo.mkii
%{_texmfdistdir}/tex/context/base/x-foxet.mkii
%{_texmfdistdir}/tex/context/base/x-foxet.mkiv
%{_texmfdistdir}/tex/context/base/x-ldx.ctx
%{_texmfdistdir}/tex/context/base/x-ldx.lua
%{_texmfdistdir}/tex/context/base/x-ldx.mkiv
%{_texmfdistdir}/tex/context/base/x-mathml.lua
%{_texmfdistdir}/tex/context/base/x-mathml.mkii
%{_texmfdistdir}/tex/context/base/x-mathml.mkiv
%{_texmfdistdir}/tex/context/base/x-mathml.xsd
%{_texmfdistdir}/tex/context/base/x-newcml.mkii
%{_texmfdistdir}/tex/context/base/x-newmme.mkii
%{_texmfdistdir}/tex/context/base/x-newmml.mkii
%{_texmfdistdir}/tex/context/base/x-newmml.mkiv
%{_texmfdistdir}/tex/context/base/x-newmmo.mkii
%{_texmfdistdir}/tex/context/base/x-newpml.mkii
%{_texmfdistdir}/tex/context/base/x-om2cml.xsl
%{_texmfdistdir}/tex/context/base/x-openmath.mkii
%{_texmfdistdir}/tex/context/base/x-openmath.xsl
%{_texmfdistdir}/tex/context/base/x-pfs-01.mkiv
%{_texmfdistdir}/tex/context/base/x-pfsense.ctx
%{_texmfdistdir}/tex/context/base/x-physml.mkii
%{_texmfdistdir}/tex/context/base/x-physml.mkiv
%{_texmfdistdir}/tex/context/base/x-physml.xsd
%{_texmfdistdir}/tex/context/base/x-res-00.mkii
%{_texmfdistdir}/tex/context/base/x-res-01.mkii
%{_texmfdistdir}/tex/context/base/x-res-01.mkiv
%{_texmfdistdir}/tex/context/base/x-res-02.mkii
%{_texmfdistdir}/tex/context/base/x-res-03.mkii
%{_texmfdistdir}/tex/context/base/x-res-04.mkii
%{_texmfdistdir}/tex/context/base/x-res-08.mkii
%{_texmfdistdir}/tex/context/base/x-res-09.mkii
%{_texmfdistdir}/tex/context/base/x-res-10.mkii
%{_texmfdistdir}/tex/context/base/x-res-11.mkii
%{_texmfdistdir}/tex/context/base/x-res-12.mkii
%{_texmfdistdir}/tex/context/base/x-res-20.mkii
%{_texmfdistdir}/tex/context/base/x-res-50.mkii
%{_texmfdistdir}/tex/context/base/x-res-50.mkiv
%{_texmfdistdir}/tex/context/base/x-sch-00.mkii
%{_texmfdistdir}/tex/context/base/x-sch-01.mkii
%{_texmfdistdir}/tex/context/base/x-set-01.mkii
%{_texmfdistdir}/tex/context/base/x-set-02.mkii
%{_texmfdistdir}/tex/context/base/x-set-11.mkii
%{_texmfdistdir}/tex/context/base/x-set-11.mkiv
%{_texmfdistdir}/tex/context/base/x-set-12.mkii
%{_texmfdistdir}/tex/context/base/x-set-12.mkiv
%{_texmfdistdir}/tex/context/base/x-sm2om.xsl
%{_texmfdistdir}/tex/context/base/x-steps.mkii
%{_texmfdistdir}/tex/context/base/x-udhr.mkiv
%{_texmfdistdir}/tex/context/base/x-xml-01.mkii
%{_texmfdistdir}/tex/context/base/x-xml-02.mkii
%{_texmfdistdir}/tex/context/base/x-xml-11.mkii
%{_texmfdistdir}/tex/context/base/x-xtag.mkiv
%{_texmfdistdir}/tex/context/base/xetx-chr.mkii
%{_texmfdistdir}/tex/context/base/xetx-cls.mkii
%{_texmfdistdir}/tex/context/base/xetx-ini.mkii
%{_texmfdistdir}/tex/context/base/xetx-utf.mkii
%{_texmfdistdir}/tex/context/base/xtag-cml.mkii
%{_texmfdistdir}/tex/context/base/xtag-ent.mkii
%{_texmfdistdir}/tex/context/base/xtag-exp.mkii
%{_texmfdistdir}/tex/context/base/xtag-ext.mkii
%{_texmfdistdir}/tex/context/base/xtag-hyp.mkii
%{_texmfdistdir}/tex/context/base/xtag-ini.mkii
%{_texmfdistdir}/tex/context/base/xtag-map.mkii
%{_texmfdistdir}/tex/context/base/xtag-mea.mkii
%{_texmfdistdir}/tex/context/base/xtag-meb.mkii
%{_texmfdistdir}/tex/context/base/xtag-mec.mkii
%{_texmfdistdir}/tex/context/base/xtag-meh.mkii
%{_texmfdistdir}/tex/context/base/xtag-men.mkii
%{_texmfdistdir}/tex/context/base/xtag-meo.mkii
%{_texmfdistdir}/tex/context/base/xtag-mer.mkii
%{_texmfdistdir}/tex/context/base/xtag-mmc.mkii
%{_texmfdistdir}/tex/context/base/xtag-mml.mkii
%{_texmfdistdir}/tex/context/base/xtag-mmp.mkii
%{_texmfdistdir}/tex/context/base/xtag-mxa.mkii
%{_texmfdistdir}/tex/context/base/xtag-mxb.mkii
%{_texmfdistdir}/tex/context/base/xtag-mxc.mkii
%{_texmfdistdir}/tex/context/base/xtag-mxh.mkii
%{_texmfdistdir}/tex/context/base/xtag-mxn.mkii
%{_texmfdistdir}/tex/context/base/xtag-mxo.mkii
%{_texmfdistdir}/tex/context/base/xtag-mxr.mkii
%{_texmfdistdir}/tex/context/base/xtag-pml.mkii
%{_texmfdistdir}/tex/context/base/xtag-pmu.mkii
%{_texmfdistdir}/tex/context/base/xtag-pre.mkii
%{_texmfdistdir}/tex/context/base/xtag-prs.mkii
%{_texmfdistdir}/tex/context/base/xtag-raw.mkii
%{_texmfdistdir}/tex/context/base/xtag-rng.mkii
%{_texmfdistdir}/tex/context/base/xtag-run.mkii
%{_texmfdistdir}/tex/context/base/xtag-stk.mkii
%{_texmfdistdir}/tex/context/base/xtag-utf.mkii
%{_texmfdistdir}/tex/context/base/xtag-xsd.mkii
%{_texmfdistdir}/tex/context/base/xtag-xsl.mkii
%{_texmfdistdir}/tex/context/bib/bibl-ams.tex
%{_texmfdistdir}/tex/context/bib/bibl-apa-de.tex
%{_texmfdistdir}/tex/context/bib/bibl-apa-fr.tex
%{_texmfdistdir}/tex/context/bib/bibl-apa.tex
%{_texmfdistdir}/tex/context/bib/bibl-aps.tex
%{_texmfdistdir}/tex/context/bib/bibl-num-fr.tex
%{_texmfdistdir}/tex/context/bib/bibl-num.tex
%{_texmfdistdir}/tex/context/bib/bibl-ssa.tex
%{_texmfdistdir}/tex/context/bib/sample.bib
%{_texmfdistdir}/tex/context/colors/icc/colorprofiles.lua
%{_texmfdistdir}/tex/context/colors/icc/colorprofiles.xml
%{_texmfdistdir}/tex/context/config/cont-de.ini
%{_texmfdistdir}/tex/context/config/cont-en.ini
%{_texmfdistdir}/tex/context/config/cont-fr.ini
%{_texmfdistdir}/tex/context/config/cont-it.ini
%{_texmfdistdir}/tex/context/config/cont-nl.ini
%{_texmfdistdir}/tex/context/config/cont-ro.ini
%{_texmfdistdir}/tex/context/extra/mag-0000.tex
%{_texmfdistdir}/tex/context/extra/setup-qr.tex
%{_texmfdistdir}/tex/context/extra/showunic.tex
%{_texmfdistdir}/tex/context/fonts/antykwa-math.lfg
%{_texmfdistdir}/tex/context/fonts/antykwapoltawskiego.lfg
%{_texmfdistdir}/tex/context/fonts/asana-math.lfg
%{_texmfdistdir}/tex/context/fonts/cambria-math.lfg
%{_texmfdistdir}/tex/context/fonts/charter-math.lfg
%{_texmfdistdir}/tex/context/fonts/demo.lfg
%{_texmfdistdir}/tex/context/fonts/dingbats.lfg
%{_texmfdistdir}/tex/context/fonts/garamond-math.lfg
%{_texmfdistdir}/tex/context/fonts/husayni.lfg
%{_texmfdistdir}/tex/context/fonts/hvmath-math.lfg
%{_texmfdistdir}/tex/context/fonts/informal-math.lfg
%{_texmfdistdir}/tex/context/fonts/iwona-math.lfg
%{_texmfdistdir}/tex/context/fonts/lm-math.lfg
%{_texmfdistdir}/tex/context/fonts/lm.lfg
%{_texmfdistdir}/tex/context/fonts/lucida-opentype-math.lfg
%{_texmfdistdir}/tex/context/fonts/lucida-typeone-math.lfg
%{_texmfdistdir}/tex/context/fonts/mathtimes-math.lfg
%{_texmfdistdir}/tex/context/fonts/px-math.lfg
%{_texmfdistdir}/tex/context/fonts/symbol-math.lfg
%{_texmfdistdir}/tex/context/fonts/tx-math.lfg
%{_texmfdistdir}/tex/context/fonts/utopia-math.lfg
%{_texmfdistdir}/tex/context/fonts/xits-math.lfg
%{_texmfdistdir}/tex/context/foxet/fe-bryson.xml
%{_texmfdistdir}/tex/context/foxet/fe-ward.xml
%{_texmfdistdir}/tex/context/foxet/fe-zapf.xml
%{_texmfdistdir}/tex/context/foxet/fo-0101.fo
%{_texmfdistdir}/tex/context/foxet/fo-0102.fo
%{_texmfdistdir}/tex/context/foxet/fo-0103.fo
%{_texmfdistdir}/tex/context/foxet/fo-0201.fo
%{_texmfdistdir}/tex/context/foxet/fo-0301.fo
%{_texmfdistdir}/tex/context/foxet/fo-0601.fo
%{_texmfdistdir}/tex/context/foxet/fo-0602.fo
%{_texmfdistdir}/tex/context/foxet/fo-0603.fo
%{_texmfdistdir}/tex/context/foxet/fo-0604.fo
%{_texmfdistdir}/tex/context/foxet/fo-0611.fo
%{_texmfdistdir}/tex/context/foxet/fo-0612.fo
%{_texmfdistdir}/tex/context/foxet/fo-0613.fo
%{_texmfdistdir}/tex/context/foxet/fo-0621.fo
%{_texmfdistdir}/tex/context/foxet/fo-0641.fo
%{_texmfdistdir}/tex/context/foxet/fo-0642.fo
%{_texmfdistdir}/tex/context/foxet/fo-0643.fo
%{_texmfdistdir}/tex/context/foxet/fo-0644.fo
%{_texmfdistdir}/tex/context/foxet/fo-0650.fo
%{_texmfdistdir}/tex/context/foxet/fo-0651.fo
%{_texmfdistdir}/tex/context/foxet/fo-0701.fo
%{_texmfdistdir}/tex/context/foxet/fo-0801.fo
%{_texmfdistdir}/tex/context/foxet/fo-0901.fo
%{_texmfdistdir}/tex/context/foxet/fo-0902.fo
%{_texmfdistdir}/tex/context/foxet/fo-1001.fo
%{_texmfdistdir}/tex/context/foxet/fo-1002.fo
%{_texmfdistdir}/tex/context/foxet/fo-1003.fo
%{_texmfdistdir}/tex/context/foxet/fo-1004.fo
%{_texmfdistdir}/tex/context/foxet/fo-1101.fo
%{_texmfdistdir}/tex/context/foxet/fo-1102.fo
%{_texmfdistdir}/tex/context/foxet/fo-1103.fo
%{_texmfdistdir}/tex/context/foxet/fo-1104.fo
%{_texmfdistdir}/tex/context/foxet/fo-1201.fo
%{_texmfdistdir}/tex/context/interface/cont-cs.xml
%{_texmfdistdir}/tex/context/interface/cont-de.xml
%{_texmfdistdir}/tex/context/interface/cont-en.xml
%{_texmfdistdir}/tex/context/interface/cont-fr.xml
%{_texmfdistdir}/tex/context/interface/cont-it.xml
%{_texmfdistdir}/tex/context/interface/cont-nl.xml
%{_texmfdistdir}/tex/context/interface/cont-pe.xml
%{_texmfdistdir}/tex/context/interface/cont-ro.xml
%{_texmfdistdir}/tex/context/interface/keys-cs.xml
%{_texmfdistdir}/tex/context/interface/keys-cz.xml
%{_texmfdistdir}/tex/context/interface/keys-de.xml
%{_texmfdistdir}/tex/context/interface/keys-en.xml
%{_texmfdistdir}/tex/context/interface/keys-fr.xml
%{_texmfdistdir}/tex/context/interface/keys-it.xml
%{_texmfdistdir}/tex/context/interface/keys-nl.xml
%{_texmfdistdir}/tex/context/interface/keys-pe.xml
%{_texmfdistdir}/tex/context/interface/keys-ro.xml
%{_texmfdistdir}/tex/context/patterns/lang-af.hyp
%{_texmfdistdir}/tex/context/patterns/lang-af.lua
%{_texmfdistdir}/tex/context/patterns/lang-af.pat
%{_texmfdistdir}/tex/context/patterns/lang-af.rme
%{_texmfdistdir}/tex/context/patterns/lang-agr.hyp
%{_texmfdistdir}/tex/context/patterns/lang-agr.lua
%{_texmfdistdir}/tex/context/patterns/lang-agr.pat
%{_texmfdistdir}/tex/context/patterns/lang-agr.rme
%{_texmfdistdir}/tex/context/patterns/lang-bg.hyp
%{_texmfdistdir}/tex/context/patterns/lang-bg.lua
%{_texmfdistdir}/tex/context/patterns/lang-bg.pat
%{_texmfdistdir}/tex/context/patterns/lang-bg.rme
%{_texmfdistdir}/tex/context/patterns/lang-ca.hyp
%{_texmfdistdir}/tex/context/patterns/lang-ca.lua
%{_texmfdistdir}/tex/context/patterns/lang-ca.pat
%{_texmfdistdir}/tex/context/patterns/lang-ca.rme
%{_texmfdistdir}/tex/context/patterns/lang-cs.hyp
%{_texmfdistdir}/tex/context/patterns/lang-cs.lua
%{_texmfdistdir}/tex/context/patterns/lang-cs.pat
%{_texmfdistdir}/tex/context/patterns/lang-cs.rme
%{_texmfdistdir}/tex/context/patterns/lang-cy.hyp
%{_texmfdistdir}/tex/context/patterns/lang-cy.lua
%{_texmfdistdir}/tex/context/patterns/lang-cy.pat
%{_texmfdistdir}/tex/context/patterns/lang-cy.rme
%{_texmfdistdir}/tex/context/patterns/lang-da.hyp
%{_texmfdistdir}/tex/context/patterns/lang-da.lua
%{_texmfdistdir}/tex/context/patterns/lang-da.pat
%{_texmfdistdir}/tex/context/patterns/lang-da.rme
%{_texmfdistdir}/tex/context/patterns/lang-de.hyp
%{_texmfdistdir}/tex/context/patterns/lang-de.lua
%{_texmfdistdir}/tex/context/patterns/lang-de.pat
%{_texmfdistdir}/tex/context/patterns/lang-de.rme
%{_texmfdistdir}/tex/context/patterns/lang-deo.hyp
%{_texmfdistdir}/tex/context/patterns/lang-deo.lua
%{_texmfdistdir}/tex/context/patterns/lang-deo.pat
%{_texmfdistdir}/tex/context/patterns/lang-deo.rme
%{_texmfdistdir}/tex/context/patterns/lang-es.hyp
%{_texmfdistdir}/tex/context/patterns/lang-es.lua
%{_texmfdistdir}/tex/context/patterns/lang-es.pat
%{_texmfdistdir}/tex/context/patterns/lang-es.rme
%{_texmfdistdir}/tex/context/patterns/lang-et.hyp
%{_texmfdistdir}/tex/context/patterns/lang-et.lua
%{_texmfdistdir}/tex/context/patterns/lang-et.pat
%{_texmfdistdir}/tex/context/patterns/lang-et.rme
%{_texmfdistdir}/tex/context/patterns/lang-eu.hyp
%{_texmfdistdir}/tex/context/patterns/lang-eu.lua
%{_texmfdistdir}/tex/context/patterns/lang-eu.pat
%{_texmfdistdir}/tex/context/patterns/lang-eu.rme
%{_texmfdistdir}/tex/context/patterns/lang-fi.hyp
%{_texmfdistdir}/tex/context/patterns/lang-fi.lua
%{_texmfdistdir}/tex/context/patterns/lang-fi.pat
%{_texmfdistdir}/tex/context/patterns/lang-fi.rme
%{_texmfdistdir}/tex/context/patterns/lang-fr.hyp
%{_texmfdistdir}/tex/context/patterns/lang-fr.lua
%{_texmfdistdir}/tex/context/patterns/lang-fr.pat
%{_texmfdistdir}/tex/context/patterns/lang-fr.rme
%{_texmfdistdir}/tex/context/patterns/lang-gb.hyp
%{_texmfdistdir}/tex/context/patterns/lang-gb.lua
%{_texmfdistdir}/tex/context/patterns/lang-gb.pat
%{_texmfdistdir}/tex/context/patterns/lang-gb.rme
%{_texmfdistdir}/tex/context/patterns/lang-hr.hyp
%{_texmfdistdir}/tex/context/patterns/lang-hr.lua
%{_texmfdistdir}/tex/context/patterns/lang-hr.pat
%{_texmfdistdir}/tex/context/patterns/lang-hr.rme
%{_texmfdistdir}/tex/context/patterns/lang-hu.hyp
%{_texmfdistdir}/tex/context/patterns/lang-hu.lua
%{_texmfdistdir}/tex/context/patterns/lang-hu.pat
%{_texmfdistdir}/tex/context/patterns/lang-hu.rme
%{_texmfdistdir}/tex/context/patterns/lang-is.hyp
%{_texmfdistdir}/tex/context/patterns/lang-is.lua
%{_texmfdistdir}/tex/context/patterns/lang-is.pat
%{_texmfdistdir}/tex/context/patterns/lang-is.rme
%{_texmfdistdir}/tex/context/patterns/lang-it.hyp
%{_texmfdistdir}/tex/context/patterns/lang-it.lua
%{_texmfdistdir}/tex/context/patterns/lang-it.pat
%{_texmfdistdir}/tex/context/patterns/lang-it.rme
%{_texmfdistdir}/tex/context/patterns/lang-la.hyp
%{_texmfdistdir}/tex/context/patterns/lang-la.lua
%{_texmfdistdir}/tex/context/patterns/lang-la.pat
%{_texmfdistdir}/tex/context/patterns/lang-la.rme
%{_texmfdistdir}/tex/context/patterns/lang-lt.hyp
%{_texmfdistdir}/tex/context/patterns/lang-lt.lua
%{_texmfdistdir}/tex/context/patterns/lang-lt.pat
%{_texmfdistdir}/tex/context/patterns/lang-lt.rme
%{_texmfdistdir}/tex/context/patterns/lang-lv.hyp
%{_texmfdistdir}/tex/context/patterns/lang-lv.lua
%{_texmfdistdir}/tex/context/patterns/lang-lv.pat
%{_texmfdistdir}/tex/context/patterns/lang-lv.rme
%{_texmfdistdir}/tex/context/patterns/lang-mn.hyp
%{_texmfdistdir}/tex/context/patterns/lang-mn.lua
%{_texmfdistdir}/tex/context/patterns/lang-mn.pat
%{_texmfdistdir}/tex/context/patterns/lang-mn.rme
%{_texmfdistdir}/tex/context/patterns/lang-nb.hyp
%{_texmfdistdir}/tex/context/patterns/lang-nb.lua
%{_texmfdistdir}/tex/context/patterns/lang-nb.pat
%{_texmfdistdir}/tex/context/patterns/lang-nb.rme
%{_texmfdistdir}/tex/context/patterns/lang-nl.hyp
%{_texmfdistdir}/tex/context/patterns/lang-nl.lua
%{_texmfdistdir}/tex/context/patterns/lang-nl.pat
%{_texmfdistdir}/tex/context/patterns/lang-nl.rme
%{_texmfdistdir}/tex/context/patterns/lang-nn.hyp
%{_texmfdistdir}/tex/context/patterns/lang-nn.lua
%{_texmfdistdir}/tex/context/patterns/lang-nn.pat
%{_texmfdistdir}/tex/context/patterns/lang-nn.rme
%{_texmfdistdir}/tex/context/patterns/lang-pl.hyp
%{_texmfdistdir}/tex/context/patterns/lang-pl.lua
%{_texmfdistdir}/tex/context/patterns/lang-pl.pat
%{_texmfdistdir}/tex/context/patterns/lang-pl.rme
%{_texmfdistdir}/tex/context/patterns/lang-pt.hyp
%{_texmfdistdir}/tex/context/patterns/lang-pt.lua
%{_texmfdistdir}/tex/context/patterns/lang-pt.pat
%{_texmfdistdir}/tex/context/patterns/lang-pt.rme
%{_texmfdistdir}/tex/context/patterns/lang-ro.hyp
%{_texmfdistdir}/tex/context/patterns/lang-ro.lua
%{_texmfdistdir}/tex/context/patterns/lang-ro.pat
%{_texmfdistdir}/tex/context/patterns/lang-ro.rme
%{_texmfdistdir}/tex/context/patterns/lang-ru.hyp
%{_texmfdistdir}/tex/context/patterns/lang-ru.lua
%{_texmfdistdir}/tex/context/patterns/lang-ru.pat
%{_texmfdistdir}/tex/context/patterns/lang-ru.rme
%{_texmfdistdir}/tex/context/patterns/lang-sk.hyp
%{_texmfdistdir}/tex/context/patterns/lang-sk.lua
%{_texmfdistdir}/tex/context/patterns/lang-sk.pat
%{_texmfdistdir}/tex/context/patterns/lang-sk.rme
%{_texmfdistdir}/tex/context/patterns/lang-sl.hyp
%{_texmfdistdir}/tex/context/patterns/lang-sl.lua
%{_texmfdistdir}/tex/context/patterns/lang-sl.pat
%{_texmfdistdir}/tex/context/patterns/lang-sl.rme
%{_texmfdistdir}/tex/context/patterns/lang-sr.hyp
%{_texmfdistdir}/tex/context/patterns/lang-sr.lua
%{_texmfdistdir}/tex/context/patterns/lang-sr.pat
%{_texmfdistdir}/tex/context/patterns/lang-sr.rme
%{_texmfdistdir}/tex/context/patterns/lang-sv.hyp
%{_texmfdistdir}/tex/context/patterns/lang-sv.lua
%{_texmfdistdir}/tex/context/patterns/lang-sv.pat
%{_texmfdistdir}/tex/context/patterns/lang-sv.rme
%{_texmfdistdir}/tex/context/patterns/lang-tk.hyp
%{_texmfdistdir}/tex/context/patterns/lang-tk.lua
%{_texmfdistdir}/tex/context/patterns/lang-tk.pat
%{_texmfdistdir}/tex/context/patterns/lang-tk.rme
%{_texmfdistdir}/tex/context/patterns/lang-tr.hyp
%{_texmfdistdir}/tex/context/patterns/lang-tr.lua
%{_texmfdistdir}/tex/context/patterns/lang-tr.pat
%{_texmfdistdir}/tex/context/patterns/lang-tr.rme
%{_texmfdistdir}/tex/context/patterns/lang-uk.hyp
%{_texmfdistdir}/tex/context/patterns/lang-uk.lua
%{_texmfdistdir}/tex/context/patterns/lang-uk.pat
%{_texmfdistdir}/tex/context/patterns/lang-uk.rme
%{_texmfdistdir}/tex/context/patterns/lang-us.hyp
%{_texmfdistdir}/tex/context/patterns/lang-us.lua
%{_texmfdistdir}/tex/context/patterns/lang-us.pat
%{_texmfdistdir}/tex/context/patterns/lang-us.rme
%{_texmfdistdir}/tex/context/patterns/lang-zh.hyp
%{_texmfdistdir}/tex/context/patterns/lang-zh.lua
%{_texmfdistdir}/tex/context/patterns/lang-zh.pat
%{_texmfdistdir}/tex/context/patterns/lang-zh.rme
%{_texmfdistdir}/tex/context/sample/aesop-de.tex
%{_texmfdistdir}/tex/context/sample/bryson.tex
%{_texmfdistdir}/tex/context/sample/cow.pdf
%{_texmfdistdir}/tex/context/sample/davis.tex
%{_texmfdistdir}/tex/context/sample/dawkins.tex
%{_texmfdistdir}/tex/context/sample/demo-mps.tex
%{_texmfdistdir}/tex/context/sample/demo-tex.tex
%{_texmfdistdir}/tex/context/sample/demo-xml.tex
%{_texmfdistdir}/tex/context/sample/douglas.tex
%{_texmfdistdir}/tex/context/sample/hacker.jpg
%{_texmfdistdir}/tex/context/sample/hawking.tex
%{_texmfdistdir}/tex/context/sample/khatt-ar.tex
%{_texmfdistdir}/tex/context/sample/khatt-en.tex
%{_texmfdistdir}/tex/context/sample/knuth.tex
%{_texmfdistdir}/tex/context/sample/linden.tex
%{_texmfdistdir}/tex/context/sample/materie.tex
%{_texmfdistdir}/tex/context/sample/mill.png
%{_texmfdistdir}/tex/context/sample/montgomery.tex
%{_texmfdistdir}/tex/context/sample/reich.tex
%{_texmfdistdir}/tex/context/sample/sample.tex
%{_texmfdistdir}/tex/context/sample/spider.eps
%{_texmfdistdir}/tex/context/sample/thuan.tex
%{_texmfdistdir}/tex/context/sample/tufte.tex
%{_texmfdistdir}/tex/context/sample/ward.tex
%{_texmfdistdir}/tex/context/sample/weisman.tex
%{_texmfdistdir}/tex/context/sample/zapf.tex
%{_texmfdistdir}/tex/context/test/context-test.tex
%{_texmfdistdir}/tex/context/test/pdf-a1a-2005.mkiv
%{_texmfdistdir}/tex/context/test/pdf-a1b-2005.mkiv
%{_texmfdistdir}/tex/context/test/pdf-x-common.mkiv
%{_texmfdistdir}/tex/context/test/pdf-x1a-2001.mkiv
%{_texmfdistdir}/tex/context/test/pdf-x1a-2003.mkiv
%{_texmfdistdir}/tex/context/test/pdf-x3-2002.mkiv
%{_texmfdistdir}/tex/context/test/pdf-x3-2003.mkiv
%{_texmfdistdir}/tex/context/test/pdf-x4.mkiv
%{_texmfdistdir}/tex/context/test/pdf-x4p.mkiv
%{_texmfdistdir}/tex/context/user/cont-sys.rme
%{_texmfdistdir}/tex/generic/context/luatex/luatex-basics-gen.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-basics-nod.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-basics.tex
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts-cbk.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts-def.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts-demo-vf-1.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts-enc.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts-ext.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts-lua.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts-merged.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts-syn.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts-tfm.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-fonts.tex
%{_texmfdistdir}/tex/generic/context/luatex/luatex-mplib.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-mplib.tex
%{_texmfdistdir}/tex/generic/context/luatex/luatex-plain.tex
%{_texmfdistdir}/tex/generic/context/luatex/luatex-preprocessor-test.tex
%{_texmfdistdir}/tex/generic/context/luatex/luatex-preprocessor.lua
%{_texmfdistdir}/tex/generic/context/luatex/luatex-preprocessor.tex
%{_texmfdistdir}/tex/generic/context/luatex/luatex-test.tex
%{_texmfdistdir}/tex/generic/context/ppchtex/m-ch-de.tex
%{_texmfdistdir}/tex/generic/context/ppchtex/m-ch-en.tex
%{_texmfdistdir}/tex/generic/context/ppchtex/m-ch-nl.tex
%{_texmfdistdir}/tex/generic/context/ppchtex/ppchtex.noc
%{_texmfdistdir}/tex/latex/context/ppchtex/m-ch-de.sty
%{_texmfdistdir}/tex/latex/context/ppchtex/m-ch-en.sty
%{_texmfdistdir}/tex/latex/context/ppchtex/m-ch-nl.sty
%{_texmfdistdir}/tex/latex/context/ppchtex/m-pictex.sty
%{_texmfdistdir}/tex/mptopdf/config/mptopdf.ini
%_texmf_fmtutil_d/context
%doc %{_texmfdistdir}/doc/context/bib/bibmod-doc.pdf
%doc %{_texmfdistdir}/doc/context/bib/bibmod-doc.tex
%doc %{_texmfdistdir}/doc/context/document/general/manuals/mreadme.pdf
%doc %{_texmfdistdir}/doc/context/document/general/manuals/tiptrick.pdf
%doc %{_texmfdistdir}/doc/context/manuals/allkind/mcommon.tex
%doc %{_texmfdistdir}/doc/context/manuals/allkind/mreadme.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/COPYING
%doc %{_texmfdistdir}/doc/context/manuals/reference/README
%doc %{_texmfdistdir}/doc/context/manuals/reference/TODO
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/Makefile
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/1x2xConference.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/1x2xConference.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/1x4.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/1x4.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/1x4xConference.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/1x4xConference.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/1x8.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/1x8.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2DOWN.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2DOWN.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2SIDE.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2SIDE.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2TOP.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2TOP.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2TOPSIDE.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2TOPSIDE.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2UP.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2UP.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x16.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x16.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x2.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x2.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x2x2.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x2x2.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x2x3.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x2x3.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x2x4.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x2x4.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x4.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x4.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x4x2-D.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x4x2-D.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x4x2.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x4x2.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x6xZ-HOR.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x6xZ-HOR.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x6xZ.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x6xZ.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x8-VER.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x8-VER.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x8.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x8.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x8xZ.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2x8xZ.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2xx.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2xx2.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/2xx2.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/3SIDE.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/3SIDE.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Doublewindow.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Doublewindow.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Mapflyer-12.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Mapflyer-12.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Tryptichon.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Tryptichon.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/XY.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/XY.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Zflyer-10.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Zflyer-10.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Zflyer-12.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Zflyer-12.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Zflyer-8.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/Zflyer-8.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/figures-base-file.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/test-arranging.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/arranging/test-arranging.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-backgrounds.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-blocks.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-colors.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-columns.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-descriptions.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-documents.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-figures.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-fonts.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-fonts.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-formulas.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-frames.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-interactive.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-introduction.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-language.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-layers.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-layout.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-metapost.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-modules.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-pagedesign.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-pagedesign.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-preface.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-references.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-tables.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-tabulate.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-textelements.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-typography.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-typography.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/co-verbatim.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/colbaltest.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-000.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-000.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-001.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-001.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-002.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-002.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-003.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-003.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-004.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-004.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-005.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-005.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-006.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-006.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-007.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-007.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-101.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-101.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-102.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-102.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-103.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-103.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-200.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-200.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-201.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-201.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-202.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-202.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-203.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-203.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-204.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-204.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-205.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-205.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-206.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-206.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-301.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-301.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-401.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-401.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-402.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-402.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-403.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-403.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-404.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-404.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-405.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-405.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-406.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-406.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-407.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-407.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-501.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-501.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-701.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-701.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-702.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-702.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-703.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-703.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-704.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-704.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-801.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-801.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-802.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-802.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-803.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-803.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-804.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-804.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-805.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-805.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-806.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cols-806.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/columns.rb
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/columns/cow.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/cont-en.xml
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/cont-xx.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/cont-yy.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/cont-zz.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/contextref-env.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/contextref.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/contextref.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/fonts/demofont.afm
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/fonts/demofont.dat
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/fonts/demofont.map
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/fonts/demofont.pfb
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/fonts/demofont.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/fonts/texnansi-test-test.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-1p.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-1q.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-2p.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-2q.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-3p.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-3q.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-4p.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-4q.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-5p.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-5q.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-6p.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-6q.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-7p.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pagedesign/co-en-7q.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pr-allfiles.lua
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pr-allfiles.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pr-copying.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/pr-texmfstart.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/s-abr-04.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/st-commands.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/st-contents.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/st-definitions.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/st-index.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/tables/registers-buffer.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/texmf.zip
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/typography/encodings.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/typography/encodings.tex
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/typography/glyphs.pdf
%doc %{_texmfdistdir}/doc/context/manuals/reference/en/typography/glyphs.tex
%doc %{_texmfdistdir}/doc/context/scripts/perl/texshow.1
%doc %{_texmfdistdir}/doc/context/scripts/perl/texshow.html
%doc %{_mandir}/man1/context.1*
%doc %{_texmfdir}/doc/man/man1/context.man1.pdf
%doc %{_mandir}/man1/ctxtools.1*
%doc %{_texmfdir}/doc/man/man1/ctxtools.man1.pdf
%doc %{_mandir}/man1/pstopdf.1*
%doc %{_texmfdir}/doc/man/man1/pstopdf.man1.pdf
%doc %{_mandir}/man1/texexec.1*
%doc %{_texmfdir}/doc/man/man1/texexec.man1.pdf
%doc %{_mandir}/man1/texmfstart.1*
%doc %{_texmfdir}/doc/man/man1/texmfstart.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
# only lua scripts
mkdir -p %{buildroot}%{_bindir}
cp -fpa bin/x86_64-linux/* %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/context <<EOF
#
# from context:
cont-en pdftex cont-usr.tex -8bit *cont-en.ini
cont-en xetex cont-usr.tex -8bit *cont-en.ini
#! cont-de pdftex cont-usr.tex -8bit *cont-de.ini
#! cont-fr pdftex cont-usr.tex -8bit *cont-fr.ini
#! cont-it pdftex cont-usr.tex -8bit *cont-it.ini
#! cont-nl pdftex cont-usr.tex -8bit *cont-nl.ini
#! cont-ro pdftex cont-usr.tex -8bit *cont-ro.ini
EOF
