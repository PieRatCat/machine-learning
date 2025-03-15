FROM streamlit/streamlit:latest

RUN apt-get update && apt-get install -y \
    libgl1 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    mesa-utils \
    libx11-6 \
    python3-opencv

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python3 -c "import cv2; print(cv2.__version__)"

COPY . .

CMD ["streamlit", "run", "streamlit_app.py"]

