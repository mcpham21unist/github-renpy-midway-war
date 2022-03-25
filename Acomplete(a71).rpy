label a71: # 0810 Báo cáo tình hình
    dmr "Hạm đội của chúng ta không có tổn thương gì.\1 máy bay zero đã bị mất, và đã bắn hạ được gần chục máy bay đối phương.\""
    hide thuyenpho
    jump analysis71
    jump choose71

label choose71:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis71
        "Được rồi":
            jump free71
label analysis71:
    hide thuyenpho
    menu:
        "Phóng máy bay tấn công ngay lập tức":   
            jump close71a
        "Phóng máy bay tấn công sau khi đội máy bay của Tomonaga hạ cánh":     
            jump close71b
        "Đã phân tích xong" :
            jump choose71
label free71:
    menu:
        "Phóng máy bay tấn công ngay lập tức":   
            jump a727374
        "Phóng máy bay tấn công sau khi đội máy bay của Tomonaga hạ cánh":
            jump a727374
label close71a:
    show thuyenpho at right:
        size(450,720)
    tp "Thuyền trưởng, vì cuộc tấn công này, chúng ta đã không thể phóng máy bay tấn công đối phương"
    tp "Tại vì bây giờ đã quá 0800, tấn công đối phương bây giờ\sẽ khiến chúng ta phải hy sinh đa số máy bay trong đội của Tomonaga.\""
    tp "Thuyền trưởng có muốn đổi quyết định không?"
    "danh tính của đối phương vẫn chưa biết, vị trí đối phương thì còn khả nghi."
    "1 vài máy bay dự trũ vừa thay đổi vũ khí nên chỉ còn 64/78 máy bay tấn công được."
    "Nhưng trong chiến tranh tàu sân bay, ai tấn công trước người đấy thắng."
    "Nhưng đa số của 97 máy bay trong đội của Tomonaga sẽ bị mất."
    jump analysis71

label close71b:
    show thuyenpho at right:
        size(450,720)
    "Không máy bay nào của Tomonaga phải bị mất"
    "Có đủ thời gian để chuẩn bị vũ khí trên máy bay nên có thể tấn công với cả 78 máy bay."
    jump analysis71

    
