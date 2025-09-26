!pip install streamlit
import streamlit as st
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

# Example: load your model if saved
# model = PipelineModel.load("path_to_saved_model")

# For demonstration, assume predictions DataFrame exists
st.title("Real-Time News Sentiment")
st.table(predictions.select("headline", "prediction").toPandas())
