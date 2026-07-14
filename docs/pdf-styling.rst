===========
PDF styling
===========

PDF builds and HTML are styled completely separately: the website is styled with CSS, and the PDF is styled with `LaTeX <https://www.latex-project.org/>`_, a widely-used typesetting system with its own syntax. This page is a primer on how that works, aimed at anyone working on this theme who hasn't used LaTeX before.

All of the PDF-specific configuration lives in :code:`iati_sphinx_theme/latex.py`.

How PDF output works
=====================

Building the website and building a PDF share the first step, then diverge completely:

1. Sphinx reads your :code:`.rst` files.
2. Sphinx then writes out a :code:`.tex` file: a plain-text document full of :code:`\commands`.
3. A LaTeX *engine* - a separate program - reads that :code:`.tex` file and lays out the actual PDF pages.

:code:`latex.py` only touches step 2. It doesn't write any of your content - it injects a block of setup commands, called a **preamble**, before Sphinx's generated content.

A handful of LaTeX terms cover almost everything in that preamble:

.. list-table::
    :header-rows: 1

    * - Term
      - What it means
    * - preamble
      - The setup block before real content starts. Anything defined here - a colour, a font, a page margin - applies for the rest of the document.
    * - :code:`\usepackage{x}`
      - An import. LaTeX ships with a small core; almost everything useful (colour, custom headers, hyperlinks, tidy tables) comes from a package you opt into by name.
    * - :code:`\command{}[]`
      - A function call. Curly braces :code:`{}` are required arguments; square brackets :code:`[]` are optional ones. :code:`\definecolor{iatiorange}{HTML}{DB584B}` reads as "define a colour named :code:`iatiorange`, from an HTML hex code, equal to :code:`DB584B`."
    * - :code:`\renewcommand`
      - Overrides a command LaTeX (or a package) already defines.
    * - engine
      - The program that actually compiles the :code:`.tex` file into a PDF. Sphinx defaults to :code:`pdflatex`; this theme changes that default (see `Building PDFs locally`_).

What :code:`latex.py` configures
==================================

:code:`latex.py` incorporates styling from the IATI design system, but there is no automatic link: if any of these aspects are changed in the design system they must be updated in the theme separately. 

Brand colours
--------------

.. code-block:: latex

    \usepackage{xcolor}
    \definecolor{iatiorange}{HTML}{DB584B}
    \definecolor{iatiteal}{HTML}{155366}
    \definecolor{iatigrey}{HTML}{121212}
    \definecolor{iatigreen}{HTML}{0A9172}
    \definecolor{iatipurple}{HTML}{6F3AAF}

Same idea as CSS custom properties: each brand colour is defined once, then used by name in every block below instead of repeating hex codes.

Page geometry
-------------

.. code-block:: latex

    \usepackage{geometry}
    \geometry{
        a4paper,
        margin=2.5cm,
        top=3cm,
        bottom=3cm
    }

Sets the paper size and the white space around content.

Document layout
----------------

.. code-block:: python

    "extraclassoptions": "oneside,openany"

LaTeX's manual/report document classes default to book-style layout: two-sided margins that mirror left/right for binding, and chapters forced to always start on a right-hand page (inserting a blank page when needed to get there). That makes sense for something printed and bound, but these PDFs are downloaded and read on a screen, so this theme opts out of both - :code:`oneside` keeps margins identical on every page, and :code:`openany` lets chapters start on the very next page instead of skipping one to land on an odd page number.

This is set via Sphinx's :code:`extraclassoptions` :code:`latex_elements` key (passed as document class options) rather than the raw preamble, since by the time the preamble runs, the document class has already been loaded with its default options.

Brand fonts
-----------

.. code-block:: latex

    \setmainfont{NunitoSans}[...]
    \setsansfont{HankenGrotesk}[...]
    \setmonofont{RobotoMono}[...]

This binds the same three fonts the website uses - Nunito Sans for body text, Hanken Grotesk for headings, Roboto Mono for code - to the :code:`.ttf` files shipped in :code:`iati_sphinx_theme/fonts/`.

It's set via Sphinx's :code:`fontpkg` :code:`latex_elements` key rather than the raw preamble, since Sphinx already loads the ``fontspec`` package itself (as part of its own :code:`fontenc` handling) when the engine is XeLaTeX or LuaLaTeX. :code:`fontpkg` just needs to say *which* fonts to use.

Headings use :code:`\sffamily` to switch to Hanken Grotesk, since :code:`\setsansfont` binds a font to LaTeX's existing "sans family" concept rather than introducing a new command.

.. note::
    ``fontspec`` (and therefore these brand fonts) only works under the XeLaTeX or LuaLaTeX engines, not the default ``pdflatex`` - see `Building PDFs locally`_.

Header and footer
------------------

.. code-block:: latex

    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \fancyhf{}
    \fancyhead[L]{\sffamily\textcolor{iatiorange}{\textbf{IATI}}}
    \fancyhead[R]{\sffamily\textcolor{iatigrey-light}{\leftmark}}
    \fancyfoot[C]{\thepage}

:code:`[L]`, :code:`[R]` and :code:`[C]` mean left, right and centre. :code:`\leftmark` is a LaTeX built-in that always resolves to the current chapter's title, so chapter names in the header stay in sync automatically.

Chapter and section headings
------------------------------

.. code-block:: latex

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

Chapters are large and orange; sections and subsections step down in size and switch to teal - the same hierarchy as the HTML theme, expressed in LaTeX's more verbose syntax.

Hyperlinks
----------

.. code-block:: latex

    \usepackage{hyperref}
    \hypersetup{
        colorlinks=true,
        linkcolor=iatiteal,
        urlcolor=iatiorange,
        citecolor=iatigreen
    }

Internal cross-references are teal, external URLs are orange, citations are green.

Custom title page
-----------------

.. code-block:: latex

    \renewcommand{\sphinxmaketitle}{
        \begin{titlepage}
            \centering
            \includegraphics[width=0.5\textwidth]{logo-colour.png}
            {\sffamily\Huge\bfseries\color{iatiorange}\@title\par}
            {\Large\color{iatigrey}\@author\par}
            {\large\color{iatigrey-light}\@date\par}
        \end{titlepage}
    }

Every LaTeX document has a default, plain title page. This throws it away and draws a logo, a coloured title, and the author/date instead.

:code:`\@title`, :code:`\@author` and :code:`\@date` aren't hardcoded - they come from whatever Sphinx's :code:`latex_documents` setting in the project's :code:`conf.py` supplied, so every project gets its own cover with the shared IATI look.

.. important::
    This has to override :code:`\sphinxmaketitle`, **not** the standard :code:`\maketitle` command. Sphinx's document classes call :code:`\sphinxmaketitle` directly and never call plain :code:`\maketitle`, so a :code:`\renewcommand{\maketitle}{...}` here would silently have no effect at all - which is exactly what happened until this was caught.

Tables, code blocks and admonitions
-------------------------------------

.. code-block:: latex

    \usepackage{booktabs}
    \renewcommand{\arraystretch}{1.3}

The rest is set via Sphinx's :code:`sphinxsetup` element rather than raw LaTeX: nicer table rules, and colour-coded borders/backgrounds for :code:`.. note::`, :code:`.. warning::`, :code:`.. tip::` and :code:`.. important::` blocks, matching the same four brand colours used everywhere else in this document.

How it's wired into Sphinx
============================

:code:`latex.py` doesn't run on its own - :code:`iati_sphinx_theme/__init__.py` connects its :code:`configure_latex_defaults` function to Sphinx's :code:`config-inited` event, a point early in the build where every project's :code:`conf.py` has just finished executing, but nothing has been generated yet.

That function merges the theme's defaults into whatever :code:`latex_elements` a project already set, without clobbering it:

- If a project's :code:`conf.py` already sets a given :code:`latex_elements` key, the project's value wins outright.
- The :code:`preamble` key is the exception: the theme's preamble is *prepended* to the project's, so a project can add its own LaTeX underneath the branding without losing it.
- Likewise, a project's :code:`sphinxsetup` string is *appended* to the theme's.

The same function also switches the default :code:`latex_engine` from Sphinx's own default (:code:`pdflatex`) to :code:`lualatex`, but only if a project hasn't already chosen a different engine - see below.

Building PDFs locally
=======================

.. code-block:: none

    make -C docs latexpdf

This requires a LaTeX distribution (for example `TeX Live <https://tug.org/texlive/>`_) that includes the ``lualatex`` engine, since the brand fonts depend on the ``fontspec`` package, which only works under XeLaTeX or LuaLaTeX - not the ``pdflatex`` engine Sphinx uses by default. This theme sets the default engine to ``lualatex`` automatically, so no extra configuration is needed in a project's ``conf.py``.

.. note::
    Of the two ``fontspec``-compatible engines, this theme picks ``lualatex`` over ``xelatex``: Sphinx's mechanism for force-wrapping long unbroken tokens (URLs, in particular) inside code blocks silently fails under XeLaTeX, letting them overflow the page instead of wrapping. The same content wraps correctly under LuaLaTeX.

Known limitations
===================

.. warning::
    Sphinx marks wrapped long lines in code blocks with a special character (U+2423, "open box"), which Roboto Mono doesn't include. LaTeX skips the missing glyph with a warning rather than failing the build, so wrapped code lines just lose that wrap indicator.
