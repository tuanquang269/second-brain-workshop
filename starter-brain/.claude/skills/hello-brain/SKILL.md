---
name: hello-brain
description: First run of this second brain — read CLAUDE.md and 00.4-index.md, then write 99-inbox/hello.md listing 3 things this brain knows and 3 things it does not know yet. Use when the user says "/hello-brain", "hello brain", "não này biết gì", or on the very first session in a new vault.
---

# hello-brain

## Input
- Không cần input. Đọc `CLAUDE.md`, `00.4-index.md`, `00.7-skills-index.md`.

## Steps
1. Đọc 3 file trên. Không đọc gì khác.
2. Viết `99-inbox/hello.md` (tạo thư mục nếu chưa có):
   ```
   # Xin chào, não thứ hai
   Ngày: YYYY-MM-DD
   ## 3 điều não này đã biết
   1. … (trích từ CLAUDE.md / index)
   2. …
   3. …
   ## 3 điều não này chưa biết (bạn nên thêm)
   1. … (ví dụ: chưa có trang nào trong 10-work/)
   2. …
   3. …
   ## Skill có sẵn
   - <liệt kê từ 00.7-skills-index.md, mỗi dòng: tên · gọi bằng>
   ```
3. Thêm 1 dòng trên cùng phần nhật ký của `00.5-log.md`: `## [YYYY-MM-DD] wire | hello-brain chạy lần đầu → 99-inbox/hello.md`.
4. Trả lời trong chat: đường dẫn file + câu "Mở file này trong Obsidian."

## Rules
- Tiếng Việt, câu ngắn.
- Nếu `CLAUDE.md` còn dấu `______` → điều chưa biết #1 = "chưa điền tôi là ai trong CLAUDE.md".
- Không tạo file nào khác ngoài `99-inbox/hello.md` và dòng log.
