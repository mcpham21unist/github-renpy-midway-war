label a3: #Ra lệnh cho máy bay trinh thám
    scene plane2 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc, hãy cho máy bay tấn công hải quân Hoa Kì ở Midway nhưu theo kế hoạch."
    hide thuyenpho
    jump analysis3
    jump choose3

label choose3:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis3
        "Được rồi":
            jump free3
label analysis3:
    hide thuyenpho
    menu:
        "không phải bây giờ": 
            jump close3a
        "Tân công Midway":     
            jump close3b
        "Đã phân tích xong" :
            jump choose3
label free3:
    menu:
        "Không phải bây giờ":
            jump a4
        "Tấn công Midway":
            jump a5
label close3a:
    show thuyenpho at right:
        size(450,720)
    tp "Đây là thời điểm tấn công theo kế hoạch, thời tiết thuận lợi\"và máy bay đủ tầm, các phi công đều đã chuẩn bị\""
    jump analysis3

label close3b:
    show thuyenpho at right:
        size(450,720)
    tp  "Nếu chúng ta trì hoãn sự tấn công, thì đối phương sẽ có thêm thời gian\chuẩn bị hoặc còn có thể phản công, thời tiết có thể trở nên xấu đi\""
    jump analysis3
