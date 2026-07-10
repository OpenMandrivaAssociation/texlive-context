%global tl_name context
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2026~07~06.1329.A
Release:	%{tl_revision}.1
Summary:	The ConTeXt macro package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/base
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(context.bin)
Requires:	texlive(dejavu)
Requires:	texlive(lm)
Requires:	texlive(lm-math)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A full featured, parameter driven macro package, which fully supports
advanced interactive documents. See the ConTeXt Wiki for more
information. This content on CTAN is packaged independently of the
ConTeXt project, so if you have a problem with ConTeXt itself, it is
best to report it to the official ntg-context@ntg.nl mailing list. If
you notice that ConTeXt is mispackaged in TeX Live or CTAN, then please
open a new issue on GitHub, email the public ntg-context@ntg.nl or tex-
live@tug.org mailing lists, or email me privately at tex@maxchernoff.ca.
Pull requests are also gladly accepted.

