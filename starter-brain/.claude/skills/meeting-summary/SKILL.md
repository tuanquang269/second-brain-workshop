---
name: meeting-summary
description: Turn a meeting transcript or notes into 96-daily/meeting-<YYYY-MM-DD>.md with decisions, todos (owner + due), risks, open questions, and an email draft section — nothing is sent. Use when the user says "/meeting-summary", "tóm tắt cuộc họp", "summarize meeting", "họp xong rồi", or gives a transcript path in 99-inbox/.
---

# meeting-summary

## Input
- Đường dẫn transcript/ghi chú họp trong `99-inbox/` (txt/md), hoặc text dán thẳng.
- Tuỳ chọn: ngày họp (mặc định = ngày trong transcript, không có → hôm nay), người nhận email.

## Steps
1. Đọc transcript. Xác định: ngày, người dự, chủ đề.
2. Soạn nháp file `96-daily/meeting-<YYYY-MM-DD>.md`:
   ```
   ---
   title: Họp <chủ đề> — YYYY-MM-DD
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   type: log
   tags: [daily]
   sources: ["99-inbox/<file>"]
   ---
   # Họp <chủ đề> — YYYY-MM-DD
   Người dự: …
   ## Quyết định
   1. …
   ## Việc cần làm
   | Việc | Ai | Hạn |
   |---|---|---|
   | … | … (không rõ → TBD) | … (không rõ → TBD) |
   ## Rủi ro / vướng
   - …
   ## Câu hỏi còn mở
   - …
   ## Email draft (chưa gửi)
   Chủ đề: [Tóm tắt họp] <chủ đề> — YYYY-MM-DD
   Chào cả nhóm,
   <3–5 dòng: quyết định chính + bảng việc rút gọn + hạn gần nhất>
   ```
3. **STOP.** Hiện nháp trong chat. Hỏi: "OK / sửa gì?". Chờ trả lời. Không ghi file trước khi có OK.
4. Sau OK: ghi file. Thêm dòng vào `00.5-log.md`: `## [YYYY-MM-DD] distill | meeting-summary → 96-daily/meeting-<ngày>.md · verdict: OK`.
5. Trả lời: đường dẫn file + "Email draft nằm cuối file — copy gửi tay. Bước nâng cấp: nối skill gửi mail."

## Rules
- Tiếng Việt, câu ngắn. Giữ tên riêng, số liệu nguyên văn.
- **Không bịa owner hoặc hạn.** Không rõ → `TBD`.
- ≥3 dòng việc cần làm nếu transcript có; ít hơn → ghi rõ "transcript chỉ có N việc".
- Không gửi email. Không tạo file nào khác.
