label a35: # cho arashi tiếp tục đuổi theo
    scene ship2 with fade:
        size(1300,720)
    "Tinh thần của bọn Mĩ mãnh liệt hơn chúng ta đã tưởng, nhưng kĩ năng của họ thì thật đáng xấu hổ."
    "Với tình hình này, chúng ta chắc chắn sẽ giành được chiến thắng."
    "Máy bay đồng minh phát hiện! Đó là đội máy bay của đội Tomonaga đang trở lại."
    hide thuyenpho
    jump analysis35
    jump choose35

label choose35:
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc đã có lựa chọn chưa ạ ?"
    hide thuyenpho
    menu:
        "Chưa ta cần phân tích thêm":
            jump analysis35
        "Được rồi":
            jump free35
label analysis35:
    hide thuyenpho
    menu:
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":
            jump close35a
        "Phóng máy bay tấn công hạm của địch sau khi đội máy bay của Tomonaga hạ cánh":
            jump close35b
        "Đã phân tích xong" :
            jump choose35
label free35:
    menu:
        "Phóng máy bay tấn công hạm đội đối phương ngay lập tức":
            jump a363839
        "Phóng máy bay tấn công hạm của địch sau khi đội máy bay của Tomonaga hạ cánh":
            jump a37
label close35a:
    show thuyenpho at right:
        size(450,720)
    "Danh tính đối phương đã được xác nhận."
    "Với tàu sân bay, địch có thể tấn công bất cứ lúc nào."
    "Chúng ta phải tấn công trước!"
    "Nhưng lưu ý, tấn công lúc này sẽ chắc chắn mất hết 97 máy bay của đội Tomonaga."
    "Và chúng ta sẽ không có máy bay tiêm kích bảo vệ máy bay thả bom vì chúng đã được sử dụng để bảo vệ hạm đội"
    "Thế nên tỉ lệ chúng ta có thể tấn công đối phương an toàn là rất thấp."
    jump analysis35

label close35b:
    show thuyenpho at right:
        size(450,720)
    "Đội máy bay của Tomonaga đã quay trở lại an toàn"
    "chúng ta không thể nhìn họ hy sinh máy bay được. "
    "Chúng ta còn thời gian để nạp nhiên liệu và đạn và tấn công sau khi đón họ trở về"
    jump analysis35
