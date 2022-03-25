label a49: # Báo cáo tình hình
    scene plane15 with fade
    show thuyenpho at right:
        size(480,720)
    tp "Tất cả tàu sân bay của chúng ta đều có vũ khí, máy bay và nhiên liệu ở dưới sàn bay."
    tp "Và chỉ với 1 quả bom, nó đã khiến cả con tàu Akagi bị cháy"
    tp "Số phận của Kaga, Soryuu đều cũng thế."
    tp "Chúng ta chỉ còn Hiryuu đã né được ngư lôi từ máy bay địch và còn hoạt động được"
    tp "Đô đốc, con tàu Akagi không thể bị cứu được nữa.\Thuyền trưởng hãy chuyển sang con tàu tuần dương nagara để tiếp tục chỉ huy trận chiến\""
    hide thuyenpho
    jump analysis49
    jump choose49

label choose49:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis49
        "Được rồi":
            jump free49
label analysis49:
    hide thuyenpho
    menu:
        "Chìm cùng với tàu": 
            jump close49a
        "Chỉ huy tiếp từ tàu Nagara":    
            jump close49b
        "Đã phân tích xong" :
            jump choose49
label free49:
    menu:
        "Chìm cùng với tàu": 
            jump a51a
        "Chỉ huy tiếp từ tàu Nagara": 
            jump a50
label close49a:
    show thuyenpho at right:
        size(450,720)
    "Thuyền trưởng có trách nghiệm bảo vệ con tàu và thủy thủ của mình, khi tàu chìm,\thuyển trưởng có truyền thống ở lại trên con tàu đang chìm để bảo vệ danh vọng của mình\""
    jump analysis49

label close49b:
    show thuyenpho at right:
        size(450,720)
    "Mình là chỉ huy của cả hạm đội, không có mình là Nhật Bản sẽ\thua trận chiến này, chúng ta cần phải trả thù để bảo toàn được danh vọng\""
    jump analysis49


    
