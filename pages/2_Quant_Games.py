import streamlit as st

def quant_games():
    st.set_page_config(page_title="Data Summary", page_icon="📊")

    st.markdown("# Quant Games")
    st.sidebar.header("Quant Games")
    st.sidebar.write(
        """This demo gives statistics for the dataset as a whole"""
    )

    st.write("## Fix It Game")  
    st.write("## Pit Game")

if __name__ == "__main__":
    quant_games()