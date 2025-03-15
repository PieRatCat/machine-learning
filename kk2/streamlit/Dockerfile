FROM streamlit/streamlit:latest

# Set the working directory
WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model file and application files
COPY xgb_model_mnist.pkl .
COPY . .

# Explicitly set permissions (just in case)
RUN chmod 644 xgb_model_mnist.pkl

# Verify current working directory and file listing
RUN pwd && ls -l

# Run the Streamlit application
CMD ["streamlit", "run", "streamlit_app.py"]