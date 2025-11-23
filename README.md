📄 Python PDF Master Tool

Python PDF Master Tool là một ứng dụng giao diện đồ họa (GUI) mạnh mẽ và dễ sử dụng, được viết bằng Python. Công cụ này giúp bạn xử lý các tệp PDF nhanh chóng: ghép file, tách trang, xoay chiều và đặt mật khẩu bảo vệ chỉ với vài cú click chuột.

Điểm nổi bật: Không cần upload file lên các trang web lạ, đảm bảo an toàn dữ liệu 100% vì mọi thứ chạy offline trên máy tính của bạn.

✨ Tính Năng Chính

📂 Ghép File (Merge): Gộp không giới hạn số lượng file PDF thành một file duy nhất.

✂️ Tách & Chọn Trang Thông Minh: Hỗ trợ cú pháp linh hoạt (ví dụ: 1-5, 8, 10-12) để lấy chính xác những trang bạn cần.

🔄 Xoay Trang (Rotate): Xoay file PDF theo các góc 90°, 180°, 270° trước khi ghép (Rất hữu ích cho các file scan bị ngược).

📑 Tự Động Tạo Mục Lục (Auto Bookmarks): File kết quả sẽ tự động có Mục lục (Outline) tương ứng với tên các file thành phần, giúp tra cứu dễ dàng.

🔒 Bảo Mật (Encryption): Đặt mật khẩu mã hóa cho file PDF đầu ra chuẩn AES.

⬆️ Sắp Xếp Linh Hoạt: Dễ dàng thay đổi thứ tự ghép file bằng các nút điều hướng Lên/Xuống.

🎨 Giao Diện Hiện Đại: Sử dụng thư viện tkinter với phong cách thiết kế phẳng, sạch sẽ và thân thiện.

📸 Giao Diện

(Bạn hãy chụp ảnh màn hình tool khi chạy và thay thế vào link bên dưới)

🛠️ Cài Đặt

Trước khi chạy, hãy đảm bảo máy tính của bạn đã cài đặt Python (phiên bản 3.6 trở lên).

Bước 1: Clone dự án về máy

git clone [https://github.com/username-cua-ban/python-pdf-master-tool.git](https://github.com/username-cua-ban/python-pdf-master-tool.git)
cd python-pdf-master-tool


Bước 2: Cài đặt thư viện

Dự án sử dụng thư viện pypdf để xử lý lõi.

pip install -r requirements.txt


🚀 Hướng Dẫn Sử Dụng

Chạy ứng dụng:

python PDF_Merger_Tool_Final.py


Thêm file: Nhấn nút + Thêm File và chọn các file PDF cần xử lý.

Cấu hình:

Chọn trang: Nhập số trang vào ô bên cạnh tên file (VD: 1-3 để lấy 3 trang đầu). Để trống nếu muốn lấy hết.

Xoay: Nhấn nút ⟳ 0° để xoay trang nếu cần.

Sắp xếp: Dùng nút ⬆ hoặc ⬇ để đổi thứ tự.

Tùy chọn: Tick vào ô Đặt mật khẩu nếu muốn bảo vệ file.

Xuất file: Nhấn nút 🚀 GHÉP FILE NGAY và chọn nơi lưu.

📦 Cấu Trúc Dự Án

python-pdf-master-tool/
├── PDF_Merger_Tool_Final.py   # Source code chính của chương trình
├── requirements.txt           # Danh sách các thư viện cần thiết
└── README.md                  # Tài liệu hướng dẫn sử dụng


🤝 Đóng Góp (Contributing)

Mọi đóng góp đều được hoan nghênh! Nếu bạn tìm thấy lỗi hoặc muốn thêm tính năng mới (ví dụ: chế độ Dark Mode, nén file...), hãy tạo một Pull Request.

Fork dự án.

Tạo branch mới (git checkout -b feature/TinhNangMoi).

Commit thay đổi (git commit -m 'Thêm tính năng X').

Push lên branch (git push origin feature/TinhNangMoi).

Mở Pull Request.

📝 Giấy Phép (License)

Dự án này được phát hành dưới giấy phép MIT License. Bạn hoàn toàn miễn phí sử dụng, sửa đổi và phân phối.

Được phát triển với ❤️ bằng Python.
