label a13: # "0715" tấn công bằng máy bay dự trữ
    scene plane13 with fade
    "Thay đổi các máy bay thả ngư lôi ở tàu Akagi và Kaga, việc này dự định sẽ tốn 1 tiếng rưỡi."
    "0745!"
    noti "Thông báo! Máy bay Tone 4, cái mà bị trễ lúc trước, đã phát hiện “10 tàu đối phương”."
    hide thuyenpho
    jump analysis13
    jump choose13

label choose13:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis13
        "Được rồi":
            jump free13
label analysis13:
    hide thuyenpho
    menu:
        "Dừng việc thay đổi vũ khí":
            jump close13a
        "Tiếp tục thay đổi vũ khí để tấn công Midway":
            jump close13b
        "Đã phân tích xong" :
            jump choose13
label free13:
    menu:
        "Dừng việc thay đổi vũ khí":
            jump a14
        "Tiếp tục thay đổi vũ khí để tấn công Midway":
            jump a15
label close13a:
    show thuyenpho at right:
        size(450,720)
    tp "Chúng ta phải tấn công mọi tàu đối phương ở xung quanh vùng này để bảo vệ hạm đội trước khi quá muộn"
    jump analysis13

label close13b:
    show thuyenpho at right:
        size(450,720)
    tp  "Midway vẫn là 1 mối đe dọa chúng ta cần phải phá hủy."
    jump analysis13
