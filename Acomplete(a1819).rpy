label a1819: # Suy đoán tàu sân bay đối phương + Chỉ là tàu bình thường thôi
    scene phongdochoi with fade:
        size(1300,720)
    "Thông báo từ Tomonaga. Đội máy bay của Tomonaga dự định sẽ quay trở lại đây vào 0815."
    "Tin xấu là máy bay của họ sẽ hết nhiên liệu vào 0915. Các máy bay đó hạ cánh sẽ mất khoảng 30 phút."
    "Thế nên họ cần bắt đầu hạ cánh muộn nhất vào 0845 nếu chúng ta không muốn mất thêm máy bay."
    "Phóng máy bay tấn công sẽ tốn khoảng 45 phút thế nên chúng ta\có đến muộn nhất 0800 để phóng trước khi mất máy bay từ đội của Tomonaga.\""
    "Và tệ hơn nữa, tàu sân bay của chúng ta không\ thể đón và phóng máy bay cùng một lúc.\""
    hide thuyenpho
    jump analysis1819
    jump choose1819

label choose1819:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis1819
        "Được rồi":
            jump free1819
label analysis1819:
    hide thuyenpho
    menu:
        "Phóng máy bay tấn công ngay lập tức":     
            jump close1819a
        "Đợi thời gian nghĩ thêm":    
            jump close1819b
        "Phóng máy bay tấn công hạm đội đối phương sau khi Tomohaga hạ cánh":
            jump close1819c
        "Đã phân tích xong" :
            jump choose1819
label free1819:
    menu:
        "Phóng máy bay tấn công ngay lập tức":  
            jump a2122
        "Đợi thời gian nghĩ thêm":  
            jump a2122
        "Phóng máy bay tấn công hạm đội đối phương sau khi Tomohaga hạ cánh":
            jump a161723
label close1819a:
    show thuyenpho at right:
        size(450,720)
    "Danh tính của đối phương vẫn chưa biết, còn vị trí thì còn khả nghi"
    "1 vài máy bay dự trữ vừa thay đổi vũ khí nên chỉ còn 64/78 máy bay tấn công được."
    "Nhưng trong chiến tranh tàu sân bay, ai tấn công trước người đấy thắng."
    jump analysis1819

label close1819b:
    show thuyenpho at right:
        size(450,720)
    "Không máy bay nào của Tomonaga phải bị mất, có đủ thời gian để\chuẩn bị vũ khí trên máy bay nên có thể tấn công với cả 78 máy ba\""
    jump analysis1819
label close1819c:
    show thuyenpho at right:
        size(450,720)
    "Chúng ta có 15 phút để suy nghĩ trước khi phải hy sinh máy bay từ đội của Tomonaga."
    jump analysis1819
