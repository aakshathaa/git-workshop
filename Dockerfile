FROM python:3.10.2-alpine3.15

WORKDIR /root/workspace/src

COPY download_pdf.py .

RUN pip install requests

CMD ["python", "download_pdf.py"]

