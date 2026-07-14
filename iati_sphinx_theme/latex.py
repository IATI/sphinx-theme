"""LaTeX/PDF configuration for IATI Sphinx Theme.

This module provides default LaTeX styling for PDF output that applies
IATI branding. Projects using this theme will automatically get these
defaults, but can override any setting in their own conf.py.
"""

import os
from typing import Any

import sphinx.application
import sphinx.config


def get_latex_preamble() -> str:
    """Return the LaTeX preamble with IATI branding."""
    # Get the path to the logo
    theme_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(theme_dir, "static", "logo-colour.png")

    return (
        r"""
% IATI Brand Colors
\usepackage{xcolor}
\definecolor{iatiorange}{HTML}{DB584B}
\definecolor{iatiorange-light}{HTML}{FF7264}
\definecolor{iatiteal}{HTML}{155366}
\definecolor{iatiteal-light}{HTML}{448093}
\definecolor{iatigrey}{HTML}{121212}
\definecolor{iatigrey-light}{HTML}{686868}
\definecolor{iatigreen}{HTML}{0A9172}
\definecolor{iatipurple}{HTML}{6F3AAF}

% Page geometry
\usepackage{geometry}
\geometry{
    a4paper,
    margin=2.5cm,
    top=3cm,
    bottom=3cm
}

% Fonts (Hanken Grotesk / Nunito Sans / Roboto Mono) are loaded via the
% "fontpkg" LaTeX element - see get_latex_fontpkg(). They require XeLaTeX
% or LuaLaTeX, since fontspec cannot load .ttf files under pdfLaTeX.
% \sffamily below refers to the Hanken Grotesk heading font set there.
%
% Known cosmetic gap: Sphinx marks wrapped long lines in code blocks with
% U+2423 (OPEN BOX), which Roboto Mono doesn't include. LaTeX just skips
% the missing glyph (a "Missing character" warning, not an error), so
% wrapped code lines lose their wrap indicator but otherwise render fine.

% Header and footer styling
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\sffamily\textcolor{iatiorange}{\textbf{IATI}}}
\fancyhead[R]{\sffamily\textcolor{iatigrey-light}{\leftmark}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

% Chapter and section heading styling
\usepackage{titlesec}

\titleformat{\chapter}[display]
    {\normalfont\sffamily\huge\bfseries\color{iatiorange}}
    {\chaptertitlename\ \thechapter}
    {20pt}
    {\Huge}

\titleformat{\section}
    {\normalfont\sffamily\Large\bfseries\color{iatiteal}}
    {\thesection}
    {1em}
    {}

\titleformat{\subsection}
    {\normalfont\sffamily\large\bfseries\color{iatiteal}}
    {\thesubsection}
    {1em}
    {}

\titleformat{\subsubsection}
    {\normalfont\sffamily\normalsize\bfseries\color{iatigrey}}
    {\thesubsubsection}
    {1em}
    {}

% Hyperlink styling
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=iatiteal,
    urlcolor=iatiorange,
    citecolor=iatigreen
}

% Custom title page
% Sphinx's document classes call \sphinxmaketitle, not the standard
% \maketitle, so that's the command we need to override.
\makeatletter
\renewcommand{\sphinxmaketitle}{
    \begin{titlepage}
        \centering
        \vspace*{2cm}

        % Logo
        \IfFileExists{"""
        + logo_path.replace("\\", "/")
        + r"""}{
            \includegraphics[width=0.5\textwidth]{"""
        + logo_path.replace("\\", "/")
        + r"""}
        }{}

        \vspace{2cm}

        % Title
        {\sffamily\Huge\bfseries\color{iatiorange}\@title\par}

        \vspace{1cm}

        % Author/Release info
        {\Large\color{iatigrey}\@author\par}

        \vspace{0.5cm}

        {\large\color{iatigrey-light}\@date\par}

        \vfill

        % Footer text
        {\color{iatigrey-light}\textit{International Aid Transparency Initiative}\par}
    \end{titlepage}
}
\makeatother

% Table styling
\usepackage{booktabs}
\usepackage{array}
\renewcommand{\arraystretch}{1.3}

% Code block styling (via sphinxsetup in latex_elements)
"""
    )


def get_latex_fontpkg() -> str:
    """Return the "fontpkg" LaTeX element, loading IATI's brand fonts.

    Sphinx inserts this after loading fontspec itself (via the "fontenc"
    element, which it sets automatically for XeLaTeX/LuaLaTeX). It only
    has to bind font families to the files in fonts/ - it doesn't need to
    \\usepackage{fontspec} itself.
    """
    theme_dir = os.path.dirname(os.path.abspath(__file__))
    fonts_dir = os.path.join(theme_dir, "fonts")

    def font_path(family: str) -> str:
        return os.path.join(fonts_dir, family).replace("\\", "/") + "/"

    return (
        r"""
\setmainfont{NunitoSans}[
    Path = """
        + font_path("NunitoSans")
        + r""",
    Extension = .ttf,
    UprightFont = *-Regular,
    ItalicFont = *-Italic,
    BoldFont = *-Bold,
    BoldItalicFont = *-BoldItalic,
]
\setsansfont{HankenGrotesk}[
    Path = """
        + font_path("HankenGrotesk")
        + r""",
    Extension = .ttf,
    UprightFont = *-Regular,
    ItalicFont = *-Italic,
    BoldFont = *-Bold,
    BoldItalicFont = *-BoldItalic,
]
\setmonofont{RobotoMono}[
    Path = """
        + font_path("RobotoMono")
        + r""",
    Extension = .ttf,
    UprightFont = *-Regular,
    ItalicFont = *-Italic,
    BoldFont = *-Bold,
]
"""
    )


def get_latex_elements() -> dict[str, Any]:
    """Return the LaTeX elements configuration dictionary.

    Returns:
        Dictionary suitable for Sphinx's latex_elements configuration.
    """
    return {
        "papersize": "a4paper",
        "pointsize": "11pt",
        "preamble": get_latex_preamble(),
        "fontpkg": get_latex_fontpkg(),
        "fncychap": "",  # Disable default chapter styling, use custom
        "sphinxsetup": (
            # Admonition styling
            "noteBorderColor={RGB}{21,83,102},"  # iatiteal
            "noteborder=1pt,"
            "noteBgColor={RGB}{240,248,250},"
            "warningBorderColor={RGB}{219,88,75},"  # iatiorange
            "warningborder=1pt,"
            "warningBgColor={RGB}{255,245,244},"
            "tipBorderColor={RGB}{10,145,114},"  # iatigreen
            "tipborder=1pt,"
            "tipBgColor={RGB}{240,253,250},"
            "importantBorderColor={RGB}{111,58,175},"  # iatipurple
            "importantborder=1pt,"
            "importantBgColor={RGB}{248,244,253},"
            # Verbatim/code styling
            "VerbatimColor={RGB}{248,248,248},"
            "VerbatimBorderColor={RGB}{200,200,200},"
            "verbatimborder=0.5pt"
        ),
        # Babel language setting
        "babel": r"\usepackage[english]{babel}",
    }


def configure_latex_defaults(
    app: "sphinx.application.Sphinx", config: "sphinx.config.Config"
) -> None:
    """Configure default LaTeX elements for IATI branding.

    This is called during the 'config-inited' event. It sets default
    values for latex_elements while allowing user overrides.

    Args:
        app: The Sphinx application instance.
        config: The Sphinx configuration object.
    """
    # Our brand fonts are loaded via fontspec, which only runs under
    # XeLaTeX/LuaLaTeX. Default to xelatex unless a project has already
    # chosen an engine other than Sphinx's own pdflatex default.
    if config.latex_engine == "pdflatex":
        config.latex_engine = "xelatex"

    theme_defaults = get_latex_elements()

    # Get user's existing latex_elements or create empty dict
    # Note: At config-inited time, latex_elements may be an empty dict {}
    user_elements = dict(config.latex_elements) if config.latex_elements else {}

    # Merge defaults with user config (user config takes precedence)
    merged = {}
    for key, value in theme_defaults.items():
        if key not in user_elements:
            merged[key] = value
        elif key == "preamble":
            # For preamble, prepend theme defaults to user's preamble
            # so user can override/extend
            user_preamble = user_elements.get("preamble", "")
            merged["preamble"] = value + "\n" + user_preamble
        elif key == "sphinxsetup":
            # For sphinxsetup, append user's settings to theme defaults
            user_setup = user_elements.get("sphinxsetup", "")
            if user_setup:
                merged["sphinxsetup"] = value + "," + user_setup
            else:
                merged[key] = value
        else:
            merged[key] = user_elements[key]

    # Copy over any user settings we didn't touch
    for key, value in user_elements.items():
        if key not in merged:
            merged[key] = value

    # Update the config - update in place rather than replacing
    # This ensures the changes persist in Sphinx's config system
    config.latex_elements.clear()
    config.latex_elements.update(merged)


def setup(app: "sphinx.application.Sphinx") -> None:
    """Set up the LaTeX configuration extension.

    This function is called if this module is loaded as a Sphinx extension.

    Args:
        app: The Sphinx application instance.
    """
    app.connect("config-inited", configure_latex_defaults)
