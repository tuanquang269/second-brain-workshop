# Ảnh cho deck

## Deck chính (`../index.html`, 6 slide) — chỉ cần 1 ảnh

| File | Slide | Chụp gì |
|---|---|---|
| `qr-deck.png` | 6 | QR trỏ tới `https://tuanquang269.github.io/second-brain-workshop/` |

6 slide còn lại là chữ + SVG, không cần ảnh. **Hình ảnh thực thi diễn ra trực tiếp trên máy chiếu** (terminal + Obsidian), không phải trên slide.

Tuỳ chọn: quay `hook-ab.mp4` (90s, A/B pane trái vs pane phải) để chiếu khi wifi/API chết. Đặt cạnh `index.html`, mở tay.

## Phụ lục (`../full.html`, 58 slide) — 36 ảnh nếu anh muốn dùng bản này

Thả PNG vào thư mục này với **đúng tên file** (số đầu = số slide trong `full.html`). Thiếu file → slide hiện khung nét đứt kèm hướng dẫn chụp, deck vẫn chạy.

Kỹ thuật chụp: terminal ≥18pt · Obsidian zoom 150% · dark theme cả hai · statusline hiện context · che dữ liệu nhạy cảm.

| File | Slide | Chụp gì |
|---|---|---|
| `03-outline-notebook.png` | 3 | Trang giấy outline thật (ảnh chụp sổ) |
| `04-ab-freeze.png` | 4 | Đóng băng 2 pane lúc gõ xong: trái `~/demo-empty` + prompt 250 từ, phải vault thật |
| `06-candidates-tree-base.png` | 6 | Cây file `40.1-hiring/candidates/` + hàng trong Base |
| `07-chat-sidebar-200.png` | 7 | Sidebar lịch sử chat ChatGPT/Claude web, hàng trăm chat xám |
| `08-skills-finder-129.png` | 8 | Finder `~/.claude/skills/` + dòng đếm trong `2-skills-index.md` |
| `09-context-73k-8k.png` | 9 | `/context` trước/sau: CLAUDE.md 73,637 B → 8,656 B |
| `10-graph-kevin-vs-3.png` | 10 | Graph view vault thật vs graph vault mới (3 chấm) |
| `11-log-4-numbers.png` | 11 | 4 con số thật từ `00.5-log.md` (số phiên/tuần, skill tái dùng…) |
| `15-distill-log-lines.png` | 15 | Các dòng `distill` trong `00.5-log.md` |
| `16-wire-skills-index.png` | 16 | `2-skills-index.md` + khối hooks trong `settings.json` |
| `17-harness-blocked-mistakes.png` | 17 | Terminal dòng BLOCKED + `00.6-mistakes.md` |
| `20-setup-target-state.png` | 20 | Trạng thái đích: Obsidian trái, terminal phải "Loaded CLAUDE.md" |
| `21-three-lines-typed.png` | 21 | Terminal sau khi gõ 3 dòng: `cd`, `claude`, `/hello-brain` |
| `22-obsidian-create-vault.png` | 22 | Dialog Obsidian *Create new vault* tên `brain` |
| `23-claude-md-12-lines.png` | 23 | `CLAUDE.md` khởi tạo mở trong Obsidian |
| `24-context-fresh-session.png` | 24 | `/context` của phiên mới trong vault mới |
| `26-kevin-folder-tree.png` | 26 | Cây thư mục vault thật (số = thứ tự đọc) |
| `27-vault-tool-move.png` | 27 | `vault_tool.py move` + link tự cập nhật |
| `29-graph-before-after.png` | 29 | Graph trước/sau khi Claude thêm wikilink |
| `30-work-base.png` | 30 | Bảng `.base` của một thư mục |
| `31-lint-green.png` | 31 | `python3 80.3-lint_wiki.py` xanh |
| `33-qr-lark-base.png` | 33 | QR tới Lark Base "Kết quả" |
| `35-work-orders-kevin.png` | 35 | `96-daily/work-orders-*.md` thật |
| `37-candidates-base-ranked.png` | 37 | `candidates.base` đã xếp hạng (MODE SCORE) |
| `38-meeting-md.png` | 38 | `96-daily/meeting-<date>.md` với bảng việc-ai-hạn |
| `39-email-campaign-md.png` | 39 | `10-work/email-campaign-<slug>.md` |
| `40-storyboard.png` | 40 | Storyboard PNG / prompt package của `animated-ad-creator` |
| `43-interview-scorecard-frontmatter.png` | 43 | Frontmatter `interview-scorecard/SKILL.md`, tô trigger words |
| `44-claude-writes-skill.png` | 44 | Terminal: Claude đang viết `SKILL.md` mới |
| `45-skills-index-diff.png` | 45 | Diff: 1 dòng mới trong skills-index |
| `47-terminal-ok-sua-gi.png` | 47 | Terminal dừng hỏi "OK / sửa gì?" |
| `48-settings-stop-hook-blocked.png` | 48 | `settings.json` Stop-hook + terminal BLOCKED |
| `50-mistakes-md.png` | 50 | 1 entry thật trong `00.6-mistakes.md` |
| `52-student-graph-skill-node.png` | 52 | Graph starter-brain sau D1–D4 (có node skill) |
| `54-lark-base-gallery.png` | 54 | Lark Base "Kết quả" dạng gallery ≥20 thẻ |
| `58-qr-deck.png` | 58 | QR trỏ tới deck |

Nguồn nội dung: `LLM-Wiki/10-foundations/26-second-brain-workshop.md` §5.
