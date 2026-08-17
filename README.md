# Bộ não thứ hai với Claude Code — Finding Camp workshop kit

Workshop 240' dạy người không kỹ thuật dựng **bộ não thứ hai** (Obsidian vault) và dùng nó với **Claude Code** + Obsidian skills. 80% thực hành trên việc thật; mỗi trạm kết thúc bằng 1 file mở trong Obsidian. Trục: **Distill → Wire → Harness**.

| Thứ | Ở đâu |
|---|---|
| Slide (6 slide mốc · bấm **L** để mở mọi file thực hành) | https://tuanquang269.github.io/second-brain-workshop/slides/ |
| Phụ lục prompt (58 slide, chiếu khi cần dòng lệnh) | https://tuanquang269.github.io/second-brain-workshop/slides/full.html |
| Bộ não mẫu (giải nén → mở bằng Obsidian, `cd` vào → `claude`) | [`starter-brain.zip`](starter-brain.zip) · nguồn `starter-brain/` |
| Dữ liệu mẫu (2 CV · transcript họp · SOP thô · email đối thủ · ticket) | [`demo-data.zip`](demo-data.zip) · nguồn `demo-data/` |
| Email chuẩn bị trước buổi | [`pre-work-email.md`](pre-work-email.md) |
| Đóng gói lại | `./build.sh` |

## Chạy bộ não mẫu (5 phút)
1. Cài Obsidian ≥1.9 và Claude Code (xem `pre-work-email.md`).
2. Giải nén `starter-brain.zip` → thư mục `brain/` (Mac `~/brain`, Windows `C:\brain`). Mở bằng Obsidian: *Open folder as vault*.
3. Terminal: `cd ~/brain && claude --permission-mode acceptEdits` → gõ `/hello-brain`.
4. 8 skill có sẵn: `hello-brain` · `interview-scorecard-lite` · `meeting-summary` · `work-orders-lite` · `obsidian-markdown` · `obsidian-bases` · `obsidian-cli` · `json-canvas` (danh sách trong `00.7-skills-index.md`).

Chỉ dùng gói thuê bao Claude. Không cần API key.
