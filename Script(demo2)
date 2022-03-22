define tp = Character("Phó Chỉ Huy", color="c8ffc8")
#The game start here
label start:
    tp "Chúng ta có 2 lựa chọn, thuyền trưởng hãy phân tích kĩ ."
    hide thuyenpho
    jump phantich
    jump chon

label chon :
    show thuyenpho at right :
        size(450,720)
    tp "Thuyền trưởng đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu :
        "Chưa, ta cần phân tích thêm" :
            jump phantich
        " Được rồi " :
            jump luachon


label phantich :
    hide thuyenpho
    menu:
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":
            jump next1
        "Phóng máy bay tấn công hạm của địch sau khi đội máy bay của Tomonaga hạ cánh" :
            jump next2
        "Đã phân tích xong" :
            jump chon


label luachon :
    menu :
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":
            jump tiep2
        "Phóng máy bay tấn công hạm của địch sau khi đội máy bay của Tomonaga hạ cánh" :
            jump luachon2


label next1 :
    show thuyenpho at right :
        size(450,720)
    "Danh tính đối phương đã được xác nhận. Với tàu sân bay, địch có thể tấn công bất cứ lúc nào"
    "Chúng ta phải tấn công trước!"
    "Nhưng lưu ý, tấn công lúc này sẽ chắc chắn mất hết 97 máy bay của đội Tomonaga"
    "Và chúng ta sẽ không có máy bay tiêm kích bảo vệ máy bay thả bom"
    "Vì chúng đã được sử dụng để bảo vệ hạm đội, thế nên tỉ lệ chúng ta có thể tấn công đối phương an toàn là rất thấp."
    jump phantich

label next2 :
    "Đội máy bay của Tomonaga đã quay trở lại an toàn, chúng ta không thể nhìn họ mất những chiếc máy bay được"
    "Chúng ta còn thời gian để nạp nhiên liệu, đạn và tấn công sau khi đón họ trở về"
    jump phantich


label luachon2 :
    scene phongchihuy with fade :
        size(1280,720)
    show thuyenpho at right :
        size(450,720)
    tp "Tất cả các phi công trong đội máy bay của Tomonaga đã hạ cánh an toàn"
    tp "Bây giờ chúng ta phải tính nước đi tiếp theo"
    tp "Chúng ta có 2 lựa chọn, xin hãy phân tích kĩ "
