# Mẫu SKILL.md — 4 trường là đủ

> Copy khối dưới vào `.claude/skills/<ten-skill>/SKILL.md`. Tên thư mục = `name`. Restart `claude` để nạp. Gọi bằng `/<ten-skill>`.
> Sau đó thêm 1 dòng vào `00.7-skills-index.md`. Không có dòng đó = skill không tồn tại.

```markdown
---
name: ten-skill
description: <Làm gì, ra file gì>. Use when I say "<câu kích hoạt 1>", "<câu kích hoạt 2>", or paste <loại input>.
---

# ten-skill

## Input
- <file trong 99-inbox/ hoặc text dán vào>

## Steps
1. Đọc input.
2. Viết `<thư mục>/<tên-file>.md` gồm: <mục 1> · <mục 2> · <mục 3>.
3. Thêm 1 dòng vào `00.5-log.md`: `## [YYYY-MM-DD] <động từ> | ten-skill → <file>`.
4. STOP. Hiện bản nháp, hỏi "OK / sửa gì?", chờ trả lời rồi mới ghi file cuối. Ghi verdict vào `00.5-log.md`.

## Rules
- Tiếng Việt. Câu ngắn.
- Không bịa. Thiếu thông tin → ghi "TBD".
- <luật rút từ 00.6-mistakes.md>
```

**Kiểm tra 1 dòng:** chạy `/<ten-skill> <input thật>` → file đầu ra xuất hiện trong Obsidian trong 60 giây. Không xuất hiện = `name` không khớp tên thư mục, hoặc chưa restart `claude`.
