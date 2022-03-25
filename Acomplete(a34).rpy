label a34: # 0839 báo cáo tình hình
    scene plane11 with fade
    hide thuyenpho
    jump analysis34
    jump choose34

label choose34:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis34
        "Được rồi":
            jump free34
label analysis34:
    hide thuyenpho
    menu:
        "Cho Arashi tiếp tục đuổi theo": 
            jump close34a
        "Gọi Arashi quay lại tàu sân bay":     
            jump close34b
        "Đã phân tích xong" :
            jump choose34
label free34:
    menu:
        "Cho Arashi tiếp tục đuổi theo":
            jump a35
        "Gọi Arashi quay lại tàu sân bay":
            jump xyzxyz
label close34a:
    show thuyenpho at right:
        size(450,720)
    "Con tàu ngầm đó vẫn là mối đe dọa lớn, một ngư lôi từ tàu ngầm đó có thể đánh chìm cả tàu sân bay."
    " Arashi sẽ trở lại sau khi tiêu diệt được tàu  ngầm hoặc là khi nó đi xa quá"
    jump analysis34

label close34b:
    show thuyenpho at right:
        size(450,720)
    "Không nên cho 1 con tàu tách riêng khỏi hạm đội, nó có thể bị tấn công riêng lẻ."
    jump analysis34
