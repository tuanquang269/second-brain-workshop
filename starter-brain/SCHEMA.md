# SCHEMA — cách đặt tên và link trong não này

1. Trang kiến thức nằm trong thư mục có số: `10-work/`, `40-hr/`. Số = thứ tự đọc.
2. Tên file: `N-<slug>.md`, ví dụ `10-work/1-quy-trinh-don-hang.md`. `N` = thứ tự trong thư mục.
3. Link giữa các trang: `[[slug]]` — không viết số vào link. Trang nào cũng có `aliases: [<slug>]` trong frontmatter để link chạy.
4. Frontmatter bắt buộc:
   ```
   ---
   title: Tiêu đề
   aliases: [ten-slug]
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   type: page | candidate | log
   tags: [knowledge | hr | ops | marketing | daily]
   ---
   ```
5. Chỉ 5 tag: `knowledge` · `hr` · `ops` · `marketing` · `daily`. Tag mới → thêm vào đây trước.
6. `96-daily/` dùng tên `<loại>-YYYY-MM-DD.md` (meeting-, work-orders-, weekly-), không cần số.
7. Trang thô (chưa xử lý) → `99-inbox/`. Phân vân → để inbox.
