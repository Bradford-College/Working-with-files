import json
import streamlit as st # type: ignore
from readfile import read_file
import pandas as pd

file_path = 'users.json'

data = read_file(file_path)
st.table(data)
st.sidebar.title('Side Bar')

import pandas as pd

df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)