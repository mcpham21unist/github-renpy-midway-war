label a37: # sau khi Tomohaga hạ cánh
    "0910!"
    scene ship8 with fade
    "Tất cả các phi công trong đội máy bay của Tomonaga đã hạ cánh an toàn."
    "Bây giờ chúng ta phải tính nước đi tiếp theo."
        hide thuyenpho
    jump analysis37
    jump choose37

label choose37:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis37
        "Được rồi":
            jump free37
label analysis37:
    hide thuyenpho
    menu:
        "Tấn công Midway":  
            jump close37a
        "Tấn công hạm đội đối phương":      
            jump close37b
        "Đã phân tích xong" :
            jump choose37
label free37:
    menu:
        "Tấn công Midway":  
            jump a363839
        "Tấn công hạm đội đối phương": 
            jump a363839
label close37a:
    show thuyenpho at right:
        size(450,720)
    "Midway vẫn là mối đe dọa, chúng ta có thể tấn công hạm đội đối phương sau khi vô hiệu hóa Midway."
    jump analysis37

label close37b:
    show thuyenpho at right:
        size(450,720)
    "Tàu sân bay của địch là đối tượng quan trọng nhất và đáng nguy hiểm nhất."
    "Mục đích chính của chiến dịch này là phá hủy tàu sân bay đối phương và bắt Mĩ phải đầu hàng."
    jump analysis37

