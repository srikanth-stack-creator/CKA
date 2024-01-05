# Use an official Apache image as the base image
FROM httpd:2.4
FROM python:3.9
RUN pip install --no-cache-dir Flask==2.0.1 Werkzeug==2.0.1
# Copy your HTML page into the Apache document root
COPY index.html /usr/local/apache2/htdocs/
COPY app.py /usr/local/apache2/htdocs/
COPY survey_questions.html /usr/local/apache2/htdocs/
COPY confirmation.html /usr/local/apache2/htdocs/
# Expose port 80
EXPOSE 80
