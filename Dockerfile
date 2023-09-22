#FROM tiangolo/uvicorn-gunicorn:python3.10
#
#RUN apt update && \
#    apt install -y htop libgl1-mesa-glx libglib2.0-0
#
#COPY requirements.txt /tmp/requirements.txt
#RUN pip install --no-cache-dir -r /tmp/requirements.txt



#FROM tiangolo/uvicorn-gunicorn:python3.10
#
## Set Working directory
#WORKDIR /app
#
#RUN apt update && \
#    apt install -y htop libgl1-mesa-glx libglib2.0-0
#
## Copy files into the app folder
#COPY . /app
#
#COPY requirements.txt /tmp/requirements.txt
#
#RUN pip install --no-cache-dir -r /tmp/requirements.txt
#
#CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8080"]


# Sử dụng image tiêu chuẩn từ tiền built Python 3.8
FROM python:3.9-slim-buster

# Thiết lập thư mục làm việc
WORKDIR /app

# Cài đặt các thư viện cần thiết cho compilation
RUN apt update && \
    apt install -y htop libgl1-mesa-glx libglib2.0-0

# Sao chép requirements.txt và cài đặt các dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Sao chép toàn bộ code vào container
COPY . .

# Mở cổng 8000 để FastAPI có thể nhận kết nối
EXPOSE 8000

# Chạy FastAPI server khi khởi động container
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
