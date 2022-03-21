define tp = Character("Thuyenpho", color="c8ffc8")

#The game start here
label start:
    scene black with fade
    "0430!"
    scene phongdochoi with fade
    show thuyenpho at right:
        size(450,720)
    tp "Thuyền trưởng, theo như kế hoạch, bây giờ chúng ta phải phóng,\"các máy bay trinh thám để quan sát mặt trận phía trước.\""
    menu:
        "Chúng ta ra lệnh cho máy bay trinh thám":
            jump trinhtham1
label trinhtham1:
    scene ship3 with fade
        menu:
            "Không phải bây giờ":
                jump Endingfire1
            "Tấn công Midway":
                jump a1
label at:
    scene black with fade
    "0532!"
    scene plane with fade
    show thuyenpho at right:
        size(450,720)
    tp "Trước khi bị tấn công, chúng ta có nên cho thêm máy bay bảo vệ không?"
    menu:
        "Cho thêm máy bay bảo vệ":
            jump a2
        "Không cho thêm máy bay bảo vệ":
            jump a2
label a2:
    scene black with fade
    "0700!"
    scene ship10 with fade
    menu:
        "Né máy bay địch không phóng máy bay ta":
            jump a3
        "Khôn phóng máy bay bảo vệ":
            jump Endingfire4
label a3:
    scene ship12 with fade
    menu:
        "Sử dụng súng phòng không lần thứ nhất":
            jump a4
label a4:
    scene ship 13 with fade
    menu:
        "Sử dụng súng phòng không lần thứ hai":
            jump a5
label a5:
    scene phongdochoi with fade
    show thuyenpho at right:
        size(450,720)
    menu:
        "Báo cáo nội dung tổng kết sau trận chiến đợt 1":
            jump a6
label a6:
    return
