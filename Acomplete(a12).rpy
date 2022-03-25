label a12: # Báo cáo tình hình chiến dịch đợt 1
    scene phongdochoi with fade:
        size(1300,720)
    dmr "Chúng ta đã mất 2 máy bay Zero"
    dmr "Các con tàu còn lại"
    dmr "Trên bầu trời đã hết máy bay địch, cuộc tấn công của địch đã kết thúc."
    dmr "Và đến bây giờ vẫn chưa có thông báo gì từ máy bay trinh thám."
    scene black with fade
    "0715!"
    scene phongdochoi with fade:
        size(1300,720)
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc, tiện thể đang trong thời gian an toàn, ngài cần trả lời yêu cầu của Tomonaga\Chúng ta cần 1 đợt nữa mới phá hủy được sân bay ở Midway.\""
    hide thuyenpho
    jump analysis12
    jump choose12

label choose12:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis12
        "Được rồi":
            jump free12
label analysis12:
    hide thuyenpho
    menu:
        "Tấn công bằng đội máy bay của Tomonaga":
            jump close12a
        "Tấn công bằng máy bay dữ trữ":
            jump close12b
        "Đã phân tích xong" :
            jump choose12

label free12:
    menu:
        "Tấn công bằng đội máy bay của Tomonaga":
            jump a62
        "Tấn công bằng máy bay dữ trữ":
            jump a13

label close12a:
    show thuyenpho at right:
        size(450,720)
    tp "Đợi đội máy bay của Tomonaga quay trở lại, tiếp nhiên liệu và vũ khí, rồi quay lại tấn công"
    tp "Lựa chọn này sẽ tốn rất nhiều thời gian, quân Mĩ có thể\sửa lại sân bay và chuẩn bị phòng thủ, sẽ dẫn đến thêm mạng chết\""
    tp "Rõ"
    jump analysis12

label close12b:
    show thuyenpho at right:
        size(450,720)
    tp "Các máy bay thả ngư lôi dự trữ sẽ thay vũ khí để thả bom. Những máy bay này đang không làm gì"
    tp "Nhưng mình sẽ không có máy bay dự bị trong trường hợp phát hiện tàu sân bay địch"
    tp "Máy bay vừa nãy suýt đâm vào tàu chứng minh rằng midway vẫn là mối đe dọa"
    tp "Rõ"
    jump analysis12
