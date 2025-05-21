from __future__ import annotations

from pathlib import Path

import gettext

TYPE_CHECKING = False
if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata

__version__ = "2025.4.1"

THEME_PATH = Path(__file__).resolve().parent


def _setup_translations(app):
    language = app.config.language or 'en'
    try:
        translation = gettext.translation(domain="messages", localedir=str(THEME_PATH / "locales"), languages=[language])
        app.builder.templates.environment.install_gettext_translations(translation, newstyle=True)
    except FileNotFoundError:
        app.builder.templates.environment.install_gettext(lambda x: x, newstyle=True)


def setup(app: Sphinx) -> ExtensionMetadata:
    app.require_sphinx("7.3")

    app.add_html_theme("python_docs_theme", str(THEME_PATH))
    app.connect("builder-inited", _setup_translations)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
