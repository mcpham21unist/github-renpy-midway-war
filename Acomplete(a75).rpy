label a75: # Chuẩn bị né
    "0820!"
    scene soryuu with fade
    "Bọn chúng đã tấn công Soryuu, Hiryuu và Akagi"
    "Nhưng ở trên độ cao đó, độ chính xác của đối phương cũng bị giảm"
    "Hạm đội của chúng ta không bị sát thương nào"
    noti "Thông báo! Thông tin đưa về từ máy bay trinh sát Tone 4"
    "Có lẽ chiếc tàu sân bay kia đi theo hạm đội chúng"
    hide thuyenpho
    jump analysis75
    jump choose75

label choose75:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis75
        "Được rồi":
            jump free75
label analysis75:
    hide thuyenpho
    menu:
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":      
            jump close75a
        "Phóng máy bay tấn công hạm đội đối phương sau khi đội máy bay của Tomonaga hạ cánh":    
            jump close75b
        "Đã phân tích xong" :
            jump choose75
label free75:
    menu:
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":      
            jump a7677
        "Phóng máy bay tấn công hạm đội đối phương sau khi đội máy bay của Tomonaga hạ cánh": 
            jump a7677
            
label close75a:
    show thuyenpho at right:
        size(450,720)
    "Danh tính đối phương đã được xác nhận."
    "Với tàu sân bay, đối phương có thể tấn công bất cứ lúc nào."
    "Chúng ta phải tấn công trước! Nhưng lưu ý, tấn công lúc này sẽ chắc chắn mất hết 97 máy bay của đội Tomonaga."
    "Và chúng ta sẽ không có máy bay tiêm kích bảo kê máy bay thả bom vì chúng đã được sử dụng để bảo vệ hạm đội"
    "thế nên tỉ lệ chúng ta có thể tấn công đối phương an toàn là rất thấp."
    jump analysis75

label close75b:
    show thuyenpho at right:
        size(450,720)
    "Không máy bay nào của Tomonaga phải bị mất"
    "có đủ thời gian để chuẩn bị vũ khí trên máy bay nên có thể tấn công với cả 78 máy bay."
    jump analysis75
