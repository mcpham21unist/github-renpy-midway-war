label start:
label a7: # "0532" ko cho thêm máy bay bảo vệ trước khi bị tấn công
    "0700!"
    scene ship10 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc! Phi công Tomonaga sau khi tấn công Midway báo rằng\chúng ta cần 1 đợt tấn công nữa mới vô hiệu hóa được hòn đảo.\""
    tp "Hơn nữa, máy bay địch đang tiến tới hạm đội"
    hide thuyenpho
    jump analysis7
    jump choose7

label choose7:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis7
        "Được rồi":
            jump free7
label analysis7:
    hide thuyenpho
    menu:
        "Phóng máy bay bảo vệ":
            jump close7a
        "Không phóng thêm máy bay, tập trung né":
            jump close7b
        "Đã phân tích xong" :
            jump choose7

label free7:
    menu:
        "Phóng máy bay bảo vệ":
            jump a9
        "Không phóng thêm máy bay, tập trung né":
            jump a8
label close7a:
    show thuyenpho at right:
        size(450,720)
    tp "Đây là một hành động rất nguy hiểm, khi đang bị tấn công, tàu sân bay không thể phóng thêm máy bay mới"
    tp "Tôi chúc đô đốc may mắn cho cuộc tấn công sắp tới"
    jump analysis7

label close7b:
    show thuyenpho at right:
        size(450,720)
    tp "Khi đang bị tấn công, các tàu sân bay tuyệt đối không được phóng máy bay mới,"
    tp "Vì điều này sẽ làm giảm sự cơ động của tàu sân bay, và khiến tàu sân bay dễ bị cháy nổ hơn"
    jump analysis7
