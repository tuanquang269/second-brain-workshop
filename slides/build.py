#!/usr/bin/env python3
"""Build slides/index.html — 6 anchor slides + 2 drawers (L = tài liệu, B = 10 bài tập).
CSS / nav JS reused from full.html; diagram = slides/anatomy.svg."""
import re, os, html

KIT = "/Users/kevinkreative/PATI/work/second-brain-workshop"
full = open(os.path.join(KIT, "slides/full.html"), encoding="utf-8").read()
STYLE = re.search(r"<style>(.*?)</style>", full, re.S).group(1)
JS = re.search(r"<script>(.*?)</script>", full, re.S).group(1)
ANATOMY = open(os.path.join(KIT, "slides/anatomy.svg"), encoding="utf-8").read()

TITLE_MAIN = "Thực chiến Second Brain + AI"
TITLE_SUB = "Để cơ giới hoá tư duy thành quy trình làm việc"
TITLE_FULL = TITLE_MAIN + " — " + TITLE_SUB

E = html.escape

EXTRA = r"""
/* ---- 6-slide deck ---- */
.slide{padding:7vh 5vw 9vh}
.slide--title h1{font-size:clamp(38px,5.6vw,92px);line-height:1.04}
.slide--title .tsub{font-size:clamp(19px,2.3vw,38px);color:var(--accent);line-height:1.2;text-wrap:balance;font-weight:500}
.slide--ab{align-items:stretch;justify-content:center}
.ab{display:grid;grid-template-columns:1fr auto 1fr;gap:2vw;align-items:center;flex:1;min-height:0}
.ab__col{display:flex;flex-direction:column;gap:3vh;min-width:0}
.ab__col h3{font-family:var(--mono);font-size:clamp(15px,1.6vw,26px);letter-spacing:.16em;text-transform:uppercase;color:var(--dim);font-weight:600}
.ab__col.win h3{color:var(--accent)}
.ab__row{display:flex;flex-direction:column;gap:.4vh}
.ab__n{font-family:var(--mono);font-size:clamp(36px,5.2vw,92px);font-weight:700;line-height:1;letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.ab__col.win .ab__n{color:var(--accent)}
.ab__k{font-size:clamp(14px,1.4vw,23px);color:var(--dim)}
.ab__vs{font-family:var(--mono);font-size:clamp(16px,1.6vw,26px);color:var(--dim);writing-mode:vertical-rl;letter-spacing:.3em;opacity:.6}
.ab .ed{display:inline-block;min-width:2.6ch;border-bottom:3px dashed var(--dim);outline:none;cursor:text}
.ab .ed:focus{border-bottom-color:var(--accent);background:var(--accent-dim)}
.an-host{flex:1;min-height:0;display:flex;align-items:center;justify-content:center}
.an-host svg{width:100%;height:100%;max-height:100%}
.blocks{display:grid;grid-template-columns:repeat(4,1fr);gap:1.4vw;flex:1;min-height:0;align-content:center}
.blk{background:var(--surface);border:1px solid var(--line);border-top:5px solid var(--accent);border-radius:12px;padding:3vh 1.4vw;display:flex;flex-direction:column;gap:1.3vh;min-width:0}
.blk .clock{font-family:var(--mono);font-size:clamp(13px,1.2vw,20px);color:var(--dim);letter-spacing:.06em}
.blk h3{font-size:clamp(21px,2.4vw,42px);font-weight:700;line-height:1.1}
.blk .arrow{font-family:var(--mono);font-size:clamp(12px,1.15vw,19px);color:var(--accent);overflow-wrap:anywhere;line-height:1.4}
a.f{font-family:var(--mono);font-size:clamp(12px,1.1vw,18px);color:var(--teal);text-decoration:none;border-bottom:1px dashed var(--teal);align-self:flex-start;overflow-wrap:anywhere;line-height:1.4;margin-top:auto}
a.f:hover{color:var(--accent);border-bottom-color:var(--accent)}
.slide--lane3 .lanes{flex:1;align-content:center}
.slide--lane3 .lane{gap:1.6vh;justify-content:center;border-top:5px solid var(--teal)}
.slide--lane3 .lane h3{font-size:clamp(25px,2.9vw,50px)}
.slide--lane3 .lane .who{font-family:var(--mono);font-size:clamp(13px,1.2vw,20px);color:var(--dim);letter-spacing:.08em;text-transform:uppercase}
.slide--lane3 .lane .out{font-family:var(--mono);font-size:clamp(13px,1.3vw,22px);color:var(--accent);overflow-wrap:anywhere;margin-top:0}
.close{display:grid;grid-template-columns:3fr 2fr;gap:4vw;align-items:center;flex:1;min-height:0}
.close .rules{gap:2.6vh}
.close .rules li{font-size:clamp(19px,2.3vw,40px);padding-left:2em}
.close .qrbox{max-height:38vh}
.close .url{font-family:var(--mono);font-size:clamp(13px,1.3vw,21px);color:var(--accent);overflow-wrap:anywhere;text-align:center;margin-top:1.4vh;line-height:1.4}
.close .side{display:flex;flex-direction:column;justify-content:center}
.close .dl{display:flex;gap:1vw;justify-content:center;margin-top:1.6vh;flex-wrap:wrap}
.close .dl a{font-family:var(--mono);font-size:clamp(13px,1.3vw,21px);color:var(--text);text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:1vh 1.1vw;background:var(--surface)}
.close .dl a:hover{border-color:var(--accent);color:var(--accent)}
/* ---- drawers ---- */
.dock{position:fixed;inset:0;background:rgba(8,8,7,.96);z-index:20;display:none;padding:5vh 5vw 8vh;overflow:auto}
body.dock-open .dock--links{display:block}
body.ex-open .dock--ex{display:block}
.dock h2{font-size:clamp(22px,2.4vw,40px);font-weight:700;margin-bottom:.5vh}
.dock .sub{font-family:var(--mono);font-size:clamp(12px,1.2vw,19px);color:var(--dim);margin-bottom:2.6vh}
.dock .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:2vw 3vw}
.dock section{display:flex;flex-direction:column;gap:1.2vh}
.dock h3{font-family:var(--mono);font-size:clamp(12px,1.15vw,18px);letter-spacing:.14em;text-transform:uppercase;color:var(--accent);border-bottom:1px solid var(--line);padding-bottom:.8vh}
.dock a{font-family:var(--mono);font-size:clamp(13px,1.25vw,20px);color:var(--text);text-decoration:none;line-height:1.35;overflow-wrap:anywhere}
.dock a:hover{color:var(--accent)}
.dock a span{color:var(--dim);font-family:var(--font);font-size:.85em}
.dock .x{position:fixed;top:2.4vh;right:3vw;font-family:var(--mono);font-size:14px;color:var(--dim);border:1px solid var(--line);border-radius:6px;padding:6px 10px;background:var(--surface);cursor:pointer;z-index:21}
.nav .dockbtn,.nav .exbtn{width:auto;padding:0 10px;font-size:12px;font-family:var(--mono)}
/* exercise cards */
.exs{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:1.6vw 1.6vw}
.ex{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;gap:9px;min-width:0}
.ex.k{border-left:4px solid var(--accent)}
.ex.e{border-left:4px solid var(--teal)}
.ex .hd{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.ex .id{font-family:var(--mono);font-size:14px;font-weight:700;color:var(--accent)}
.ex.e .id{color:var(--teal)}
.ex h4{font-size:18px;font-weight:700;line-height:1.2}
.ex .lane{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--dim);border:1px solid var(--line);border-radius:10px;padding:2px 8px}
.ex .in{font-size:14px;color:var(--dim);line-height:1.4}
.ex .p{position:relative;background:var(--surface2);border:1px solid var(--line);border-radius:8px;padding:26px 12px 10px;font-family:var(--mono);font-size:13px;line-height:1.45;white-space:pre-wrap;overflow-wrap:anywhere;color:var(--text);cursor:copy}
.ex .p:hover{border-color:var(--accent)}
.ex .p::after{content:"⧉ chép";position:absolute;top:6px;right:8px;font-size:10.5px;color:var(--dim);letter-spacing:.08em}
.ex .p.copied::after{content:"✓ đã chép";color:var(--accent)}
.ex .out{font-family:var(--mono);font-size:13px;color:var(--accent);overflow-wrap:anywhere;line-height:1.4}
.ex .dc{font-family:var(--mono);font-size:12.5px;color:var(--teal);line-height:1.4}
.ex a{font-size:12.5px;border-bottom:1px dashed var(--line);align-self:flex-start}
@media (max-width:900px){.ab,.blocks,.close{grid-template-columns:1fr}.ab__vs{display:none}}
"""

REPO = "https://github.com/tuanquang269/second-brain-workshop"
DOCK = [
    ("Tải về · làm 1 lần", [
        ("../starter-brain.zip", "starter-brain.zip", "bộ não mẫu — giải nén, mở bằng Obsidian"),
        ("../demo-data.zip", "demo-data.zip", "dữ liệu mẫu nếu bạn không mang việc thật"),
        ("../pre-work-email.md", "pre-work-email.md", "cài Obsidian + Claude Code"),
        (REPO, "github repo", "toàn bộ bộ kit"),
    ]),
    ("Prompt để gõ", [
        ("full.html", "full.html", "phụ lục: mọi dòng lệnh của 4 trạm"),
        ("../starter-brain/98-templates/skill-template.md", "skill-template.md", "mẫu SKILL.md 4 trường"),
        ("../starter-brain/98-templates/page-template.md", "page-template.md", "mẫu trang kiến thức"),
        ("../starter-brain/00.7-skills-index.md", "00.7-skills-index.md", "8 skill có sẵn + chỗ ghi skill của bạn"),
    ]),
    ("File mẫu · lane HR", [
        ("../demo-data/cv-nguyen-van-a.md", "cv-nguyen-van-a.md", "CV ứng viên 1"),
        ("../demo-data/cv-tran-thi-b.md", "cv-tran-thi-b.md", "CV ứng viên 2"),
        ("../demo-data/job-post-marketing-exec.md", "job-post-marketing-exec.md", "tin tuyển dụng"),
    ]),
    ("File mẫu · lane Ops", [
        ("../demo-data/meeting-2026-08-10.txt", "meeting-2026-08-10.txt", "transcript họp 12 phút"),
        ("../demo-data/sop-order-handling-raw.txt", "sop-order-handling-raw.txt", "voice memo quy trình đơn hàng"),
        ("../demo-data/ticket-042.md", "ticket-042.md", "ticket CSKH cần review trước khi đóng"),
    ]),
    ("File mẫu · lane Mkt", [
        ("../demo-data/emails/promo-1.txt", "promo-1.txt", "email đối thủ 1 — bỏ giỏ"),
        ("../demo-data/emails/promo-2.txt", "promo-2.txt", "email đối thủ 2 — dạy khách"),
        ("../demo-data/emails/promo-3.txt", "promo-3.txt", "email đối thủ 3 — sau mua"),
        ("../demo-data/product-onepager.md", "product-onepager.md", "one-pager sản phẩm"),
    ]),
]

# id, kind, lane, title, input, prompt, output, done-check, demo file (href, label) or None
EX = [
    ("K1", "k", "HR", "Phỏng vấn: câu hỏi + chấm điểm", "1 CV (ẩn tên) + 3 dòng ghi chú sau buổi",
     "/interview-scorecard-lite prep 99-inbox/cv.md role=<vị trí>",
     "40-hr/candidates/<slug>.md + hàng trong candidates.base",
     "5 điểm 1–6 · câu hỏi tiếng Việt · tự xếp hạng trong Base",
     ("../demo-data/cv-nguyen-van-a.md", "cv-nguyen-van-a.md")),
    ("K2", "k", "Video", "Skill video Pixar / len móc / lego", "kịch bản 30 giây",
     "Tạo skill my-video-style: từ kịch bản 30s → storyboard 6 cảnh phong cách <len móc>, mỗi cảnh 1 prompt ảnh + 1 prompt chuyển động; chạy thử với kịch bản này.",
     "10-work/video-<slug>-storyboard.md",
     "6 cảnh · mỗi cảnh gọi tên phong cách · không render", None),
    ("K3", "k", "Mọi lane", "Xin review trước khi đóng việc", "skill bạn vừa viết",
     "Sửa skill vừa tạo: trước khi ghi file cuối, hiện bản nháp, hỏi \"OK / sửa gì?\", chờ trả lời, rồi ghi verdict vào 00.5-log.md. Chạy lại.",
     "dòng verdict trong 00.5-log.md",
     "Claude thật sự dừng lại hỏi · có dòng log",
     ("../demo-data/ticket-042.md", "ticket-042.md")),
    ("K4", "k", "Ops", "Họp → tóm tắt → draft email", "transcript hoặc ghi chú cuộc họp",
     "/meeting-summary 99-inbox/meeting.txt",
     "96-daily/meeting-<date>.md",
     "≥3 việc có người + hạn (không rõ → TBD) · có mục Email draft",
     ("../demo-data/meeting-2026-08-10.txt", "meeting-2026-08-10.txt")),
    ("K5", "k", "Mkt", "Phân tích + tạo chiến dịch email", "3 email đối thủ + 1 sản phẩm",
     "Đọc 99-inbox/emails/, phân tích cấu trúc, viết chiến dịch 3 email cho <sản phẩm> vào 10-work/email-campaign-<slug>.md kèm bảng \"vì sao\".",
     "10-work/email-campaign-<slug>.md",
     "3 subject + 3 body + bảng vì sao",
     ("../demo-data/emails/promo-1.txt", "emails/promo-1..3.txt")),
    ("E1", "e", "CSKH", "Ngân hàng câu trả lời khách", "20 tin nhắn Zalo/FB dán vào 1 file",
     "Distill 99-inbox/inbox.txt → 10-work/cs-reply-bank.md: 8 intent hay gặp, mỗi intent 1 câu trả lời chuẩn ≤60 từ, kèm luật chuyển cấp.",
     "10-work/cs-reply-bank.md",
     "8 intent · đúng giọng brand · có luật chuyển cấp",
     ("../demo-data/ticket-042.md", "ticket-042.md")),
    ("E2", "e", "Quản lý", "Báo cáo tuần từ chat nhóm", "export 1 tuần chat nhóm",
     "Đọc 99-inbox/chat-week.txt → 96-daily/weekly-<date>.md: wins, blockers, decisions, 1 việc nên dừng.",
     "96-daily/weekly-<date>.md",
     "4 mục · mục \"dừng\" gọi tên đúng 1 việc", None),
    ("E3", "e", "Ops", "SOP từ voice memo", "ghi âm 3 phút kể quy trình → text",
     "Đọc 99-inbox/sop-raw.txt → 10-work/sop-<task>.md: bước đánh số, công cụ dùng, checkpoint, khi nào hỏi ai.",
     "10-work/sop-<task>.md",
     "≥6 bước · đồng nghiệp làm theo được, không hỏi lại",
     ("../demo-data/sop-order-handling-raw.txt", "sop-order-handling-raw.txt")),
    ("E4", "e", "Mkt", "Teardown đối thủ", "3 URL đối thủ",
     "Với 3 URL này, viết 10-work/competitor-<name>.md: offer, thang giá, hook, proof, và khoảng trống ta lấy được.",
     "10-work/competitor-<name>.md",
     "mỗi đối thủ 1 dòng \"gap\" cụ thể · cần wifi",
     ("../demo-data/product-onepager.md", "product-onepager.md")),
    ("E5", "e", "HR", "JD + câu hỏi sàng lọc", "5 gạch đầu dòng: vị trí phải làm ra gì",
     "Từ 5 gạch đầu dòng này viết 40-hr/jd-<role>.md ≤1 trang và 40-hr/roles/<role>.md với ≥5 câu hỏi loại trừ.",
     "40-hr/jd-<role>.md + 40-hr/roles/<role>.md",
     "JD ≤1 trang · ≥5 câu loại trừ gắn với deliverable",
     ("../demo-data/job-post-marketing-exec.md", "job-post-marketing-exec.md")),
]

S = []


def add(html_, block, clock, notes, cls=""):
    S.append((html_, block, clock, notes, cls))


def flink(href, text):
    return '<a class="f" href="%s" target="_blank" rel="noopener">%s ↗</a>' % (href, text)


# 1 — title
add('<p class="sub">Finding Camp · 240 phút · thực hành trên máy của bạn</p>'
    '<h1>%s</h1><p class="tsub">%s</p>'
    '<p class="rule">80%% thời gian là bạn gõ · mỗi trạm về nhà bằng 1 file trong Obsidian</p>'
    '<p class="who">Kevin Kreative · PATI Group</p>'
    '<p class="who">Bấm <b style="color:var(--accent)">B</b> = 10 bài tập · <b style="color:var(--accent)">L</b> = file thực hành · '
    % (E(TITLE_MAIN), E(TITLE_SUB))
    + flink("../starter-brain.zip", "starter-brain.zip") + '</p>',
    "MỞ ĐẦU", "0:00",
    "Chào 60 giây rồi mở A/B live — không giảng. Chỉ cho cả phòng 2 phím: B = 10 bài tập (prompt bấm là chép), L = mọi file cần tải.",
    "title")

# 2 — why
ed = '<span class="ed" contenteditable="true" spellcheck="false">__</span>'
add('<div class="ab">'
    '<div class="ab__col"><h3>Chat trần</h3>'
    '<div class="ab__row"><span class="ab__n">250</span><span class="ab__k">từ phải gõ</span></div>'
    f'<div class="ab__row"><span class="ab__n">{ed}</span><span class="ab__k">phút tới file dùng được</span></div>'
    '<div class="ab__row"><span class="ab__n">0</span><span class="ab__k">file còn lại sau Cmd+W</span></div></div>'
    '<div class="ab__vs">so với</div>'
    '<div class="ab__col win"><h3>Bộ não</h3>'
    '<div class="ab__row"><span class="ab__n">7</span><span class="ab__k">từ phải gõ</span></div>'
    f'<div class="ab__row"><span class="ab__n">{ed}</span><span class="ab__k">phút tới file dùng được</span></div>'
    '<div class="ab__row"><span class="ab__n">1</span><span class="ab__k">file + 1 skill giữ lại</span></div></div>'
    '</div>'
    '<p class="caption">Cùng một việc. Đóng tab: một bên mất, một bên còn.</p>',
    "WHY", "0:00–0:20",
    "20'. Chạy A/B thật: pane trái ~/demo-empty + prompt 250 từ · pane phải /interview-scorecard prep. Bấm giờ, gõ số vào 2 ô __, chạy /cost, rồi Cmd+W cả hai. Fallback: hook-ab.mp4.",
    "ab")

# 3 — anatomy
add('<div class="an-host"></div>'
    '<p class="caption">Bốn lớp · ba động từ · sản phẩm ra ngoài não.</p>',
    "WHAT", "0:20–0:30",
    "10'. Vẽ lại từ sơ đồ @namhethong, đã kiểm chứng: 5 loại trang Wiki = 5 giá trị type: trong SCHEMA.md ✓. Sửa 3 chỗ: (1) 4_Kết quả nằm NGOÀI vault — knowledge in, outputs out; (2) file luật phải tên CLAUDE.md — test 2026-08-17 trên Claude Code 2.1.233: CLAUDE.md nạp, AGENTS.md và AGENT.md KHÔNG nạp; (3) chat web không ghi được file, cần agent chạy local. Thêm mistakes.md = học từ lỗi.",
    "an")

# 4 — blocks
blocks = [
    ("0:30–0:55", "Cài đặt", "CLAUDE.md ≤40 dòng", "../pre-work-email.md", "pre-work-email.md"),
    ("0:55–1:35", "Sắp xếp", "10-work/1-&lt;slug&gt;.md", "../demo-data/sop-order-handling-raw.txt", "sop-order-handling-raw.txt"),
    ("1:45–2:40", "Sử dụng", "1 file lane của bạn", "../demo-data.zip", "demo-data.zip"),
    ("2:40–3:45", "Huấn luyện", ".claude/skills/&lt;tên&gt;/SKILL.md", "../starter-brain/98-templates/skill-template.md", "skill-template.md"),
]
tiles = "".join('<div class="blk"><span class="clock">%s</span><h3>%s</h3><span class="arrow">→ %s</span>%s</div>'
                % (c, n, out, flink(h, t)) for c, n, out, h, t in blocks)
add('<div class="blocks">%s</div>'
    '<p class="caption">Bốn trạm. Mỗi trạm về nhà bằng một file.</p>' % tiles,
    "HOW", "0:30–3:45",
    "Nói 60 giây rồi vào việc. Dòng lệnh từng trạm: bấm L → full.html. Nghỉ 1:35–1:45, helper chạy login clinic.",
    "blocks")

# 5 — lanes
lanes = [
    ("HR", "tuyển dụng", "1 CV → câu hỏi + điểm", "40-hr/candidates/&lt;slug&gt;.md",
     "../demo-data/cv-nguyen-van-a.md", "cv-nguyen-van-a.md"),
    ("Ops", "vận hành", "transcript họp → quyết định + việc", "96-daily/meeting-&lt;date&gt;.md",
     "../demo-data/meeting-2026-08-10.txt", "meeting-2026-08-10.txt"),
    ("Mkt", "marketing", "3 email đối thủ → chiến dịch 3 email", "10-work/email-campaign-&lt;slug&gt;.md",
     "../demo-data/emails/promo-1.txt", "emails/promo-1..3.txt"),
]
lt = "".join('<div class="lane"><span class="who">%s</span><h3>%s</h3><p class="dc">%s</p>'
             '<p class="out">→ %s</p>%s</div>' % (w, n, d, o, flink(h, t))
             for n, w, d, o, h, t in lanes)
add('<div class="lanes">%s</div>'
    '<p class="caption">Chọn 1 lane để chạy tại lớp — <b style="color:var(--accent)">bấm B</b> để xem cả 10 bài tập.</p>' % lt,
    "SỬ DỤNG", "1:45–2:40",
    "55'. 3 lane là mặc định; ai xong sớm mở B chọn thêm bài (E1–E5). Prompt trong B bấm một cái là chép, dán thẳng vào Claude Code. Không render video, không gửi mail — dừng ở file .md.",
    "lane3")

# 6 — close
add('<div class="close">'
    '<ol class="rules">'
    '<li><b>Phân vân → inbox.</b></li>'
    '<li><b>Mỗi ngày 1–2 note.</b> Hệ thống tự lớn.</li>'
    '<li><b>Mở não mỗi sáng:</b> đọc log 2 phút, chạy 1 skill.</li>'
    '</ol>'
    '<div class="side"><div class="qrbox">'
    '<figure class="shot"><img src="img/qr-deck.png" alt="" onerror="this.parentElement.classList.add(\'missing\')">'
    '<figcaption class="shot__todo"><b>▢ CHỤP · img/qr-deck.png</b>'
    '<span>QR trỏ tới https://tuanquang269.github.io/second-brain-workshop/</span></figcaption></figure>'
    '</div><p class="url">tuanquang269.github.io/<br>second-brain-workshop</p>'
    '<div class="dl"><a href="../starter-brain.zip" target="_blank" rel="noopener">↓ starter-brain.zip</a>'
    '<a href="../demo-data.zip" target="_blank" rel="noopener">↓ demo-data.zip</a></div>'
    '</div></div>'
    '<p class="caption">Quét hoặc bấm: bộ não mẫu, dữ liệu mẫu, 10 bài tập.</p>',
    "KẾT", "3:45–4:00",
    "15'. Tường kết quả → 3 luật → QR. Nhắc mỗi người chọn 1 bài trong B làm thứ Hai. Zip cũng có trên USB nếu wifi chết.",
    "close")

sections = []
for html_, block, clock, notes, cls in S:
    c = "slide" + (" slide--" + cls if cls else "")
    sections.append('<section class="%s" data-block="%s" data-clock="%s" data-notes="%s">\n%s\n</section>'
                    % (c, block, clock, notes.replace('"', "&quot;"), html_))

# ---- drawer: links ----
links_dock = ['<aside class="dock dock--links"><button class="x" data-close="dock">ĐÓNG · L</button>',
              '<h2>Tài liệu thực hành</h2>',
              '<p class="sub">Click là mở. Mọi file nằm trong repo — dùng được cả khi chiếu offline.</p>',
              '<div class="cols">']
for title, items in DOCK:
    links_dock.append("<section><h3>%s</h3>" % title)
    for href, name, desc in items:
        links_dock.append('<a href="%s" target="_blank" rel="noopener">%s<br><span>%s</span></a>' % (href, name, desc))
    links_dock.append("</section>")
links_dock.append("</div></aside>")

# ---- drawer: exercises ----
ex_dock = ['<aside class="dock dock--ex"><button class="x" data-close="ex">ĐÓNG · B</button>',
           '<h2>10 bài tập — chọn bài đúng việc của bạn</h2>',
           '<p class="sub">K = 5 bài chính chạy tại lớp · E = 5 bài thêm khi bạn xong sớm. Bấm vào khối prompt để chép.</p>',
           '<div class="exs">']
for eid, kind, lane, title, inp, prompt, out, dc, demo in EX:
    card = ['<div class="ex %s">' % kind,
            '<div class="hd"><span class="id">%s</span><h4>%s</h4><span class="lane">%s</span></div>' % (eid, E(title), E(lane)),
            '<p class="in">vào: %s</p>' % E(inp),
            '<div class="p" data-copy="%s">%s</div>' % (E(prompt), E(prompt)),
            '<p class="out">→ %s</p>' % E(out),
            '<p class="dc">✓ %s</p>' % E(dc)]
    if demo:
        card.append('<a href="%s" target="_blank" rel="noopener">file mẫu: %s ↗</a>' % (demo[0], demo[1]))
    card.append("</div>")
    ex_dock.append("".join(card))
ex_dock.append("</div></aside>")

DRAWER_JS = r"""
(function(){
  function set(cls,on){document.body.classList.toggle(cls,on);}
  function only(cls){var on=!document.body.classList.contains(cls);set('dock-open',false);set('ex-open',false);set(cls,on);}
  document.querySelector('.dockbtn').addEventListener('click',function(){only('dock-open');});
  document.querySelector('.exbtn').addEventListener('click',function(){only('ex-open');});
  document.querySelectorAll('[data-close]').forEach(function(b){b.addEventListener('click',function(){set('dock-open',false);set('ex-open',false);});});
  document.addEventListener('keydown',function(e){
    if(e.target.isContentEditable||/^(INPUT|TEXTAREA)$/.test(e.target.tagName))return;
    var k=e.key;
    if(k==='l'||k==='L'){only('dock-open');}
    else if(k==='b'||k==='B'){only('ex-open');}
    else if(k==='Escape'){set('dock-open',false);set('ex-open',false);}
  });
  document.querySelectorAll('.ex .p').forEach(function(p){
    p.addEventListener('click',function(){
      var t=p.getAttribute('data-copy');
      var done=function(){p.classList.add('copied');setTimeout(function(){p.classList.remove('copied');},1600);};
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(done,done);}
      else{var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy');}catch(err){}a.remove();done();}
    });
  });
})();
"""

page = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="Workshop 240 phút. 6 slide mốc · B = 10 bài tập (prompt chép được) · L = file thực hành · full.html = mọi dòng lệnh.">
<style>%s%s</style>
</head>
<body>
<main class="deck">
%s
</main>
<div class="progress"></div>
<div class="nav"><button data-go="-1" title="Slide trước (←)">‹</button><span class="counter">1 / %d</span><button data-go="1" title="Slide sau (→)">›</button><button class="exbtn" title="10 bài tập (B)">🎯 Bài tập</button><button class="dockbtn" title="Tài liệu thực hành (L)">📎 Tài liệu</button></div>
<div class="hints">← → Space · F toàn màn hình · N ghi chú · <b style="color:var(--accent)">B bài tập</b> · <b style="color:var(--accent)">L tài liệu</b></div>
<aside class="notes"><b>Ghi chú diễn giả</b><p></p></aside>
%s
%s
<template id="an-tpl">
%s
</template>
<script>%s
(function(){var tpl=document.getElementById('an-tpl');document.querySelectorAll('.an-host').forEach(function(h){h.appendChild(tpl.content.cloneNode(true));});})();
%s</script>
</body>
</html>
""" % (E(TITLE_FULL), STYLE, EXTRA, "\n\n".join(sections), len(S),
       "\n".join(links_dock), "\n".join(ex_dock), ANATOMY, JS, DRAWER_JS)

open(os.path.join(KIT, "slides/index.html"), "w", encoding="utf-8").write(page)
print("slides:", len(S), "| exercises:", len(EX), "| links:", sum(len(i) for _, i in DOCK), "| bytes:", len(page))
