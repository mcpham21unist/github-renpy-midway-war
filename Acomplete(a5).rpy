label a5: # tấn công Midway
    scene plane3 with fade
    "Tuyệt vời, đội máy bay tấn công Midway sẽ có phi công Tomonaga dẫn đầu."
    "Với anh ta, chúng ta có thể yên tâm là Midway sẽ bị vô hiệu hóa."
    "Hãy chúc các phi công trẻ của chúng ta trở lại an toàn."
    scene black with fade
    "0500!"
    scene plane with fade
    "Thông báo! Máy bay trinh thám Tone 4 vì sự cố kĩ thuật đã bị phóng muộn mất 30 phút."
    scene black with fade
    "0532!"
    scene ship8 with fade
    show thuyenpho at right:
        size(450,720)
    tp "Đô đốc! Một máy bay Mĩ Catalina PBY đã phát hiện\ra hạm đội của chúng ta. Chúng ta đã mất yếu tố bất ngờ\""
    tp "Tệ hơn nữa, máy bay thả bom của chúng ta chưa đến đảo Midway,\có nghĩa là máy bay Mĩ ở đảo Midway có thể tấn công hạm đội của t bất cứ lúc nào.\""
    tp "Chúng ta phải làm sao đây"
    hide thuyenpho
    jump analysis5
    jump choose5

label choose5: 
    show thuyenpho at right:
        size(450,720)
        tp: "Đô đốc đã có lựa chọn chưa ạ ?"
        hide thuyenpho
        menu:
        "Chưa ta cần phân tích thêm":
            jump analysis5
        "Được rồi":
            jump free5

label analysis5:
    hide thuyenpho
    menu:
        "không phải bây giờ":
            jump close5a
        "Tân công Midway":     
            jump close5b
        "Đã phân tích xong" :
            jump choose5
label free5:
    menu:
        "Không cho thêm máy bay bảo vệ":
            jump a6
        "Cho thêm máy bay bảo vệ":
            jump a7

label close5a:
    show thuyenpho at right:
        size(450,720)
    tp "Chúng ta đã có nhiều máy bay đang bay trên đầu để bảo vệ hạm đội."
    tp "Hơn nữa, đối phương không thể phản ứng nhanh đến thế được" 
    tp "Chúng ta sẽ có thừa thời gian để chuẩn bị một khi phát hiện máy bay địch"  
     jump analysis5

label close5b:
    show thuyenpho at right:
        size(450,720)
    tp "Có càng nhiều máy bay bảo vệ hạm đội càng an toàn"
    tp "Nhưng phải dùng các máy bay dự trữ, chúng ta sẽ không sẵn sàng nếu phát hiện hạm đội đối phương"
    jump analysis5
