label a79: # 0839 báo cáo tình hình
    scene plane11 with fade
    hide thuyenpho
    jump analysis79
    jump choose79

label choose79:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis79
        "Được rồi":
            jump free79
label analysis79:
    hide thuyenpho
    menu:
        "Cho Arashi tiếp tục đuổi theo": 
            jump close79a
        "Gọi Arashi quay lại tàu sân bay":   
            jump close79b
        "Đã phân tích xong" :
            jump choose79
label free79:
    menu:
        "Cho Arashi tiếp tục đuổi theo":
            jump a80
        "Gọi Arashi quay lại tàu sân bay":
            jump xyzyz
label close79a:
    show thuyenpho at right:
        size(450,720)
    "Con tàu ngầm đó vẫn là mối đe dọa lớn, một ngư lôi từ tàu ngầm đó có thể đánh chìm cả tàu sân bay."
    " Arashi sẽ trở lại sau khi tiêu diệt được tàu  ngầm hoặc là khi nó đi xa quá"
    jump analysis79

label close79b:
    show thuyenpho at right:
        size(450,720)
    "Không nên cho 1 con tàu tách riêng khỏi hạm đội, nó có thể bị tấn công riêng lẻ."
    jump analysis79
