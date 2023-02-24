import pandas as pd 
import streamlit as st

class Home:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        st.title("Quant SC Game Theory") 

        st.write("OpenRML is a free and open-source tool for data analysis and machine learning.")
        st.write("## Getting Started")
        st.write("To get started, upload a dataset using the sidebar.")

        
if __name__ == "__main__":
    web = Home()
    web.run()