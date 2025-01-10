import streamlit as st
from coffee.client import JsonApiClient
import sys
sys.path.append('/opt/anaconda3/envs/myenvtest/lib/python3.10/site-packages')
from coffee.workflows import ConstantPropertyWorkflow
import tempfile

# Title of the application
st.title("Constant Property Workflow - Bulk Link to Component Type")

# Header for the upload step
st.header("Step 1: Upload a CSV file")
uploaded_file = st.file_uploader("Upload a CSV file for linking constant property to Component Type", type=["csv"])

# Process the uploaded file
if uploaded_file is not None:
    st.write("Uploaded file:", uploaded_file.name)

    # Process the file when the user clicks the button
    if st.button("Process File"):
        try:
            # Write the uploaded file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_path = temp_file.name  # Temporary file path

            # Perform the workflow operation using the temporary file
            with JsonApiClient() as client:
                cp_workflow = ConstantPropertyWorkflow(client)
                cp_workflow.bulk_link_constant_property_to_component_type(temp_file_path)

            st.success("File processed and constant properties linked successfully!")
        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")
