import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pypdf import PdfReader, PdfWriter
import os

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python PDF Tool - Smiling 😺")
        self.root.geometry("900x650")
        self.root.configure(bg="#f0f2f5")

        # Dữ liệu chính
        self.files_data = []

        self.setup_styles()
        self.create_header()
        self.create_main_list()
        self.create_footer()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", gripcount=0, background="#bdc3c7", 
                        darkcolor="#bdc3c7", lightcolor="#bdc3c7", 
                        troughcolor="#f0f2f5", bordercolor="#f0f2f5", arrowcolor="#bdc3c7")
        style.configure("TCombobox", padding=5)

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="white", pady=15, padx=20)
        header_frame.pack(fill=tk.X)

        tk.Label(header_frame, text="📄 PDF TOOL", font=("Segoe UI", 16, "bold"), bg="white", fg="#2c3e50").pack(side=tk.LEFT)

        btn_frame = tk.Frame(header_frame, bg="white")
        btn_frame.pack(side=tk.RIGHT)

        tk.Button(btn_frame, text="+ Thêm File", command=self.add_files, 
                  bg="#2196f3", fg="white", font=("Segoe UI", 10, "bold"), 
                  relief="flat", padx=15, pady=5, cursor="hand2").pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="🗑 Xóa Hết", command=self.clear_all, 
                  bg="#ffebee", fg="#c62828", font=("Segoe UI", 10), 
                  relief="flat", padx=10, pady=5, cursor="hand2").pack(side=tk.LEFT, padx=5)

    def create_main_list(self):
        list_container = tk.Frame(self.root, bg="#f0f2f5", padx=20, pady=10)
        list_container.pack(fill=tk.BOTH, expand=True)

        tbl_header = tk.Frame(list_container, bg="#dfe6e9", height=30)
        tbl_header.pack(fill=tk.X)
        tk.Label(tbl_header, text="THÔNG TIN FILE", bg="#dfe6e9", fg="#636e72", font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=10)
        
        right_header = tk.Frame(tbl_header, bg="#dfe6e9")
        right_header.pack(side=tk.RIGHT, padx=10)
        tk.Label(right_header, text="XOAY", bg="#dfe6e9", fg="#636e72", font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=20)
        tk.Label(right_header, text="CHỌN TRANG", bg="#dfe6e9", fg="#636e72", font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=20)
        tk.Label(right_header, text="THỨ TỰ", bg="#dfe6e9", fg="#636e72", font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=15)
        tk.Label(right_header, text="XÓA", bg="#dfe6e9", fg="#636e72", font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT, padx=10)

        self.canvas = tk.Canvas(list_container, bg="#f0f2f5", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=self.canvas.yview, style="Vertical.TScrollbar")
        self.scrollable_frame = tk.Frame(self.canvas, bg="#f0f2f5")

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=900)
        self.canvas.bind('<Configure>', lambda e: self.canvas.itemconfig(self.canvas.find_all()[0], width=e.width))
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=5)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=5)

    def create_footer(self):
        footer_frame = tk.Frame(self.root, bg="white", pady=15, padx=20)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        opt_frame = tk.Frame(footer_frame, bg="white")
        opt_frame.pack(side=tk.LEFT)

        # Chỉ giữ lại phần Mật khẩu
        self.use_password = tk.BooleanVar()
        tk.Checkbutton(opt_frame, text="Đặt mật khẩu:", variable=self.use_password, bg="white").pack(side=tk.LEFT)
        self.password_entry = tk.Entry(opt_frame, show="*", width=15, bd=1, relief="solid")
        self.password_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(footer_frame, text="🚀 GHÉP FILE NGAY", command=self.process_pdf, 
                  bg="#27ae60", fg="white", font=("Segoe UI", 11, "bold"), 
                  relief="flat", padx=20, pady=8, cursor="hand2").pack(side=tk.RIGHT)

    def add_files(self):
        filepaths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if not filepaths: return
        for path in filepaths:
            try:
                reader = PdfReader(path)
                num_pages = len(reader.pages)
                is_valid = True
            except:
                num_pages = 0
                is_valid = False

            item = {
                'path': path,
                'range_var': tk.StringVar(),
                'rotate_angle': 0,
                'max_pages': num_pages,
                'is_valid': is_valid
            }
            self.files_data.append(item)
        self.refresh_ui_list()

    def refresh_ui_list(self):
        for widget in self.scrollable_frame.winfo_children(): widget.destroy()
        for index, item in enumerate(self.files_data): self.draw_row(index, item)

    def draw_row(self, index, item):
        bg_color = "white" if index % 2 == 0 else "#f8f9fa"
        row_frame = tk.Frame(self.scrollable_frame, bg=bg_color, pady=8, padx=5)
        row_frame.pack(fill=tk.X, pady=1)

        icon = "📄" if item['is_valid'] else "⚠️"
        color = "#2c3e50" if item['is_valid'] else "#c0392b"
        tk.Label(row_frame, text=icon, font=("Segoe UI", 14), bg=bg_color, fg="#3498db").pack(side=tk.LEFT, padx=10)

        info_frame = tk.Frame(row_frame, bg=bg_color)
        info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Label(info_frame, text=os.path.basename(item['path']), font=("Segoe UI", 10, "bold"), fg=color, bg=bg_color, anchor="w").pack(fill=tk.X)
        tk.Label(info_frame, text=f"{item['max_pages']} trang" if item['is_valid'] else "Lỗi file", font=("Segoe UI", 8), fg="#7f8c8d", bg=bg_color, anchor="w").pack(fill=tk.X)

        action_frame = tk.Frame(row_frame, bg=bg_color)
        action_frame.pack(side=tk.RIGHT, padx=5)

        if item['is_valid']:
            btn_rot = tk.Button(action_frame, text=f"⟳ {item['rotate_angle']}°", command=lambda i=index: self.rotate_file(i),
                                bg="#e3f2fd", fg="#1565c0", relief="flat", font=("Consolas", 9), width=8, cursor="hand2")
            btn_rot.pack(side=tk.LEFT, padx=15)
            tk.Entry(action_frame, textvariable=item['range_var'], width=12, bd=1, relief="solid", font=("Consolas", 10), justify="center").pack(side=tk.LEFT, padx=10, ipady=3)

        state_up = "normal" if index > 0 else "disabled"
        tk.Button(action_frame, text="⬆", command=lambda i=index: self.move_item(i, -1), state=state_up, bg="#fff", relief="flat", fg="#555", width=2).pack(side=tk.LEFT)
        state_down = "normal" if index < len(self.files_data) - 1 else "disabled"
        tk.Button(action_frame, text="⬇", command=lambda i=index: self.move_item(i, 1), state=state_down, bg="#fff", relief="flat", fg="#555", width=2).pack(side=tk.LEFT)
        tk.Button(action_frame, text="✕", command=lambda i=index: self.delete_item(i), bg="#ffebee", fg="red", relief="flat", font=("Arial", 9, "bold"), width=3).pack(side=tk.LEFT, padx=(10, 0))

    def move_item(self, index, direction):
        new_index = index + direction
        if 0 <= new_index < len(self.files_data):
            self.files_data[index], self.files_data[new_index] = self.files_data[new_index], self.files_data[index]
            self.refresh_ui_list()

    def delete_item(self, index):
        del self.files_data[index]
        self.refresh_ui_list()

    def rotate_file(self, index):
        self.files_data[index]['rotate_angle'] = (self.files_data[index]['rotate_angle'] + 90) % 360
        self.refresh_ui_list()

    def clear_all(self):
        self.files_data = []
        self.refresh_ui_list()

    def parse_page_selection(self, page_str, max_pages):
        if not page_str.strip(): return list(range(max_pages))
        selected_pages = set()
        for part in page_str.split(','):
            part = part.strip()
            if '-' in part:
                try:
                    s, e = map(int, part.split('-'))
                    selected_pages.update(range(max(1, s) - 1, min(e, max_pages)))
                except: continue
            else:
                try:
                    p = int(part)
                    if 1 <= p <= max_pages: selected_pages.add(p - 1)
                except: continue
        return sorted(list(selected_pages))

    def process_pdf(self):
        if not self.files_data:
            messagebox.showwarning("Nhắc nhở", "Danh sách trống!")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")], initialfile="merged_document.pdf")
        if not save_path: return

        writer = PdfWriter()
        total_pages = 0
        
        try:
            for item in self.files_data:
                if not item['is_valid']: continue
                
                reader = PdfReader(item['path'])
                pages_idx = self.parse_page_selection(item['range_var'].get(), item['max_pages'])
                
                if not pages_idx: continue

                # Tự động tạo Bookmark (Mục lục) là tên file
                filename = os.path.basename(item['path'])
                writer.add_outline_item(title=filename, page_number=total_pages)

                for idx in pages_idx:
                    page = reader.pages[idx]
                    
                    # Xoay trang nếu cần
                    # Ở chế độ merge thường này, chỉ cần rotate là đủ, pypdf sẽ tự update metadata
                    if item['rotate_angle'] != 0:
                        page.rotate(item['rotate_angle'])
                    
                    writer.add_page(page)
                    total_pages += 1

            if total_pages == 0:
                messagebox.showwarning("Lỗi", "Không có trang nào được chọn!")
                return

            # Đặt mật khẩu nếu có
            if self.use_password.get() and self.password_entry.get():
                writer.encrypt(self.password_entry.get())

            with open(save_path, "wb") as f:
                writer.write(f)
            
            messagebox.showinfo("Thành công", f"Đã ghép {total_pages} trang thành công!\nFile lưu tại: {save_path}")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Chi tiết lỗi: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
