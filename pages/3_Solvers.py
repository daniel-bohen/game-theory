import streamlit as st

def solvers() -> None:
    st.set_page_config(page_title="Column Summaries", page_icon="📊")

    st.markdown("# Game Theory Solvers")
    st.sidebar.header("Game Theory Solvers")
    st.sidebar.write("""This demo gives statistics for each column of the dataframe.""")

    st.markdown("## Normal Form Game Solver")

    st.markdown("## Extensive Form Game Solver")

    st.markdown("## Linear Programming Solver")

if __name__ == "__main__":
    solvers()