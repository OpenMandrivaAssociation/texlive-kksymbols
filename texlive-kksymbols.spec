%global tl_name kksymbols
%global tl_revision 79445

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2.1
Release:	%{tl_revision}.1
Summary:	LaTeX commands for enclosing characters in circles, squares, diamonds, or bra...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/kksymbols
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kksymbols.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kksymbols.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers LaTeX commands for enclosing characters in circles,
squares, diamonds, or brackets, with automatic scaling and baseline
correction to ensure correct appearance in both horizontal and vertical
writing modes. The package relies on TikZ and works only with LuaLaTeX.

