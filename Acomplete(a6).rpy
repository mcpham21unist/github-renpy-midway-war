label a6: # "0532" cho máy bay bảo vệ trước khi bị tấn công
    "0700!"
    scene ship10 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Báo cáo! Có 1 máy bay ném bom đang tiến tới tàu của chúng ta."
    tp "Không thể nào"
    tp "Máy bay đó đang cháy, mà vẫn nhắm tới chúng ta."
    tp "Cúi đầu xuống!"
    "Bọn Mĩ không thể dũng cảm như thế này được"
    "Chắc chắn là do bộ điều khiển của nó đã bị hỏng"
    "Cái máy bay đó đã đâm trượt tàu của mình, nhưng vài thủy thủ đã bị thương\ Họ đã được đưa đến phòng y tế.\""
    tp "Đô đốc! Phi công Tomonaga sau khi tấn công Midway báo rằng\chúng ta cần 1 đợt tấn công nữa mới vô hiệu hóa được hòn đảo.\""
    tp "Hơn nữa, máy bay địch đang tiến tới hạm đội"
    hide thuyenpho
    jump analysis6
    jump choose6

label choose6:
     show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis6
        "Được rồi":
            jump free6

label analysis6:
    hide thuyenpho
    menu:
        "Phóng máy bay bảo vệ": 
            jump close6a
        "Không phóng thêm máy bay, tập trung né":    
            jump close6b
        "Đã phân tích xong":
            jump choose6
label free6:
    menu:
        "Phóng máy bay bảo vệ": 
            jump a9
        "Không phóng thêm máy bay, tập trung né": 
            jump a8
label close6a:
     show thuyenpho at right:
        size(450,720)
    tp "Đây là một hành động rất nguy hiểm, khi đang bị tấn công, tàu sân bay không thể phóng thêm máy bay mới"
    tp "Tôi chúc đô đốc may mắn cho cuộc tấn công sắp tới"
    jump analysis6

label close6b:
    show thuyenpho at right:
        size(450,720)
    tp "Khi đang bị tấn công, các tàu sân bay tuyệt đối không được phóng máy bay mới"
    tp "Vì điều này sẽ làm giảm sự cơ động của tàu sân bay, và khiến tàu sân bay dễ bị cháy nổ hơn"
    jump analysis6
