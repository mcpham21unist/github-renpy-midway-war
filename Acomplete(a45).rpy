define tp = Character("Phó Chỉ Huy", color="c8ffc8")
define noti = Character("Thông Báo", color="9FE2BF")
define dmr = Character("Damage Report", color="FF7F50")
label start:

label a45: # tiếp tục phóng máy bay tấn công
    "1010"
    scene ship19 with fade
    noti "Phát hiện máy bay thả ngư lôi địch từ phía đông nam!"
    "Đây quả là một trò đùa, hơn 50 phút rồi có 3 đợt tấn công liên tiếp, trì hoãn đợt tấn công của chúng ta."
    "Điều này chứng tỏ đối phương phải có hơn 1 tàu sân bay."
    "Nhưng từ nãy đến giờ chỉ có máy bay thả ngư lôi, vậy máy bay thả bom của Mĩ đâu?"
    scene black with fade
    "1020"
    scene ship19 with fade
    "Tin xấu! Đợt tấn công lần này của kẻ địch có máy bay chiến đấu."
    "Quân địch đang dùng chiến thuật di chuyển mới, và rất nhiều máy bay zero của chúng ta đang bị bắn hạ"
    "Điều này khiến cho tất cả máy bay zero đều đã ra ngăn cản máy bay địch, khiến hạm đội chúng ta không hề có máy bay bảo vệ trên đầu"
    hide thuyenpho
    jump analysis45
    jump choose45

label choose45:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis45
        "Được rồi":
            jump free45
label analysis45:
    hide thuyenpho
    menu:
        "Gọi máy bay chiến đấu bảo vệ trên đầu":
            jump close45a
        "Để tất cả máy bay tập trung tấn công máy bay địch":
            jump close45b
        "Đã phân tích xong" :
            jump choose45
label free45:
    menu:
        "Gọi máy bay chiến đấu bảo vệ trên đầu":
            jump a4647
        "Để tất cả máy bay tập trung tấn công máy bay địch":
            jump a4647
label close45a:
    show thuyenpho at right:
        size(450,720)
    "Chúng ta cần có máy bay bảo vệ hạm đội trên\đầu đề phòng trường hợp mình bị tấn công từ hướng khác\""
    jump analysis45

label close45b:
    show thuyenpho at right:
        size(450,720)
    "Chúng ta cần tiêu diệt đối thủ trước khi chúng nó có thể lại gần, cách này sẽ hiệu quả hơn."
    jump analysis45
