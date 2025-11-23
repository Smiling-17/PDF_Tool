# 📄 **Python PDF Tool -- Smiling 😺**

## 🔧 Ứng dụng gộp & xử lý PDF đơn giản -- mạnh mẽ -- trực quan

**Python PDF Tool** là ứng dụng desktop được xây dựng bằng **Tkinter**
và **pypdf**, cho phép bạn thao tác với PDF một cách nhanh chóng và trực
quan:

-   Gộp nhiều file PDF thành một file duy nhất
-   Chọn trang tùy ý từ từng file
-   Xoay trang PDF theo ý muốn
-   Thay đổi thứ tự sắp xếp file
-   Tự động tạo Bookmark theo tên file
-   Đặt mật khẩu bảo vệ PDF đầu ra

------------------------------------------------------------------------

# 📸 Giao diện

Ứng dụng gồm 3 phần chính:

### **1️⃣ Header**

-   Nút **+ Thêm File**
-   Nút **🗑 Xóa Hết**

### **2️⃣ Danh sách PDF**

Hiển thị: - Tên file + số trang
- Nút xoay trang
- Ô nhập phạm vi trang
- Nút tăng/giảm thứ tự
- Nút xoá file

### **3️⃣ Footer**

-   Tuỳ chọn **Đặt mật khẩu**
-   Nút **🚀 GHÉP FILE NGAY**

------------------------------------------------------------------------

# 🚀 Tính năng chi tiết

## ✔ 1. Thêm và kiểm tra file PDF

Ứng dụng: - Cho phép chọn nhiều file cùng lúc
- Kiểm tra tính hợp lệ
- Lấy số trang bằng `PdfReader`

------------------------------------------------------------------------

## ✔ 2. Chọn trang cần dùng

Bạn có thể nhập theo các cú pháp: - `1-5`
- `1, 3, 7`
- `1-4, 6, 8-10`

Ứng dụng tự động phân tích & chuẩn hóa.

------------------------------------------------------------------------

## ✔ 3. Xoay trang PDF

-   Mỗi lần click xoay **90°**
-   Hỗ trợ xoay từng file độc lập

------------------------------------------------------------------------

## ✔ 4. Sắp xếp thứ tự file

-   Nút **⬆** và **⬇** giúp thay đổi thứ tự file được merge
-   Ảnh hưởng trực tiếp đến thứ tự trang trong file PDF cuối

------------------------------------------------------------------------

## ✔ 5. Tự động tạo Bookmark

Khi gộp file: - Tên từng file PDF được thêm thành một **Bookmark** -
Giúp nhảy nhanh tới từng phần trong PDF gộp

------------------------------------------------------------------------

## ✔ 6. Đặt mật khẩu PDF

-   Hỗ trợ mã hóa bằng `writer.encrypt()`
-   Chỉ cần nhập password rồi xuất file

------------------------------------------------------------------------

## ✔ 7. Xuất file PDF gộp

-   Tự chọn đường dẫn lưu
-   Mặc định: **merged_document.pdf**
-   Hiện thông báo thành công + tổng số trang đã gộp

------------------------------------------------------------------------

# 🛠 Cài đặt

## Yêu cầu

-   Python ≥ **3.8**
-   Cài thư viện:

``` bash
pip install pypdf
```

Nếu dùng Linux:

``` bash
sudo apt install python3-tk
```

------------------------------------------------------------------------

# ▶️ Chạy ứng dụng

``` bash
python main.py
```

------------------------------------------------------------------------

# 📂 Cấu trúc

    main.py        # Source code chính
    README.md          # File mô tả dự án
    requirements.txt    # Thư viện cần thiết

------------------------------------------------------------------------

# 🧠 Kiến trúc code

## **🔹 Lớp chính: `PDFMergerApp`**

### **Các phương thức quan trọng:**

#### `add_files()`

-   Chọn file
-   Đọc số trang
-   Kiểm tra hợp lệ

#### `parse_page_selection()`

-   Phân tích chuỗi trang
-   Hỗ trợ dạng range & danh sách

#### `draw_row()`

-   Vẽ từng dòng PDF lên UI
-   Render đầy đủ nút xoay, xoá, thứ tự

#### `move_item()`, `delete_item()`

-   Quản lý danh sách PDF

#### `process_pdf()`

-   Merge PDF theo thứ tự
-   Lọc trang theo lựa chọn
-   Xoay theo góc đã đặt
-   Tạo Bookmark tự động
-   Đặt mật khẩu nếu bật
-   Ghi file xuất ra

------------------------------------------------------------------------

# ❤️ Tác giả

Made with love by **Smiling 😺**
Ứng dụng miễn phí -- đơn giản -- mạnh mẽ -- dễ sử dụng.

- Dark/Light mode mới
- Refactor code
