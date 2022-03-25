label a50: # tháo chạy bằng xuồng và chỉ huy tiếp từ tàu Nagara
    scene ship5 with fade:
        size(1300,720)
    show thuyenpho at right:
        size(480,720)
    tp "Chào mừng thuyền trưởng trên con tàu tuần dương hạng nhẹ Nagara, kỳ hạm tạm thời của chúng ta."
    tp "Chúng ta còn mỗi con tàu sân bay Hiryuu được chỉ huy bởi Yamaguchi."
    tp "Hiryuu vẫn có đội máy bay thả bom giỏi nhất của Nhật Bản,\ những phi công trẻ của chúng ta đã sẵn sàng để trả thù, vì danh vọng của tổ quốc.\""
    tp "Nhưng theo số máy bay đối phương,\ tôi dự đoán là Mĩ đang có 3 tàu sân bay đang tham gia trận chiến này\""
    tp "Chúng ta có lệnh từ đô đốc Yamamoto, chỉ huy toàn bộ hải quân Nhật Bản."
    tp "Ông ấy muốn chúng ta tìm và tấn công hạm đội Mỹ trực tiếp\ Ông ấy đã ra lệnh cho một số chiến hạm làm viện trợ cho chúng ta.\""
    tp "Hơn nữa, 2 tàu sân bay hạng nhẹ Junyo và Ryujo cũng sẽ đến tiếp viện cho chúng ta."
    tp "Nhưng tất cả viện trợ này đang ở rất xa chúng ta và sẽ không có thể đến kịp thời gian được"
    tp "Tại vì hạm đội đối phương có vẻ như đang đi theo hướng Đông Nam,\ và đang tăng khoảng cách với mình. Thế nên chỉ có Hiryuu là có thể tấn công thôi\""
    tp "Cả tương lai của Nhật Bản đang đặt trên vai của thuyền trưởng."
    hide thuyenpho
    jump analysis50
    jump choose50

label choose50:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis50
        "Được rồi":
            jump free50
label analysis50:
    hide thuyenpho
    menu:
        "Rút lui":
            jump close50a
        "Đuổi theo":
            jump close50b
        "Đã phân tích xong" :
            jump choose50
label free50:
    menu:
        "Rút lui":
            jump a52
        "Đuổi theo":
            jump a51
label close50a:
    show thuyenpho at right:
        size(450,720)
    "Tình hình đang là 3 vs 1, Hiyruu là tàu sân bay duy \nhất của Kido Butai, và chúng ta phải bảo vệ cô ấy với mọi giá.\""
    jump analysis50

label close50b:
    show thuyenpho at right:
        size(450,720)
    "Lựa chọn duy nhất mà mọi người Nhật Bản có thể chọn, chúng ta vẫn còn có cơ hội"
    "để lật đảo cuộc chiến này. Kẻ địch đã chạy ra ngoài tâm của chúng ta,"
    "nhưng chúng ta có thể đuổi kịp trong khoảng thời gian ngắn."
    jump analysis50
