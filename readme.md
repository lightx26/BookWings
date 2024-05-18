# Xây dựng trang web bán sách
Trang web này được xây dựng để bán sách trực tuyến. Bạn có thể tìm thấy các cuốn sách từ nhiều tác giả khác nhau. Hãy khám phá và tìm kiếm những cuốn sách mà bạn quan tâm.

Tác giả:
- Nguyễn An Hưng
- Nguyễn Cửu Nhật Quang

## Hướng dẫn khởi chạy dự án
### 1. Đối với Windows
Đối với hệ điều hành Windows thì ta có thể cài đặt các gói thư viện cần thiết cho python với cú pháp sau:
```bash
$ pip install -r requirements.txt
```


### 2. Đối với Ubuntu
Đối với Ubuntu bạn cần cài đặt một số packages cho hệ thống, để đơn giản hóa công việc, bạn cài đặt hệ thống mình với các câu lệnh dưới:

```bash
$ sudo apt-get install -y python3-mysqldb
```

```bash
$ sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

Sau khi cài đặt các gói hệ thống ở trên, ta tiến hành cài đặt các thư viện cần thiết cho python với cú pháp sau:
```bash
$ pip install -r requirements.txt
```

### Một số thiết lập đầu tiên với Database
Hệ thống sử dụng mysql làm cơ sở dữ liệu, nên do đó, máy tính cần có các thiết lập liên quan đến mysql-client, sau khi thiết lập thông tin kết nối tại `BookWings/settings.py`. Chúng ta cần chạy cú pháp sau để khởi tạo các bảng và **migrate** dữ liệu.

```bash
$ python manage.py makemigrations
```
```bash
$ python manage.py migrate
```