FROM python:3.10-slim

# تثبيت المتطلبات الأساسية
RUN apt-get update && apt-get install -y \
    chromium-driver \
    && apt-get clean

# إعداد مجلد العمل
WORKDIR /app

# نسخ ملفات المشروع
COPY requirements.txt .
RUN pip install -r requirements.txt

# نسخ كود التطبيق
COPY . .

# أمر تشغيل التطبيق
CMD ["python", "app.py"]
