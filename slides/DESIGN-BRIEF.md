# Design brief — deck "Thực chiến Second Brain + AI"

> Dùng để đưa vào Claude Design (hoặc Open Design). Nội dung đã chốt; phần cần thiết kế lại là **hình thức**.
> Bản đang chạy: `slides/index.html` (tự chứa, 6 slide + 2 ngăn) — dùng làm **spec**, không phải bản giao.

## Bối cảnh
Workshop 240 phút tại Finding Camp. Học viên: chủ doanh nghiệp / nhân sự SME Việt Nam, **không kỹ thuật**, Mac + Windows lẫn. 80% thời gian họ gõ trên máy mình; slide chỉ là **mốc**, không phải tài liệu. Máy chiếu hội trường, người ngồi xa 8–10m.

## Tiêu đề
**Thực chiến Second Brain + AI** — *Để cơ giới hoá tư duy thành quy trình làm việc*

## Ràng buộc cứng
1. **Đúng 6 slide.** Không thêm. Chi tiết nằm trong speaker notes (phím `N`), không nằm trên mặt slide.
2. **Ít chữ.** Mỗi slide: 1 ý lớn + tối đa 1 dòng caption ≤ 12 từ. Không đoạn văn.
3. **Chữ to.** Caption ≥ 32px ở 1280×720. Đọc được từ cuối phòng.
4. **Tự chứa 100%**: 1 file HTML, CSS/JS/SVG nhúng, **0 request ra ngoài** (không CDN font, không script ngoài). Phải chạy khi wifi chết.
5. **1 viewport / slide** (`100dvh`), không cuộn dọc, không tràn ngang ở 1280×720 và 1920×1080.
6. **Tiếng Việt** toàn bộ; chỉ tên file/lệnh giữ tiếng Anh. Font phải render đủ dấu.
7. Giữ nguyên cơ chế: `←/→/Space` chuyển slide · `F` toàn màn hình · `N` ghi chú · `B` ngăn bài tập · `L` ngăn tài liệu · `#số` link tới slide · thanh tiến độ + bộ đếm.

## 6 slide
| # | Vai trò | Nội dung phải có |
|---|---|---|
| 1 | Bìa | Tiêu đề + phụ đề · "80% thời gian là bạn gõ · mỗi trạm về nhà bằng 1 file" · Kevin Kreative · PATI Group · nhắc phím B / L · link `starter-brain.zip` |
| 2 | Why (bảng điểm A/B) | 2 cột: **Chat trần** 250 từ / `__` phút / 0 file — **Bộ não** 7 từ / `__` phút / 1 file + 1 skill. Hai ô `__` phải **gõ được ngay trên slide** khi chạy A/B live. Caption: "Cùng một việc. Đóng tab: một bên mất, một bên còn." |
| 3 | What (sơ đồ) | Sơ đồ 4 lớp `1_Nguồn → 2_Wiki → 3_Tôi` trong vault, `4_Kết quả` **ngoài** ranh giới; 3 động từ DISTILL / WIRE / HARNESS; dải 4 file OS (CLAUDE.md · index · log · mistakes); dải động cơ Claude Code + 4 bậc; 5 chip loại trang Wiki; cột 5 dòng "đã kiểm chứng / đã sửa". Nguồn: `slides/anatomy.svg` |
| 4 | How (4 trạm) | Cài đặt 0:30–0:55 → `CLAUDE.md` · Sắp xếp 0:55–1:35 → `10-work/1-<slug>.md` · Sử dụng 1:45–2:40 → file lane · Huấn luyện 2:40–3:45 → `SKILL.md`. Mỗi ô 1 link file mẫu click được |
| 5 | Sử dụng (3 lane) | HR / Ops / Mkt: mô tả 1 dòng + file đầu ra + link file mẫu. Caption nhắc "bấm B xem cả 10 bài tập" |
| 6 | Kết | 3 luật để không bỏ cuộc · QR (`img/qr-deck.png`) · URL · 2 nút tải zip |

## 2 ngăn (overlay toàn màn hình)
- **`B` — 10 bài tập**: 10 thẻ (K1–K5 = 5 bài chính, viền cam; E1–E5 = bài thêm, viền xanh mòng két). Mỗi thẻ: mã · tên · chip lane · dòng "vào:" · **khối prompt bấm là chép** · `→ file đầu ra` · `✓ done-check` · link file mẫu.
- **`L` — 18 link tài liệu**: 5 nhóm (Tải về · Prompt để gõ · File mẫu HR/Ops/Mkt).

## Hướng thẩm mỹ hiện tại (có thể đổi, nêu lý do)
Nền gần đen `#0d0c0a` · chữ trắng ngà `#f0e8d8` · 1 accent hổ phách `#e08a3c` · 1 phụ xanh mòng két `#5db3a5` · font IBM Plex Sans + IBM Plex Mono. Không tím/neon, không gradient. Terminal + giấy.

**Việc của khâu thiết kế lại:** nhịp thị giác giữa 6 slide (đừng 6 slide cùng một bố cục), hệ thống hoá spacing/typography, làm sơ đồ slide 3 đẹp và dễ đọc hơn ở khoảng cách xa, và làm 2 ngăn overlay trông như một sản phẩm chứ không phải bảng dữ liệu.

## Không được đổi
Số slide (6) · nội dung 10 bài tập và 18 link · 4 lớp và 3 động từ trong sơ đồ · 4 mốc giờ · cơ chế phím · tính tự chứa.
