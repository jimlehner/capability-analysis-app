import streamlit as st
from pathlib import Path

from pathlib import Path
import streamlit as st

from pathlib import Path
import streamlit as st


def render_markdown_with_figures(content):
    figures = {
        "[FIGURE_1]": {
            "path": "figures/Fig_capability_ratio.png",
            "caption": "Figure 1. Capability ratio."
        },
        "[FIGURE_2]": {
            "path": "figures/Fig_centered_capability_ratio.png",
            "caption": "Figure 2. Centered capability ratio."
        },
        "[FIGURE_3]": {
            "path": "figures/Fig_performance_ratio.png",
            "caption": "Figure 3. Performance ratios."
        },
        "[FIGURE_4]": {
            "path": "figures/Fig_centered_performance_ratio.png",
            "caption": "Figure 3. Performance ratios."
        },
    }

    parts = content.split("\n\n")

    for part in parts:
        part = part.strip()

        if not part:
            continue

        if part in figures:
            figure = figures[part]

            st.image(
                figure["path"],
                use_container_width=True,
                caption=figure["caption"]
            )
        else:
            st.markdown(part)


def display_index_overview():
    content_path = Path("content/capability_index_overview.md")
    content = content_path.read_text(encoding="utf-8")

    before, remainder = content.split("[CAPABILITY_RATIOS]", 1)

    capability_content, performance_content = remainder.split(
        "[PERFORMANCE_RATIOS]", 1
    )

    if before.strip():
        st.markdown(before.strip())

    col1, col2 = st.columns(2)

    with col1:
        render_markdown_with_figures(capability_content)

    with col2:
        render_markdown_with_figures(performance_content)
