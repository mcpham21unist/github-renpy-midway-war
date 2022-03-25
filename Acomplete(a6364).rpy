label a6364: # suy đoán tàu sân bay đối phương + chỉ là tàu bình thường
    scene plane14 with fade
    "1 điều tôi thấy lạ về thông báo này của Tone 4, \theo đường bay chỉ định, Tone 4 không thể đi qua hạm đội đối phương được\""
    "Nghĩa là Tone 4 đi sai đường, hoặc là vị trí của hạm đội bị thông báo sai."
    "Hơn nữa, “10 tàu đối phương” có thể có tàu sân bay, hoặc chỉ là tàu khu trực nhỏ."
    "Một tháng trước, tại trận đấu Biển San Hô, đô đốc Takagi đã\tấn công nhầm tàu khu trực của Mĩ thay vì tàu sân bay Mĩ. Chúng ta không thể làm lại lỗi lầm đó\""
    "Ngoài ra, tại sao lại có 1 hạm đội 240 dặm Bắc của Midway?\Không có lí do gì để có 1 hạm đội ở đây trừ khi đó là hạm đội tàu sân bay.\""
    "Quan trọng hơn, theo báo cáo, hạm đội đối phương đang đi vào vùng có gió.\Bình thường tàu sân bay cần có gió để phóng máy bay.\""
    hide thuyenpho
    jump analysis6364
    jump choose6364

label choose6364:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis6364
        "Được rồi":
            jump free6364
label analysis6364:
    hide thuyenpho
    menu:
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":   
            jump close6364a
        "Đợi thời gian nghĩ thêm":   
            jump close6364b
        "Phóng máy bay tấn công hạm đội đối Phương sau khi đội máy bay của Tomonaga hạ cánh": 
            jump close6364c
        "Đã phân tích xong" :
            jump choose6364
label free6364:
    menu:
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":   
            jump a6667
        "Đợi thời gian nghĩ thêm": 
            jump a6667
        "Phóng máy bay tấn công hạm đội đối Phương sau khi đội máy bay của Tomonaga hạ cánh": 
            jump a68
label close6364a:
    show thuyenpho at right:
        size(450,720)
    "Danh tính của đối phương vẫn chưa biết, còn vị trí thì còn khả nghi"
    "1 vài máy bay dự trữ vừa thay đổi vũ khí nên chỉ còn 64/78 máy bay tấn công được."
    "Nhưng trong chiến tranh tàu sân bay, ai tấn công trước người đấy thắng."
    jump analysis6364

label close6364b:
    show thuyenpho at right:
        size(450,720)
    "Không máy bay nào của Tomonaga phải bị mất, có đủ thời gian để\chuẩn bị vũ khí trên máy bay nên có thể tấn công với cả 78 máy ba\""
    jump analysis6364
    
label close6364c:
    show thuyenpho at right:
            size(450,720)
    "Chúng ta có 15 phút để suy nghĩ trước khi phải hy sinh máy bay từ đội của Tomonaga."
    jump analysis6364
