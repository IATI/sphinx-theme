===========
PDF styling
===========

PDF builds and HTML are styled completely separately: the website is styled with CSS, and the PDF is styled with `LaTeX <https://www.latex-project.org/>`_, a typesetting system with its own syntax. This page is a primer on how that works for anyone working on this theme who hasn't used LaTeX before.

The PDF-specific configuration lives in :code:`iati_sphinx_theme/latex.py`.

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

:code:`latex.py` incorporates styling from the IATI design system. Most of it - the brand colours and the logo - is derived from the design system automatically at build time (see `Keeping in sync with the design system`_ below). The fonts are the one deliberate exception.

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

These :code:`\definecolor` lines are generated from the design system's colour tokens at build time (see `Keeping in sync with the design system`_).

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

LaTeX's manual/report document classes default to book-style layout, but these PDFs are downloaded and read on a screen, so this line sets that up: :code:`oneside` keeps margins identical on every page, and :code:`openany` lets chapters start on the very next page instead of skipping one to land on an odd page number.

This is set via Sphinx's :code:`extraclassoptions` :code:`latex_elements` key (passed as document class options) rather than the raw preamble, since by the time the preamble runs, the document class has already been loaded with its default options.

Brand fonts
-----------

.. code-block:: latex

    \setmainfont{NunitoSans}[...]
    \setsansfont{HankenGrotesk}[...]
    \setmonofont{RobotoMono}[...]

These are the brand fonts: Nunito Sans for body text; Hanken Grotesk for headings; Roboto Mono for code; provided by the :code:`.ttf` files shipped in :code:`iati_sphinx_theme/fonts/`.

Unlike the colours and logo, these font files are committed to the repository rather than pulled from Google Fonts at build time to ensure that there's always a local font file on disk for LaTeX to use. See `Keeping in sync with the design system`_.

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

This configures the title page to have a logo, a coloured title, and the author/date.

:code:`\@title` and :code:`\@author` aren't hardcoded - they come from Sphinx's :code:`latex_documents` setting. In the standardised IATI setup the :code:`conf.py` holding :code:`latex_documents` is synced identically across repos, so it derives those values from the project's :code:`project_info.py` (the :code:`project` name and author) rather than having anyone hand-edit :code:`conf.py`. (:code:`\@date` isn't part of :code:`latex_documents` - it defaults to the build date.) So every project gets its own cover with the shared IATI look.

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

SVG images
==========

Sphinx's LaTeX builder only accepts PDF, PNG and JPEG images, so an SVG referenced in your docs is silently dropped from the PDF - even though it renders fine on the website. To avoid that, the theme registers the :code:`sphinxcontrib.rsvgconverter` extension automatically (in :code:`iati_sphinx_theme/__init__.py`), which converts SVGs to PDF - as crisp vectors - during the PDF build using the :code:`rsvg-convert` tool from librsvg.

The upshot: you can use SVG images in your docs and they render in both HTML and PDF, with no need to keep a separate PNG copy.

**System requirement.** :code:`rsvg-convert` must be present in the build environment:

- Read the Docs - add it via :code:`build.apt_packages` in :code:`.readthedocs.yaml`:

  .. code-block:: yaml

      build:
        apt_packages:
          - librsvg2-bin

- Local, Debian/Ubuntu (including the devcontainer) - :code:`apt-get install librsvg2-bin`.
- Local, macOS - :code:`brew install librsvg`.

If :code:`rsvg-convert` is missing, SVGs are simply skipped in the PDF (with a warning), exactly as before - HTML builds are never affected.

.. note::
    Consumer sites get the extension automatically from the theme (it's a theme dependency, and the theme registers it - no :code:`conf.py` change needed). Each site only needs to install :code:`librsvg2-bin` in its own build environments: its :code:`.readthedocs.yaml` and its devcontainer.

Keeping in sync with the design system
========================================

The HTML theme consumes the `IATI design system <https://github.com/IATI/iati-design-system>`_ directly: it's an npm dependency, pinned in :code:`package.json`, and the CSS is compiled from it by :code:`npm run build`. The PDF pipeline needs the same branding, but in forms LaTeX can use - colours as hex codes, the logo as a raster image - so rather than hand-copying them (where they drift out of sync), it derives them from the *same pinned design system* at build time.

:code:`scripts/generate-brand-assets.mjs`, which runs as part of :code:`npm run build`, produces:

- :code:`iati_sphinx_theme/_generated/brand_colors.json` - the brand colours, read from the design system's :code:`tokens/_color.scss`. :code:`latex.py` reads this to emit the :code:`\definecolor` lines and the admonition border colours.
- :code:`iati_sphinx_theme/static/logo-colour.svg` and :code:`logo-colour.png` - copied and rasterised from the design system's logo SVG. The HTML header uses the SVG; the PDF title page uses the PNG. (SVG images in docs *content* are converted to PDF automatically - see `SVG images`_ - but the title-page logo deliberately uses the pre-rasterised PNG.)

These are gitignored build artifacts, exactly like the compiled CSS - they aren't committed to this repository. They're regenerated wherever the CSS already is: local development, Read the Docs (in its :code:`pre_install` step), and the PyPI publish workflow (before :code:`python -m build`, so they're baked into the released package).

**The pinned version is the unit of sync.** Builds are reproducible against whatever :code:`iati-design-system` version is pinned in :code:`package.json`; brand values only change when someone bumps that pin deliberately - the same moment the CSS would change. To adopt design-system updates, bump the pin and rebuild.

To catch the design system moving ahead of the pin, the :code:`.github/workflows/design-system-drift.yml` workflow runs on a schedule: it regenerates the brand assets against the latest published :code:`iati-design-system` and fails (with a warning annotation) if the colours or logo would differ from the pinned version, as a prompt to bump the pin.

The fonts are the exception to all of this - see `Brand fonts`_ for why they're vendored rather than generated.

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
