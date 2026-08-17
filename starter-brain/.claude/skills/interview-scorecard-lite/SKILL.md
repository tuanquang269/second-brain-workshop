---
name: interview-scorecard-lite
description: Round-1 hiring helper for this vault. MODE PREP — given a candidate CV (text/markdown/PDF in 99-inbox/) and a role, write a CV screen + a 30-minute Vietnamese interview question set mapped to 5 dimensions, saved to 40-hr/candidates/<slug>.md (status prep). MODE SCORE — given a short typed debrief after the interview, fill the 5 scores (1–6) so the card auto-ranks in 40-hr/candidates/candidates.base. Use when the user says "/interview-scorecard-lite", "prep phỏng vấn", "screen CV này", "chấm ứng viên", "score <slug>", or pastes a CV/debrief. Text only — no audio, no external API.
---

# interview-scorecard-lite

Phiên bản workshop của quy trình chấm vòng 1. Mọi đường dẫn **tương đối với vault**. Không gọi API ngoài, không xử lý audio.

## Thang điểm — 5 chiều, mỗi chiều 1–6 (key frontmatter → ý nghĩa)
| Key | Chiều | 6 | 3 | 1 |
|---|---|---|---|---|
| `s1_integrity` | Chính trực | báo rủi ro sớm, tự sửa, cam kết lại | thừa nhận nhưng chậm/một phần | né trách nhiệm |
| `s2_ownership` | Ownership | nói theo dạng vấn đề → giải pháp → hành động, 0 lý do | lẫn giải thích và giải pháp, cần nhắc | đổ lỗi, không nhận |
| `s3_problem_solving` | Giải quyết vấn đề & DoD | luôn mang 1-3-1 (1 vấn đề, 3 phương án, 1 đề xuất) | thỉnh thoảng có giải pháp, còn dựa sếp | chờ, né, phụ thuộc |
| `s4_ai_first` | AI First | xây workflow/automation AI cho cả team | dùng AI việc cơ bản (viết, tra cứu) | không dùng / không tin AI |
| `s5_impact_8020` | Impact 80/20 | ưu tiên việc ra doanh thu, cắt việc vô giá trị | biết ưu tiên nhưng hay bị việc nhỏ kéo | không phân biệt việc lớn/nhỏ |

**Luật cứng:** chỉ tính **ví dụ thật đã làm** ("em sẽ…" = không phải bằng chứng → đẩy "em ĐÃ làm gì?"). Chiều nào **không có ví dụ cụ thể → tối đa 1**. Chỉ hỏi việc liên quan công việc; không hỏi tuổi/gia đình/thai sản/tôn giáo/sức khoẻ/chính trị.

## MODE PREP — `prep <đường dẫn CV> role=<vị trí>`
1. Đọc CV (file trong `99-inbox/`, hoặc text dán). Ghi: kinh nghiệm, thời gian mỗi nơi, 3–5 tuyên bố cần kiểm chứng.
2. **CV screen (tiếng Việt):** độ khớp vị trí · nghiêng tạm theo 5 chiều (ghi "chưa kiểm chứng") · 3–5 tuyên bố cần hỏi thật · chiều nào CV im lặng (phải hỏi trực tiếp).
3. **Bộ câu hỏi 30 phút (tiếng Việt, đọc to được):** 5 khối = 5 chiều, mỗi khối 2–3 câu săn ví dụ thật + dấu hiệu mạnh/yếu + câu đào riêng theo CV này. Hỏi Chính trực trực tiếp (hay bị bỏ qua nhất). Kết bằng 1 câu về logistics (onsite/thu nhập).
4. **Ghi** `40-hr/candidates/<slug>.md` (slug = tên bỏ dấu, chữ thường, gạch ngang; "Nguyễn Văn A" → `nguyen-van-a`) với frontmatter:
   ```
   ---
   type: candidate
   candidate: <Tên>
   role: <vị trí>
   status: prep
   interview_date:
   source_cv: <đường dẫn CV>
   s1_integrity:
   s2_ownership:
   s3_problem_solving:
   s4_ai_first:
   s5_impact_8020:
   avg_score:
   recommendation:
   red_flags:
   ---
   ```
   Thân file = CV screen + bộ câu hỏi + bảng chấm trống (5 hàng: chiều · điểm · bằng chứng).
5. Thêm dòng vào `00.5-log.md`: `## [YYYY-MM-DD] distill | interview prep <slug> → 40-hr/candidates/<slug>.md`. Trả lời: đường dẫn file + bộ câu hỏi trong chat.

## MODE SCORE — `score <slug>: <debrief 3–10 dòng>`
1. Đọc `40-hr/candidates/<slug>.md` + debrief người dùng gõ (không cần audio).
2. Chấm 5 chiều: mỗi chiều = số 1–6 + bằng chứng cụ thể từ debrief. Không có ví dụ / không hỏi tới → 1 và ghi "chưa hỏi". Ghi cờ đỏ nếu có.
3. `avg_score` = trung bình 5 điểm, 1 chữ số thập phân. `recommendation`: ≥5 🟢 mạnh · 4–4.9 🟢 đi tiếp · 3–3.9 🟡 cân nhắc · <3 🔴 loại; cờ đỏ hoặc Chính trực ≤2 → "xem tay".
4. **STOP:** hiện bảng 5 điểm + đề xuất trong chat, hỏi "OK / sửa gì?", chờ trả lời.
5. Sau OK: cập nhật frontmatter (`status: scored`, 5 key, `avg_score`, `recommendation`, `red_flags`, `interview_date`) + bảng bằng chứng tiếng Việt trong thân. Tự kiểm: 5 key là số nguyên 1–6; avg đúng công thức; file nằm trong `40-hr/candidates/`.
6. Thêm dòng vào `00.5-log.md`: `## [YYYY-MM-DD] harness | score <slug> verdict: OK → avg <x>`. Trả lời: điểm, đề xuất, chiều mạnh/yếu nhất, "mở `40-hr/candidates/candidates.base` để xem xếp hạng".

## Rules
- Không bao giờ chấm từ trí nhớ — luôn đọc CV/debrief thật.
- 1 file / 1 ứng viên (prep → scored). Chấm lại = cập nhật cùng file.
- Chính trực = 1 chỉ vì *chưa hỏi* là lỗ hổng phỏng vấn ("chưa đánh giá, hỏi lại"), không phải fail đã chứng minh.
