label a93: # Báo cáo tình hình
    scene plane15 with fade
    show thuyenpho at right:
        size(480,720)
    tp "Tất cả tàu sân bay của chúng ta đều có vũ khí, máy bay và nhiên liệu ở dưới sàn bay."
    tp "Và chỉ với 1 quả bom, nó đã khiến cả con tàu Akagi bị cháy"
    tp "Số phận của Kaga, Soryuu đều cũng thế."
    tp "Chúng ta chỉ còn Hiryuu đã né được ngư lôi từ máy bay địch và còn hoạt động được"
    tp "Đô đốc, con tàu Akagi không thể bị cứu được nữa.\Thuyền trưởng hãy chuyển sang con tàu tuần dương nagara để tiếp tục chỉ huy trận chiến\""
    hide thuyenpho
    jump analysis93
    jump choose93

label choose93:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis93
        "Được rồi":
            jump free93
label analysis93:
    hide thuyenpho
    menu:
        "Rút lui":     
            jump close93a
        "Đuổi theo":       
            jump close93b
        "Đã phân tích xong" :
            jump choose93
label free93:
    menu:
        "Rút lui":     
            jump a94
        "Đuổi theo":   
            jump a95
label close93a:
    show thuyenpho at right:
        size(450,720)
    "Tình hình đang là 3 vs 1, Hiyruu là tàu sân bay duy \nhất của Kido Butai, và chúng ta phải bảo vệ cô ấy với mọi giá.\""
    jump analysis93

label close93b:
    show thuyenpho at right:
        size(450,720)
    "Lựa chọn duy nhất mà mọi người Nhật Bản có thể chọn, chúng ta vẫn còn có cơ hội"
    "Chúng ta có thể đuổi kịp trong khoảng thời gian ngắn."
    jump analysis93

