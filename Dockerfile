# ── Build stage ──────────────────────────────────────────────────────────────
FROM python:3.11-slim

# Metadata
LABEL maintainer="B.J. Navadeep"
LABEL description="AI-Powered Sustainable Predictive Maintenance System"

# Set working directory
WORKDIR /app

# Install dependencies first (cached layer — only rebuilds if requirements change)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Streamlit config — disable the browser auto-open and the welcome message
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Health check — verifies the app is responding
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Launch the app
CMD ["python", "-m", "streamlit", "run", "app/app.py"]
