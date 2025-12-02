# 1. Select the base operating system (Base Image)
# Use the slim version of Python 3.9 for lightness
FROM python:3.9-slim

#2. Create working directory in container
WORKDIR /app

# 3. Copy file requirements.txt into the container
COPY requirements.txt .

# 4. Install necessary libraries (Streamlit) inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all code (app.py) into the container
COPY . .

# 6. Open port 8501 (Default port for Streamlit)
EXPOSE 8501

# 7. Command to run when the container starts
# Note: address=0.0.0.0 is required to run inside Docker
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]