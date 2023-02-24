import streamlit as st

def mixed_strategies() -> None:
    st.set_page_config(page_title="Column Summaries", page_icon="📊")

    st.markdown("# Mixed Strategy Tests")
    st.sidebar.header("Mixed Strategy Tests")
    st.sidebar.write("""This demo gives statistics for each column of the dataframe.""")

    st.markdown("## Normal Form Game Solver")

    st.markdown("## Extensive Form Game Solver")

    st.markdown("## Linear Programming Solver")

if __name__ == "__main__":
    mixed_strategies()