---
name: work-orders-lite
description: Run a short Musk 5-step pass (question → delete → simplify → accelerate → automate) over a pasted list of 5–10 tasks and write 96-daily/work-orders-<YYYY-MM-DD>.md with one #1 per person, a Definition of Done per task, killed/parked lists, and an automation backlog. Use when the user says "/work-orders-lite", "lên việc ngày mai", "sắp việc", "work orders", or pastes a task list.
---

# work-orders-lite

Bản rút gọn 10–12 phút của phiên brainstorm 5 bước Musk. Không đọc gì ngoài vault này. Kết thúc bằng 1 file.

## Input
- Danh sách 5–10 việc, mỗi dòng: **động từ + đối tượng + hạn** (ví dụ: "Gửi báo giá cho A — thứ Ba"). Có thể kèm tên người làm.
- Ngày áp dụng (mặc định: ngày mai).

## Steps — 5 bước, mỗi bước 1 câu hỏi
1. **Hỏi lại yêu cầu:** với mỗi việc, ai cần nó và để ra kết quả gì? Việc không có người cần → đánh dấu nghi vấn.
2. **Xoá:** việc nào bỏ mà không ai kêu trong 1 tuần? → **Killed** (ghi lý do). Mục tiêu: xoá ≥20%.
3. **Đơn giản:** việc còn lại → 1 câu, động từ đứng đầu, kèm **Definition of Done** người thứ ba kiểm được (số, file, trạng thái nhìn thấy).
4. **Tăng tốc:** xếp **1 việc #1 mỗi người**; còn lại = queued. Việc nào cần người dùng cung cấp gì (duyệt, tài liệu, quyền) → ghi vào "unblocks".
5. **Tự động hoá:** việc lặp lại tuần này là lần thứ 2+ → ghi vào **Automation backlog** (chỉ ghi, không build). Đây là ứng viên skill tiếp theo.
6. **STOP.** Hiện nháp, hỏi "OK / sửa gì?", chờ. Sau OK ghi `96-daily/work-orders-<YYYY-MM-DD>.md`:
   ```
   ---
   title: Work orders YYYY-MM-DD
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   type: log
   tags: [daily]
   ---
   # Work orders — YYYY-MM-DD
   ## ✅ Giao việc
   ### <Người> — #1: <việc>
   - Why: … · DoD: … · Hạn: … · Bước đầu tiên (15'): … · Cần cung cấp: …
   ### <Người> — queued: <việc> — DoD: … · Hạn: …
   ## 🗑️ Killed
   - <việc> — lý do
   ## 📦 Parked
   - <việc> — xem lại: YYYY-MM-DD
   ## 🤖 Automation backlog (ứng viên skill)
   - <việc lặp> — ai làm tay — ~Xh/tuần — lần thứ n
   ## 🔓 Cần người dùng mở khoá trong 24h
   - [ ] …
   ```
7. Thêm dòng vào `00.5-log.md`: `## [YYYY-MM-DD] harness | work-orders → 96-daily/work-orders-<ngày>.md · <n> việc, killed <k>, parked <p>`. Trả lời: đường dẫn + 3 dòng tóm tắt.

## Rules
- Một #1 mỗi người. Không bao giờ hai "ưu tiên cao nhất".
- DoD kiểm được bởi người thứ ba. "Cải thiện X" = fail; "3 file Y trong thư mục Z" = pass.
- Killed/Parked là hồ sơ vĩnh viễn: lần sau chạy, đọc file work-orders gần nhất trước, việc killed quay lại = gọi tên "zombie".
- Tiếng Việt, câu ngắn.
