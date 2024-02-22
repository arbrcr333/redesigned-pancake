import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# App title
st.title('Data Visualization App')

# Sidebar for user input features
st.sidebar.header('Upload your CSV data')
uploaded_file = st.sidebar.file_uploader("Choose a file", type=['csv'])

# Function to load the data
@st.cache_data
def load_data(file):
    if file is not None:
        df = pd.read_csv(file)
        return df
    else:
        return pd.DataFrame()

# Load the data
df = load_data(uploaded_file)

# Display the dataframe
if not df.empty:
    st.write(df)

    # Selectbox for type of plot
    plot_type = st.sidebar.selectbox('Select the type of plot', ['Line Chart', 'Bar Graph', 'Scatter Plot', 'Heatmap'])

    # Plotting based on user selection
    if plot_type == 'Line Chart':
        st.subheader('Line Chart')
        selected_columns = st.multiselect('Select columns to plot', df.columns)
        if len(selected_columns) >= 1:
            st.line_chart(df[selected_columns])
    
    elif plot_type == 'Bar Graph':
        st.subheader('Bar Graph')
        x_axis = st.selectbox('Choose a column for the X-axis:', df.columns)
        y_axis = st.selectbox('Choose a column for the Y-axis:', df.columns)
        st.bar_chart(df[[x_axis, y_axis]])

    elif plot_type == 'Scatter Plot':
        st.subheader('Scatter Plot')
        x_axis = st.selectbox('Choose a column for the X-axis:', df.columns, index=0)
        y_axis = st.selectbox('Choose a column for the Y-axis:', df.columns, index=1)
        fig = px.scatter(df, x=x_axis, y=y_axis)
        st.plotly_chart(fig)

    elif plot_type == 'Heatmap':
        st.subheader('Heatmap')
        corr = df.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, ax=ax)
        st.pyplot(fig)

else:
    st.write("Please upload a CSV file to visualize data.")
